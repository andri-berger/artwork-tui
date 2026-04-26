# SPDX-License-Identifier: AGPL-3.0-or-later
# SPDX-FileCopyrightText: 2024 Andri Berger
#
# This file is part of layout-tui.
#
# layout-tui is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

from textual.containers import VerticalScroll, HorizontalScroll, ScrollableContainer
from textual.containers import Horizontal
from textual.app import ComposeResult
from textual.widget import Widget
from textual.widgets import Placeholder
from .table import TableApp
from .imageTab import ImageTab

# def copy_user_files(files: list[str]):
#     UPLOADS_DIR.mkdir(parents=True, exist_ok=True)
#     for f in files:
#         src = pathlib.Path(f).expanduser().resolve()
#         shutil.copy(src, UPLOADS_DIR / src.name)

class Box(Placeholder):
    """Example widget."""

    DEFAULT_CSS = """
    Box {
        width: 3;
        height: 8;        
    }
    """

class ContainerApp(Widget):


    DEFAULT_CSS = """                                                                                      
    TableApp {
        height: 1fr;                                                                                       
    }               
    """

    def __init__(self):
        super().__init__()

    def compose(self) -> ComposeResult:
        with Horizontal():
            yield TableApp()

    # async def on_mount(self):
    #     asyncio.create_task(self._start_browser())
    #
    # async def _start_browser(self):
    #     self.pw = await async_playwright().start()
    #     browser = await self.pw.chromium.launch()
    #     self.page = await browser.new_page()
    #     await self.page.goto(self.link)

    # async def capture(self):
    #     start = time.time()
    #     data_url = await self.page.evaluate(self.setup, self.config)
    #     b64 = data_url.split(',')[1]
    #     img_bytes = base64.b64decode(b64)
    #     identity = time.time() - start
    #     with open(f"outputs-{identity:.3f}.png", "wb") as f:
    #         f.write(img_bytes)
    #     self.query_one(ImageApp).image_path = f"outputs-{identity:.3f}.png"


