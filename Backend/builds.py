from .models import (
    on_cell_highlighted_,
    on_key_, on_pressed,
    on_submitted)
from textual.widgets import (
    DataTable, Input, Button,
    ContentSwitcher, Digits, Label)

from .model import FileTypeTree, ImageTab
from textual.containers import Horizontal
from textual.app import ComposeResult
from textual.widget import Widget
from textual.events import Key
from textual import events, on
from itertools import cycle
cursors = cycle(["cell"])


class NoSelectInput(Input):
    def on_focus(self):
        self.cursor_position = len(self.value)

class TableApp(Widget):
    def __init__(self) -> None:
        super().__init__()
        self.coord = None
        self._cursor = None
        self._clipboard = None
        self._visual_start = None
        self._visual_mode = False
        self.full_IDs = self.app.store["4-0"]
        self.turi = ['activated', 'deactivated']
        self.turis = ['visible', 'hidden']
        self.lister = [9, 100, 301, 300, 6, 6]
        self.listers = [28, 22, 18, 18, 14, 14]
        self.check_only = [8,7,7,7,7,7]
        self.check_only0 = [7,7,7,7,7,62]

    def on_mount(self) -> None:
        self.f_left = self.query_one("#cont-switch-0", ContentSwitcher)
        self.c_cont = self.query_one("#cont-switch-0", ContentSwitcher)
        self.f_right = self.query_one("#cont-switch-1", ContentSwitcher)
        self.d_digits = self.query_one("#digits-0",Digits)
        self.c_digits = self.query_one("#digits-0",Digits)
        self.e_fourth = self.query_one("#fourth", Input)
        self.e_third = self.query_one("#third", Input)
        self.label = self.query_one("#label-0", Label)
        self.e_images = self.query_one(ImageTab)
        a_tables = self.query(DataTable)

        for i, table in enumerate(a_tables):
            i0 = '2' if i == 3 else i
            rows = self.app.store[f"1-{i0}"]
            checks = self.check_only[i]
            table.cursor_type = "cell"
            table.zebra_stripes = True
            table.fixed_columns = 1
            table.fixed_rows = 0
            table.add_column(
                "", width=self.listers[i])
            for _ in range(self.lister[i]):
                if i <= 3:
                    table.add_column(
                        "",
                        width=checks)
                elif i >= 4:
                    checks0 = self.check_only0[_]
                    table.add_column(
                        "",
                        width=checks0)
            table.add_rows(rows[0:])

    def compose(self) -> ComposeResult:
        with Horizontal(id="top"):
            yield ImageTab(name="")
            yield Digits("F00",
                         id="digits-0")

        with Horizontal(id="bottom"):
            with ContentSwitcher(
                    initial="dir-tree-0",
                    id="cont-switch-0"):
                yield FileTypeTree(
                    "/",
                    file_type="json",
                    id="dir-tree-0")
                yield FileTypeTree(
                    "/",
                    file_type="image",
                    id="dir-tree-1")
                yield FileTypeTree(
                    "/",
                    file_type="font",
                    id="dir-tree-2")

            with ContentSwitcher(
                    initial="data-table-0",
                    id="cont-switch-1"):
                yield DataTable(
                    show_header=False,
                    id="data-table-0")
                yield DataTable(
                    show_header=False,
                    id="data-table-1")
                yield DataTable(
                    show_header=False,
                    id="data-table-2")
                yield DataTable(
                    show_header=False,
                    id="data-table-3")
                yield DataTable(
                    show_header=False,
                    id="data-table-4")
                yield DataTable(
                    show_header=False,
                    id="data-table-5")

        with Horizontal(id="status"):
            yield Button("X", id="button-6")
            yield Button("AS", id="button-0")
            yield Button("BS", id="button-1")
            yield Button("CS", id="button-2")
            yield Button("CREATE", id="button-3")
            yield Button("EXPORT", id="button-4")
            yield Input(id="fourth", disabled=False)
            yield Input(id="third", disabled=False)

        with Horizontal(id="bottoms"):
            yield Label(id="label-0")

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

    def _position_digits(self):
        x_offset = self.c_cont.region.x - self.c_digits.region.x
        y_offset = self.c_cont.region.y - self.c_digits.region.y - 3
        self.c_digits.styles.offset = (x_offset, y_offset)

    @on(DataTable.CellHighlighted)
    def highlighted(self, event: DataTable.CellHighlighted) -> None:
        on_cell_highlighted_(self, event.coordinate)

    @on(DataTable.CellSelected)
    async def selected(self, event: DataTable.CellSelected) -> None:
        self.coord = event.coordinate
        if event.value is not None:
            self.e_third.value = str(event.value)
        self.e_third.focus()

    @on(Input.Submitted)
    def submitted(self, event: Input.Submitted) -> None:
        on_submitted(self,event)

    @on(Button.Pressed)
    def pressed(self, event: Button.Pressed) -> None:
        on_pressed(self, event)

    @on(events.Resize)
    def on_resize(self, event: events.Resize) -> None:
        self.d_digits.styles.offset = (0, 0)
        self.call_after_refresh(
            self._position_digits)

    @on(Key)
    async def key(self, event) -> None:
        await on_key_(self, event)
