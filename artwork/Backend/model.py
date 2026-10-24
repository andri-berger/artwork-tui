import asyncio
import base64
import json
import time

from textual import on
from textual.app import ComposeResult
from textual.binding import Binding
from textual.coordinate import Coordinate
from textual.reactive import reactive
from textual.widget import Widget
from textual.widgets import (
    DataTable,
    DirectoryTree,
)
from textual_image.widget import Image

from .script import (
    script_f00,
    script_f01,
    script_f6,
    script_f7,
    script_f9,
    script_f10,
    script_f12,
    script_f13,
    script_f15,
    script_f17,
)
from .scripts import scripts_f1

PORT_0 = script_f01()
PORT_1 = script_f00()
PORT_2 = PORT_0 / "module"
PORT_3 = PORT_0 / "modules"
PATH_3 = PORT_0 / "model.png"
PATH_4 = PORT_1 / "1700000000.png"
PATH_5 = PORT_1 / "1700000000.json"
PATH = "async (store) => window.h11(store)"


class MainTab(Widget):
    config: reactive[dict] = reactive(
        dict, init=False
    )

    def compose(self) -> ComposeResult:
        # A saved layout renders on startup:
        # no fallback image before it
        if self.app.stores.get("1") is None:
            yield Image(PATH_3)

    def on_mount(self) -> None:
        for f0 in self.query(Image):
            f0.styles.width = "auto"
            f0.styles.height = "100%"
        self.rows = {}

    async def watch_config(
        self, path: dict
    ) -> None:
        f0 = self.app.query_one("#cont-switch-1")
        f00 = self.app.query_one("#layer-1")
        f2 = [6, 100, 301, 300, 12, 13]
        f3 = self.app.query(DataTable)
        f4 = self.app.playwright
        f6 = self.app.store
        f7 = self.size

        f12, f13, *f47 = path.pop("_", [])
        # Load/clear: path is the new state, so
        # a render queued before it can't undo it
        if f12 == 2:
            self.app.stores = path
        f5 = self.app.stores

        f8 = f5.get("0", {})
        f9 = f8.get("30", {})
        f10 = f8.get("34", {})
        f11 = f8.get("37", {})

        f14 = script_f9(path, f6)
        try:
            f15 = await f4.evaluate(
                PATH, [f13, f14]
            )
        except Exception as e:
            self.notify(
                str(e).splitlines()[0],
                title="Render failed",
                severity="error",
            )
            if f12 == 1:
                self.show_rows()
            # Startup render failed: fallback
            if f12 == 2 and not self.query(Image):
                f47 = Image(PATH_3)
                f47.styles.width = "auto"
                f47.styles.height = "100%"
                await self.mount(f47)
            return
        # Rendered: drop the CREATE row snapshot
        self.rows = {}
        f16 = f15[0].split(",")[1]
        f17 = base64.b64decode(f16)
        f18 = script_f15(f10.get("1"))
        f19 = script_f15(f10.get("0"))
        f20 = script_f15(f9.get("0"))

        if f20 in range(1, 5):
            f21 = {
                "h": f20,
                "h0": script_f15(
                    f9.get("1"), float
                ),
                "h1": script_f15(
                    f9.get("2"), float
                ),
            }
            f17 = await asyncio.to_thread(
                scripts_f1, f21, f17
            )

        if f13 == 4:
            f22 = int(time.time())
            f22 = f47[0] if f47 else f22
            f23 = PORT_1 / f"{f22}.png"
            with open(f23, "wb") as f:
                f.write(f17)

        if f13 <= 3:
            self.query(Image).remove()
            with open(PATH_4, "wb") as f:
                f.write(f17)
            f24 = Image(PATH_4)
            script_f7(f7, f10, f24, f17)
            # Not query_one: its cache keeps each
            # removed preview and its pixels alive
            await self.mount(f24)

            if f10.get("3") == "true":
                f26 = f24.styles
                f26.width = "100%"
                f26.height = "auto"

        if f13 == 2:
            f27 = script_f10(f15[1], f6)
            f5 = {**f5, **f27}
            self.app.stores = f5

        if f12 >= 1:
            f29 = f12 == 2
            f32 = (0, 6) if f29 else (1, 4)
            with self.app.batch_update():
                for h0 in range(*f32):
                    f35 = 2 if h0 == 3 else h0
                    f36 = f6.get(f"1-{f35}")
                    f37 = f5.get(str(h0), {})
                    if f37 is not None:
                        f51 = []
                        f38 = [
                            str(h1)
                            for h1 in range(
                                f2[h0]
                            )
                        ]
                        for h2 in range(len(f36)):
                            f39 = f37.get(str(h2))
                            f40 = [f36[h2][0]]
                            if f39 is not None:
                                for h3 in f38:
                                    f40.append(
                                        str(
                                            f39.get(
                                                h3,
                                                "",
                                            )
                                        )
                                    )
                            f51.append(f40)
                        self.set_rows(f3[h0], f51)

                # Load/X: back to the saved table
                # ("37"/"0" = 4 + table) and cell;
                # CREATE: set_rows keeps cursors
                f41 = script_f15(f11.get("1"))
                f42 = script_f15(f11.get("2"))
                f49 = script_f15(f11.get("0")) - 4
                if f12 == 2 and f49 in range(6):
                    f0.current = (
                        f"data-table-{f49}"
                    )
                    f3[f49].move_cursor(
                        row=f41, column=f42
                    )

        # Unset or out of range: defaults
        f43 = f18 in range(1, 10)
        f44 = f6["001"]
        f45 = f19 in range(len(f44))
        f00.styles.height = (
            12 - f18 if f43 else None
        )
        self.app.theme = f44[f19 if f45 else 0]

        PATH_5.write_text(json.dumps(f5))

        # CREATE/EXPORT done: confirm now, so
        # the toast doesn't sit out the render
        if f13 in (2, 4):
            f52 = f"button-{f13 // 2 + 3}"
            f53 = self.app.query_one(f"#{f52}")
            f54 = str(f53.label)
            script_f6(self.app, f52, "", f54)

    def hide_rows(self) -> None:
        # Blank tables 1-3 until CREATE
        # returns; keep rows for show_rows
        f0 = self.app.query(DataTable)
        self.rows = {}
        for h in range(1, 4):
            f1 = f0[h]
            f2 = [
                f1.get_row_at(h0)
                for h0 in range(f1.row_count)
            ]
            self.rows[h] = f2
            self.set_rows(
                f1, [[h1[0]] for h1 in f2]
            )

    def show_rows(self) -> None:
        f0 = self.app.query(DataTable)
        for h, h0 in self.rows.items():
            self.set_rows(f0[h], h0)

    def set_rows(self, h, h0) -> None:
        # Write only the changed cells: a new row
        # makes DataTable measure every cell (300
        # columns), though the widths are fixed.
        # Cursor and scroll stay where they are
        f0 = len(h.columns)
        if h.row_count != len(h0):
            f3 = h.cursor_coordinate
            h.clear(columns=False)
            h.add_rows(h0)
            h.move_cursor(
                row=f3.row, column=f3.column
            )
            return
        for h1, h2 in enumerate(h0):
            f1 = h.get_row_at(h1)
            f2 = [*h2, *[None] * (f0 - len(h2))]
            for h3, h4 in enumerate(f2):
                if f1[h3] != h4:
                    h.update_cell_at(
                        Coordinate(h1, h3), h4
                    )

    def render(self):
        return ""


class FileTree(DirectoryTree):
    show_root = False
    show_guides = True
    guide_depth = 4
    BINDINGS = [
        Binding(
            "space", "select_cursor", "Select"
        )
    ]

    def __init__(
        self, path, file_type, **kwargs
    ) -> None:
        super().__init__(path, **kwargs)
        self.file_type = file_type

    def filter_paths(self, path) -> list:
        f0 = self.file_type
        return [
            h
            for h in path
            if (
                h.is_dir()
                or h.suffix.lower() in f0
            )
            and not h.name.startswith(".")
        ]

    @on(DirectoryTree.FileSelected)
    def selected(
        self, event: DirectoryTree.FileSelected
    ) -> None:
        f0 = self.app.query_one("#cont-switch-1")
        f1 = self.app.query_one(f"#{f0.current}")
        f2 = self.app.query_one(MainTab)
        f3 = f0.current.split("-")[-1]
        f4 = f1.cursor_coordinate
        f5 = event.control.id
        f6 = self.app.stores
        f7 = f5.split("-")[-1]
        f8 = ["4", "5"][int(f7) - 1]
        f11 = event.path
        f12 = f11.name
        script_f6(self.app, f5, f12)

        if int(f7) >= 1:
            f13 = f4.column
            f14 = str(f4.row)
            f15 = int(f7) - 1
            f16 = script_f13(f11, f15)

            # Column 12 of the tree's own table
            # (images: 4, fonts: 5), else base
            if f3 == f8 and f13 == 12:
                f20 = f6.setdefault(f8, {})
                f21 = f20.setdefault(f14, {})
                f22 = f21.get("11")
                f21["11"] = f16
                f1.update_cell_at(f4, f16)

            else:
                f25 = f6.setdefault("0", {})
                f26 = f25.setdefault("37", {})
                f22 = f26.get(str(f15 + 3))
                f26[str(f15 + 3)] = f16

            script_f12(f11, f15, f6, f22)
            f27 = {**self.app.stores}
            f27.update({"_": [0, 1]})
            f2.config = f27

        elif int(f7) == 0:
            # script_f9 checks the layout of
            # every value against build.json
            try:
                f29 = json.loads(f11.read_text())
                script_f9(f29, self.app.store)
            except Exception as e:
                self.notify(
                    f"{f12}: {e!r}",
                    title="Invalid project file",
                    severity="error",
                )
                return
            f30 = script_f17(f29)
            if f30:
                self.notify(
                    ", ".join(f30),
                    title="Missing assets",
                    severity="warning",
                )
            f29.update({"_": [2, 1]})
            self.app.stores = f29
            f2.config = f29
