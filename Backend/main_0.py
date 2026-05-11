
from textual.widgets import (
    DataTable, Input, Button, ContentSwitcher, Digits, Label)
from textual.containers import Horizontal
from textual.app import ComposeResult
from textual.widget import Widget
from textual.events import Key
from itertools import cycle
from textual import on


from .helper import on_cell_highlighted_, on_key_
from .main_2 import FileTypeTree
from .main_1 import ImageTab
cursors = cycle(["cell"])



class NoSelectInput(Input):
    def on_focus(self):
        self.cursor_position = len(self.value)


class TableApp(Widget):
    def __init__(self) -> None:
        super().__init__()
        self._cursor = None
        self._visual_start = None
        self._visual_mode = False
        self._clipboard = None
        self._coord = None
        self.config = self.app.config["4-0"]
        self.full_IDs = self.app.config["7-0"]

    def on_mount(self) -> None:
        tables = self.query(DataTable)

        for i, table in enumerate(tables):
            lister = [9,100,600]
            listers = [28,22,18]
            rows = self.app.config[f"1-{i}"]
            table.cursor_type = next(cursors)
            table.zebra_stripes = True
            table.fixed_columns = 1
            table.fixed_rows = 0
            table.add_column("", width=listers[i])
            for _ in range(lister[i]):
                table.add_column("", width=6)
            table.add_rows(rows[1:])

    def compose(self) -> ComposeResult:
        with Horizontal(id="top"):
            yield ImageTab()
            yield Digits("F00", id="digits-0")

        with Horizontal(id="bottom"):
            with ContentSwitcher(
                    initial="dir-tree-0",
                    id="cont-switch-0"):
                yield FileTypeTree(
                    "/",file_type="json",id="dir-tree-0")
                yield FileTypeTree(
                    "/",file_type="image",id="dir-tree-1")
                yield FileTypeTree(
                    "/",file_type="font",id="dir-tree-2")

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

        with Horizontal(id="status"):
            yield Button("SA", id="button-0")
            yield Button("SB", id="button-1")
            yield Button("SC", id="button-2")
            yield Button("LABEL", id="button-5")
            yield Button("CLEAR", id="button-6")
            yield Button("Create", id="button-3")
            yield Button("Save", id="button-4")
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
        digits = self.query_one("#digits-0",Digits)
        cont = self.query_one("#cont-switch-0", ContentSwitcher)
        x_offset = cont.region.x - digits.region.x
        y_offset = cont.region.y - digits.region.y - 3
        digits.styles.offset = (x_offset, y_offset)

    def on_resize(self, event):
        digits = self.query_one("#digits-0",Digits)
        digits.styles.offset = (0, 0)
        self.call_after_refresh(
            self._position_digits)

    def action_next_table(self, event, prefix) -> None:
        testlauf = (self.full_IDs.index(self.app.focused.id) + prefix) % len(self.full_IDs)

        if testlauf in {1, 2, 4, 5}:
            event.stop()
            event.prevent_default()

        if testlauf < 6:
            switcher_id = "#cont-switch-1" if testlauf >= 3 else "#cont-switch-0"
            self.query_one(switcher_id, ContentSwitcher).current = self.full_IDs[testlauf]


    @on(DataTable.CellHighlighted)
    def on_cell_highlighted(self, event: DataTable.CellHighlighted) -> None:
        on_cell_highlighted_(self, event)

    @on(DataTable.CellSelected)
    async def on_cell_selected(self, event: DataTable.CellSelected) -> None:
        third = self.query_one("#third", Input)

        self._coord = event.coordinate
        third.disabled = False
        if event.value is not None:
            third.value = str(event.value)
        third.focus()

    @on(Input.Submitted)
    def on_input_submitted(self, event: Input.Submitted):
        switcher = self.query_one("#cont-switch-1", ContentSwitcher)
        tables = self.query_one(f"#{switcher.current}", DataTable)
        third = self.query_one("#third", Input)
        images = self.query_one(ImageTab)

        if self._coord is not None:
            tables.update_cell_at(self._coord, event.value)
            tst = self.get_all_data(tables)
            self.notify(f"TST: {tst}")
            images.config = tst
            third.value = ""
            self._coord = None
            tables.focus()

    @on(Button.Pressed)
    def on_button_pressed(self, event: Button.Pressed) -> None:
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


    @on(Key)
    async def on_key(self, event) -> None:
        await on_key_(self, event)


    # def key_c(self):
    #     switcher = self.query_one("#cont-switch-1", ContentSwitcher)
    #     table = self.query_one(f"#{switcher.current}", DataTable)
    #     table.cursor_type = next(cursors)