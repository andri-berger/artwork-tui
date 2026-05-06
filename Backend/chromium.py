
async def on_mount(self) -> None:
    # show TUI immediately
    self.run_worker(self._init_browser(), exclusive=True)

async def _init_browser(self) -> None:
    self._pw = await async_playwright().start()
    browser = await self._pw.chromium.launch(headless=True)
    self.page = await browser.new_page()
    await self.page.goto(f"http://localhost:{PORT}/model.html",wait_until="commit")
    # only NOW is canvas ready

