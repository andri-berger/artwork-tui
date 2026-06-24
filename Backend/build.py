from playwright.async_api import async_playwright
from textual.app import App, ComposeResult
from .script import (script_f0,
                     script_f1,
                     script_f4,
                     script_f2,
                     script_f3)
from .model import MainTab
from .builds import MainApp
from pathlib import Path
import http.server
import threading
import functools
import json
import time

PORT = Path(__file__).parent
PORT_0 = PORT.parent / "Fontend"
PORT_1 = PORT.parent / "Formula"
PATH_1 = PORT_0 / "style.tcss"
PATH_2 = PORT_0 / "build.json"
PATH_3 = PORT_1 / "za.json"
PATH = ("http://localhost:"
       "9000/build.html")

class CLIApp(App):
    AUTO_FOCUS = None
    COMMAND_PALETTE_DISPLAY = None
    ENABLE_COMMAND_PALETTE = False
    NOTIFICATION_TIMEOUT = 10
    CSS_PATH = PATH_1

    def __init__(self) -> None:
        super().__init__()
        self.vertical = 1
        self.horizontal = 0
        self.clipboards = ""
        self.textfield = ""
        self.textfields = None
        self.playwright = None
        self.store = json.loads(
            PATH_2.read_text())
        self.stores = json.loads(
            PATH_3.read_text()) \
            if PATH_3.exists() else {}

        f0 = self.store or {}
        f0["1-4"] = script_f4(0)
        f0["1-5"] = script_f4(1)
        f0["2-4"] = script_f2()
        f0["2-5"] = script_f3()
        f0["00"] = [
            script_f0("1"),
            script_f0("2"),
            script_f0("-3"),
            script_f0("808080"),
            script_f0("ffffff"),
            script_f1("ffffff"),
            script_f1("808080"),
            script_f1("0"),
            script_f1("1"),
            script_f1("2")]

    async def on_mount(self) -> None:
        f0 = self.query_one(MainTab)
        f1 = ("localhost", 9000)
        f2 = functools.partial(
            http.server.
            SimpleHTTPRequestHandler,
            directory=str(PORT_0))
        f3 = (http.server.
              HTTPServer(f1, f2))
        threading.Thread(
            target=f3.serve_forever,
            daemon=True).start()

        f4 = await async_playwright().start()
        f5 = await f4.chromium.launch(headless=True)
        self.playwright = await f5.new_page()
        await self.playwright.goto(PATH)
        f6 = self.stores.get("0")

        if f6 is None:
            self.notify("No")
            f10 = self.stores
            f11 = int(time.time())
            f12 = f10.setdefault('0', {})
            f13 = f12.setdefault('39', {})
            for k in ['0', '1', '2']:
                    f13[k] = f11

        elif f6 is not None:
            self.notify("Yes")
            f14 = {**self.stores}
            f15 = 1 if f14 else 2
            f14['_'] = [2,f15]
            f0.config = f14

    def compose(self) -> ComposeResult:
        yield MainApp()
