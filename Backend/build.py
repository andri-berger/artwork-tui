from playwright.async_api import async_playwright
from textual.app import App, ComposeResult
from .script import make_layer, make_sparse_layer
from .builds import TableApp
from pathlib import Path
import http.server
import threading
import functools
import json




PORT = 9000
PATH_FILE = Path(__file__).parent
STATIC_DIR = PATH_FILE.parent / "Fontend"
DIR = f"http://localhost:{PORT}/build.html"
CSS_PATHS = STATIC_DIR / "build.tcss"
CONFIG = STATIC_DIR / "build.json"
CONFIGS = STATIC_DIR / "models.json"


# import json
# from pathlib import Path
# from platformdirs import user_data_dir
#
#   STATE_FILE = Path(user_data_dir("layoutgen")) / "state.json"
#
#   # on exit — dump DataTable
#   def save_state(self) -> None:
#       table = self.query_one(DataTable)
#       data = self.get_all_data(table)
#       STATE_FILE.parent.mkdir(parents=True, exist_ok=True)
#       STATE_FILE.write_text(json.dumps(data, indent=2))
#
#   # on launch — restore DataTable
#   def load_state(self) -> dict:
#       if STATE_FILE.exists():
#           return json.loads(STATE_FILE.read_text())
#       return {}
#
#   class CLIApp(App):
#       async def on_mount(self) -> None:
#           data = load_state()
#           table = self.query_one(DataTable)
#           for row in data.values():
#               table.add_row(*row.values())
#
#       async def on_unmount(self) -> None:
#           save_state(self)

# # serve.py
# import http.server, socketserver
#
# class Handler(http.server.SimpleHTTPRequestHandler):
#     def end_headers(self):
#         self.send_header("Content-Security-Policy", "")
#         self.send_header("Cross-Origin-Embedder-Policy", "unsafe-none")
#         super().end_headers()
#
# with socketserver.TCPServer(("", 9000), Handler) as httpd:
#     httpd.serve_forever()
# handler = functools.partial(
#     NoCacheHandler,
#     directory=str(STATIC_DIR))


# class NoCacheHandler(http.server.SimpleHTTPRequestHandler):
#     def end_headers(self):
#         self.send_header("Cache-Control", "no-store, no-cache, must-revalidate")
#         self.send_header("Pragma", "no-cache")
#         self.send_header("Expires", "0")
#         super().end_headers()

class CLIApp(App):
    COMMAND_PALETTE_DISPLAY = None
    NOTIFICATION_TIMEOUT = 2
    CSS_PATH = CSS_PATHS
    AUTO_FOCUS = '*'

    def __init__(self):
        super().__init__()
        self.helpful = {}
        self.page = None
        self._pw = None
        self._server = None
        with open(CONFIG) as f:
            self.store = json.load(f)
        self.stores = json.loads(
            CONFIGS.read_text()) \
            if CONFIGS.exists() else {}

        self.store["00"] = [
            make_layer("1"),
            make_layer("2"),
            make_layer("-3"),
            make_layer("808080"),
            make_layer("ffffff"),
            make_sparse_layer(300, "ffffff", 300),
            make_sparse_layer(300, "808080", 300),
            make_sparse_layer(300, "0", 300),
            make_sparse_layer(300, "1", 300),
            make_sparse_layer(300, "2", 300)]


    def compose(self) -> ComposeResult:
        yield TableApp()

    async def on_mount(self) -> None:
        dt = self.query_one(
            "#data-table-0")
        self.set_focus(dt)
        handler = functools.partial(
            http.server.SimpleHTTPRequestHandler,
            directory=str(STATIC_DIR))
        self._server = http.server.HTTPServer(("localhost", PORT), handler)
        thread = threading.Thread(target=self._server.serve_forever, daemon=True)
        thread.start()

        self._pw = await async_playwright().start()
        browser = await self._pw.chromium.launch(
        headless=True)
        self.page = await browser.new_page()
        await self.page.goto(DIR)
        # self.query_one(ImageTab).store = self.configs

    async def on_unmount(self) -> None:
        if self._server:
            self._server.shutdown()
        if self._pw:
        # if self.page:
            await self._pw.stop()
