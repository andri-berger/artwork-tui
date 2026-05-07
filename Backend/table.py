
from textual.widgets import (DataTable, Input, Label, Button, ContentSwitcher, Digits, LoadingIndicator)
from .data_img import ImageTab
from .directory_tree import TDirectoryTree
from textual.containers import Horizontal
from textual.coordinate import Coordinate
from textual.screen import ModalScreen
from textual.app import ComposeResult
from textual.widget import Widget


from itertools import cycle
from textual import on
cursors = cycle(["cell"])


class CellEditModal(ModalScreen[str]):
    def __init__(self, value: str):
        super().__init__()
        self._value = value

    def compose(self) -> ComposeResult:
        yield Label("Edit value")
        yield Input(value=self._value, id="editor")

    def on_input_submitted(self, event: Input.Submitted) -> None:
        self.dismiss(event.value)  # return new value to caller

    def on_key(self, event) -> None:
        if event.key == "escape":
            self.dismiss(None)  # cancel — return None

class TableApp(Widget):

    def __init__(self) -> None:
        super().__init__()
        self._cursor = None
        self._visual_start = None
        self._visual_mode = False
        self._clipboard = None

    def compose(self) -> ComposeResult:
        with Horizontal(id="top"):
            yield ImageTab()
        with Horizontal(id="bottom"):

            with ContentSwitcher(
                    initial="dir-tree-0",
                    id="cont-switch-0"):
                yield TDirectoryTree(
                    "/",id="dir-tree-0")
                yield TDirectoryTree(
                    "/",id="dir-tree-1")

            with ContentSwitcher(
                    initial="data-table-0",
                    id="cont-switch-1"):
                yield DataTable(
                    id="data-table-0")
                yield DataTable(
                    id="data-table-1")
                yield DataTable(
                    id="data-table-2")

        with Horizontal(id="status"):
            yield Digits("F00", id="digits-0")
            yield Button("Tab0", id="button-0")
            yield Button("Tab1", id="button-1")
            yield Button("Tab2", id="button-2")
            yield Input(placeholder="Select 7", disabled=True, id="second")
            yield Input(placeholder="No Default", id="third")


    @on(Button.Pressed)
    def button_pressed(self, event: Button.Pressed) -> None:
        left = self.query_one("#cont-switch-0", ContentSwitcher)
        right = self.query_one("#cont-switch-1", ContentSwitcher)
        if event.button.id == "button-0":
            right.current = "data-table-0"
            left.current = "dir-tree-0"
        elif event.button.id == "button-1":
            right.current = "data-table-1"
            left.current = "dir-tree-1"
        elif event.button.id == "button-2":
            right.current = "data-table-2"
            left.current = "dir-tree-1"
        right.query_one(
            f"#{right.current}").focus()



    def on_mount(self) -> None:
        rows0 = self.app.config['00-0']
        rows1 = self.app.config['00-1']
        rows2 = self.app.config['00-2']
        table0 = self.query_one("#data-table-0", DataTable)
        table1 = self.query_one("#data-table-1", DataTable)
        table2 = self.query_one("#data-table-2", DataTable)

        for table in self.query(DataTable):
            table.cursor_type = next(cursors)
            table.zebra_stripes = True
            table.fixed_columns = 1
            table.fixed_rows = 0

        table0.add_columns(*rows0[0])
        table1.add_columns(*rows1[0])
        table2.add_columns(*rows2[0])
        table0.add_rows(rows0[1:])
        table1.add_rows(rows1[1:])
        table2.add_rows(rows2[1:])


    def get_all_data(self, table: DataTable):
        skip_rows = 0
        skip_cols = 1

        def coerce(v):
            if not isinstance(v, str):  # only convert actual strings
                return v
            for cast in (int, float):
                try:
                    return cast(v)
                except (ValueError, TypeError):
                    pass
            return v

        return {
            str(row_i): d
            for row_i, r in enumerate(range(skip_rows, len(table.rows)))
            if (d := {
                str(i): coerce(v)
                for i, v in enumerate(table.get_row_at(r)[skip_cols:])
                if v is not None and v != ''
            })
        }

    def set_all_data(self):
        table = self.query_one(DataTable)
        images = self.query_one(ImageTab)
        tst = self.get_all_data(table)
        self.notify(f"TST: {tst}")
        images.config = tst

    @on(DataTable.CellHighlighted)
    def track_cursor(self, event: DataTable.CellHighlighted) -> None:
        self._cursor = event.coordinate

    @on(DataTable.CellSelected)
    async def on_cell_selected(self, event: DataTable.CellSelected) -> None:
        coord = event.coordinate

        def apply(new_value: str | None) -> None:
            if new_value is not None:
                self.query_one(DataTable).update_cell_at(coord, new_value)
                self.set_all_data()
        await self.app.push_screen(CellEditModal(str(event.value)), apply)

    async def on_key(self, event) -> None:
        table = self.query_one(DataTable)

        if event.key == "v":  # enter/exit visual mode
            self._visual_mode = not self._visual_mode
            self._visual_start = self._cursor if self._visual_mode else None
            self.notify("VISUAL" if self._visual_mode else "NORMAL")

        elif event.key == "y":
            if self._visual_mode and self._visual_start:  # yank rectangle
                r1 = min(self._visual_start.row, self._cursor.row)
                r2 = max(self._visual_start.row, self._cursor.row)
                c1 = min(self._visual_start.column, self._cursor.column)
                c2 = max(self._visual_start.column, self._cursor.column)

                self._clipboard = [
                    [table.get_cell_at(Coordinate(r, c)) for c in range(c1, c2 + 1)]
                    for r in range(r1, r2 + 1)
                ]
                self._visual_mode = False
                self._visual_start = None
                self.notify(f"Yanked {r2 - r1 + 1}×{c2 - c1 + 1}")

            else:          # yank
                self._clipboard = table.get_cell_at(self._cursor)
                self.notify(f"Copied: {self._clipboard}")  # toast confirmation

        elif event.key == "p" and self._clipboard is not None:  # paste
            if isinstance(self._clipboard, list):
                for ri, row in enumerate(self._clipboard):
                    for ci, val in enumerate(row):
                        try:
                            table.update_cell_at(
                                Coordinate(self._cursor.row + ri, self._cursor.column + ci),
                                val
                            )
                        except Exception:
                            pass  # silently skip out-of-bounds
                self.notify(f"Pasted {len(self._clipboard)}×{len(self._clipboard[0])}")

            else:
                table.update_cell_at(self._cursor, self._clipboard)

    def key_c(self):
        table = self.query_one(DataTable)
        table.cursor_type = next(cursors)