import functools
import http.server
import json
import threading
import time
from pathlib import Path

from playwright.async_api import async_playwright
from textual.app import App, ComposeResult

from .builds import MainApp
from .model import MainTab
from .script import (
    script_f0,
    script_f1,
    script_f2,
    script_f3,
    script_f4,
)

PORT = Path(__file__).parent
PORT_0 = PORT.parent / "Fontend"
PORT_1 = PORT.parent / "Formula"
PATH_1 = PORT_0 / "style.tcss"
PATH_2 = PORT_0 / "build.json"
PATH_3 = PORT_1 / "var.json"
PATH = "http://localhost:9000/build.html"


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
            PATH_2.read_text()
        )
        self.stores = (
            json.loads(PATH_3.read_text())
            if PATH_3.exists()
            else {}
        )

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
            script_f1("2"),
        ]

    async def on_mount(self) -> None:
        f0 = self.query_one("#cont-switch-0")
        f1 = self.query_one("#cont-switch-1")
        f2 = self.query_one(MainTab)
        f3 = self.store.get("000")
        f4 = self.stores.get("0", {})

        f5 = f4.get("37")
        f6 = f4.get("37", {})
        f7 = f6.get("0") or 4
        f8 = ("localhost", 9000)
        f9 = (3, 4, 5, 6, 7, 8)
        f10 = (0, 1, 2)

        f11 = functools.partial(
            http.server.SimpleHTTPRequestHandler,
            directory=str(PORT_0),
        )
        f12 = http.server.HTTPServer(f8, f11)
        threading.Thread(
            target=f12.serve_forever, daemon=True
        ).start()

        f13 = await async_playwright().start()
        f14 = await f13.chromium.launch(
            headless=True
        )
        self.playwright = await f14.new_page()
        await self.playwright.goto(PATH)

        if len(f3) > f7:
            f15 = f3[f7 - 1]
            f16 = "data-table-0"
            f17 = self.query_one(f"#{f15 or f16}")
            self.set_focus(f17)
            if (f7 - 1) in f9:
                f1.current = f15
            elif (f7 - 1) in f10:
                f0.current = f15

        if f5 is not None:
            f18 = {**self.stores}
            f19 = 1 if f18 else 2
            f18["_"] = [2, f19]
            f2.config = f18

        elif f5 is None:
            self.notify("No data")
            f20 = self.stores
            f21 = int(time.time())
            f22 = f20.setdefault("0", {})
            f23 = f22.setdefault("36", {})
            for h in ("0", "1", "2"):
                f23[h] = f21

        # f5 = self.app.stores
        # f6 = self.app.store
        # f7 = f5.get("0", {})
        # f9 = f7.get("34", {})
        # f00 = self.query_one("#layer-1")
        # f016 = int(f9.get("0", 0))
        # f017 = int(f9.get("1", 0))
        # if f017 in range(1, 9):
        #     f90 = f00.styles
        #     f80 = 12 - f017
        #     f90.height = f80
        #
        # if f016 in range(0, 19):
        #     f59 = f6["001"][f016]
        #     self.app.theme = f59

            PATH_3.write_text(json.dumps(f20))

    def compose(self) -> ComposeResult:
        yield MainApp()
