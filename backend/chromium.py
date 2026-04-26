# SPDX-License-Identifier: AGPL-3.0-or-later
# SPDX-FileCopyrightText: 2024 Andri Berger
#
# This file is part of layout-tui.
#
# layout-tui is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

async def on_mount(self) -> None:
    # show TUI immediately
    self.run_worker(self._init_browser(), exclusive=True)

async def _init_browser(self) -> None:
    self._pw = await async_playwright().start()
    browser = await self._pw.chromium.launch(headless=True)
    self.page = await browser.new_page()
    await self.page.goto(f"http://localhost:{PORT}/model.html",wait_until="commit")
    # only NOW is canvas ready

