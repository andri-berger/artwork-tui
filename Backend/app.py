from playwright.async_api import async_playwright
from textual.app import App, ComposeResult
from .table import TableApp
from pathlib import Path
import http.server
import threading
import functools
import json
import time


BINDINGS = {
      "quit":    ("q", "Quit"),
      "edit":    ("f2", "Edit cell"),
      "yank":    ("y", "Yank"),
      "paste":   ("p", "Paste"),
}

PORT = 9000
PATH_FILE = Path(__file__).parent
STATIC_DIR = PATH_FILE.parent / "Fontend"
DIR = f"http://localhost:{PORT}/model.html"
CSS_PATHS = STATIC_DIR / "style.tcss"
CONFIG = STATIC_DIR / "build.json"





class CLIApp(App):
    # COMMAND_PALETTE_DISPLAY = None
    COMMAND_PALETTE_BINDING = 'ctrl+p'
    CSS_PATH = CSS_PATHS
    AUTO_FOCUS = '*'

    def __init__(self):
        super().__init__()
        self.page = None
        self._pw = None
        self._server = None
        with open(CONFIG) as f:
            self.config = json.load(f)

        rows0 = []
        self.config["001-2"] = [
        *([f"A{n:02d}" for n in range(100)] * 10),
        *([f"B{n:02d}" for n in range(100)] * 10),
        *([f"C{n:02d}" for n in range(100)] * 10),
        *([f"D{n:02d}" for n in range(100)] * 10),
        *([f"E{n:02d}" for n in range(100)] * 10),
        *([f"F{n:02d}" for n in range(100)] * 10)]

        for letter in "ABCDEF":
            row0 = [f"{letter}{n:02d}"
                for n in range(100)]
            rows0.extend([row0] * 10)
            keys0 = [f"{l}{n:02d}"
                for l in "ABCDEF"
                for n in range(100)]
            keys1 = [f"{l}{n:02d}"
                for l in "ABCDEF"
                for n in range(100)]

        self.config["01-2"] = rows0
        self.config["01-2"] = [
            *([keys1] * 10)
        ]




    def compose(self) -> ComposeResult:
        yield TableApp()

    async def on_mount(self) -> None:
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

    async def on_unmount(self) -> None:
        if self._server:
            self._server.shutdown()
        if self._pw:
        # if self.page:
            await self._pw.stop()
