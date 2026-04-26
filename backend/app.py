# SPDX-License-Identifier: AGPL-3.0-or-later
# SPDX-FileCopyrightText: 2024 Andri Berger
#
# This file is part of layout-tui.
#
# layout-tui is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

from playwright.async_api import async_playwright
from textual.app import App, ComposeResult
from .containers import ContainerApp
from pathlib import Path
import http.server
import threading
import functools
import json


PORT = 9000
PATH_FILE = Path(__file__).parent
STATIC_DIR = PATH_FILE.parent / "frontend"
DIR = f"http://localhost:{PORT}/model.html"
CSS_PATHS = STATIC_DIR / "style.tcss"
CONFIG = STATIC_DIR / "build.json"


class CLIApp(App):

    COMMAND_PALETTE_DISPLAY = None
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

    def compose(self) -> ComposeResult:
            yield ContainerApp()

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
        headless=True,
        args=[
          "--disable-extensions",
          "--disable-gpu",
          "--no-sandbox",
          "--disable-dev-shm-usage",
        ]
        )
        self.page = await browser.new_page()
        await self.page.goto(DIR)

    async def on_unmount(self) -> None:
        if self._server:
            self._server.shutdown()
        if self._pw:
        # if self.page:
            await self._pw.stop()

# if __name__ == "__main__":
#     app = CLIApp().run()
