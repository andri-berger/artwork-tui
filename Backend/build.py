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
        f0["2-5"] = script_f3()
        f0["2-4"] = script_f2()
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
        f2 = self.query_one("#layer-1")
        f3 = self.query_one(MainTab)
        f4 = self.store.get("000")
        f5 = self.store.get("001")
        f6 = self.stores.get("1")
        f7 = self.stores.get(
            "0", {})

        f9 = f7.get("36")
        f10 = f7.get("37", {})
        f11 = f7.get("34", {})
        f12 = f11.get("1", 0)
        f13 = f11.get("0", 0)
        f14 = f10.get("0") or 4
        f15 = ("localhost", 9000)
        f16 = (3, 4, 5, 6, 7, 8)
        f17 = (0, 1, 2)

        f18 = functools.partial(
            http.server.SimpleHTTPRequestHandler,
            directory=str(PORT_0),
        )
        f19 = http.server.HTTPServer(f15, f18)
        threading.Thread(
            target=f19.serve_forever, daemon=True
        ).start()

        f20 = await async_playwright().start()
        f21 = await f20.chromium.launch(
            headless=True
        )
        self.playwright = await f21.new_page()
        await self.playwright.goto(PATH)
        f22 = self.stores

        if len(f4) > f14:
            f23 = f4[f14 - 1]
            f24 = "data-table-0"
            f25 = f"#{f23 or f24}"
            f26 = self.query_one(f25)
            self.set_focus(f26)
            if (f14 - 1) in f16:
                f1.current = f23
            elif (f14 - 1) in f17:
                f0.current = f23

        if f6 is not None:
            f27 = {**f22}
            f27["_"] = [2, 1]
            f3.config = f27

        if f6 is None:
            f28 = int(f13)
            f29 = int(f12)
            if f29 in range(1, 9):
                f30 = f2.styles
                f31 = 12 - f29
                f30.height = f31

            if f28 in range(0, 19):
                self.app.theme = f5[f28]

        if f9 is None:
            f32 = int(time.time())
            f33 = f22.setdefault("0", {})
            f34 = f33.setdefault("36", {})
            for h in ("0", "1", "2"):
                f34[h] = f32

            PATH_3.write_text(json.dumps(f22))

    def compose(self) -> ComposeResult:
        yield MainApp()
