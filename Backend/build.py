from playwright.async_api import async_playwright
from textual.app import App, ComposeResult
from .script import (make_layer,
make_layers, make_new, make_news, make_news_0)
from .model import ImageTab
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
CSS_PATHS = STATIC_DIR / "style.tcss"
CONFIG = STATIC_DIR / "build.json"
CONFIGS = STATIC_DIR / "model.json"


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
        self.store = json.loads(
            CONFIG.read_text())
        self.stores = json.loads(
            CONFIGS.read_text()) \
            if CONFIGS.exists() else {}

        self.store["1-4"] = make_new("Image")
        self.store["1-5"] = make_new("Text")
        self.store["2-4"] = make_news_0("Image")
        self.store["2-5"] = make_news_0("Text")
        self.store["3-4"] = make_news("Image")
        self.store["3-5"] = make_news("Text")

        self.store["00"] = [
            make_layer("1"),
            make_layer("2"),
            make_layer("-3"),
            make_layer("808080"),
            make_layer("ffffff"),
            make_layers("ffffff"),
            make_layers("808080"),
            make_layers("0"),
            make_layers("1"),
            make_layers("2")]


    def compose(self) -> ComposeResult:
        yield TableApp()

    async def on_mount(self) -> None:
        self.e_images = self.query_one(ImageTab)
        dt = self.query_one("#data-table-0")
        self.set_focus(dt)

        handler = functools.partial(
            http.server.SimpleHTTPRequestHandler,
            directory=str(STATIC_DIR))
        self._server = http.server.HTTPServer(
            ("localhost", PORT), handler)
        thread = threading.Thread(
            target=self._server.serve_forever,
            daemon=True)
        thread.start()

        self._pw = await async_playwright().start()
        browser = await self._pw.chromium.launch(
        headless=True)
        self.page = await browser.new_page()
        await self.page.goto(DIR)

        l0 = {**self.stores}
        l0['_'] = 1 if self.stores else 2
        self.e_images.config = l0

    async def on_unmount(self) -> None:
        if self._server:
            self._server.shutdown()
        if self._pw:
        # if self.page:
            await self._pw.stop()
