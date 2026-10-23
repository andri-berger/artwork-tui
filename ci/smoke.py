# Headless smoke test of an installed
# artwork-tui: start, CREATE, EXPORT. Run it
# with the installed env's Python.
import asyncio
import sys
import time

from artwork.Backend.build import CLIApp
from artwork.Backend.script import script_f00


async def wait_for(check, timeout=90):
    end = time.monotonic() + timeout
    while time.monotonic() < end:
        if check():
            return True
        await asyncio.sleep(1)
    return False


async def main() -> int:
    data = script_f00()
    before = set(data.glob("*.png"))
    app = CLIApp()
    async with app.run_test(
        size=(160, 48)
    ) as pilot:
        await pilot.pause(5)
        await pilot.click("#button-4")
        ok = await wait_for(
            lambda: (
                (data / "1700000000.png").exists()
                or app._exception
            )
        )
        if not ok or app._exception:
            print(
                "CREATE failed:", app._exception
            )
            return 1
        await pilot.click("#button-5")
        ok = await wait_for(
            lambda: (
                set(data.glob("*.png"))
                - before
                - {data / "1700000000.png"}
                or app._exception
            )
        )
        errors = [
            n.message
            for n in app._notifications
            if n.severity == "error"
        ]
        if not ok or app._exception or errors:
            print(
                "EXPORT failed:",
                app._exception,
                errors,
            )
            return 1
    print("smoke ok")
    return 0


sys.exit(asyncio.run(main()))
