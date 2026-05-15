from playwright.async_api import async_playwright
from textual.app import App, ComposeResult
from .main_0 import TableApp
from pathlib import Path
from .main_1 import ImageTab
import http.server
import threading
import functools
import json


BINDINGS = {
      "quit":    ("q", "Quit"),
      "edit":    ("f2", "Edit cell"),
      "yank":    ("y", "Yank"),
      "paste":   ("p", "Paste")}

PORT = 9000
PATH_FILE = Path(__file__).parent
STATIC_DIR = PATH_FILE.parent / "Fontend"
DIR = f"http://localhost:{PORT}/model.html"
CSS_PATHS = STATIC_DIR / "style.tcss"
CONFIG = STATIC_DIR / "build.json"
with open(CONFIG) as f:
    CONF = json.load(f)


class CLIApp(App):
    COMMAND_PALETTE_DISPLAY = None
    NOTIFICATION_TIMEOUT = 10
    CSS_PATH = CSS_PATHS
    AUTO_FOCUS = '*'

    def __init__(self):
        super().__init__()
        self.page = None
        self._pw = None
        self._server = None
        self.configs = {}
        with open(CONFIG) as f:
            self.config = json.load(f)

    def compose(self) -> ComposeResult:
        yield TableApp()

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

    async def on_mount(self) -> None:
        self.set_focus(self.query_one("#data-table-0"))
        handler = functools.partial(
            http.server.SimpleHTTPRequestHandler,
            directory=str(STATIC_DIR)
        )
        self._server = http.server.HTTPServer(("localhost", PORT), handler)
        thread = threading.Thread(target=self._server.serve_forever, daemon=True)
        thread.start()

        self._pw = await async_playwright().start()
        browser = await self._pw.chromium.launch(
        headless=True)
        self.page = await browser.new_page()
        await self.page.goto(DIR)
        # self.query_one(ImageTab).config = self.configs

    async def on_unmount(self) -> None:
        if self._server:
            self._server.shutdown()
        if self._pw:
        # if self.page:
            await self._pw.stop()
