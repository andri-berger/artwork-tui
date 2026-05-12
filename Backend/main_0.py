
from textual.widgets import (
    DataTable, Input, Button, ContentSwitcher, Digits, Label)
from textual.containers import Horizontal
from textual.app import ComposeResult
from textual.widget import Widget
from textual.events import Key
from itertools import cycle
from textual import on
from textual import events

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
        lister = [9, 100, 600]
        listers = [28, 22, 18]

        for i, table in enumerate(a_tables):
            rows = self.app.config[f"1-{i}"]
            table.cursor_type = "cell"
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
        x_offset = self.c_cont.region.x - self.c_digits.region.x
        y_offset = self.c_cont.region.y - self.c_digits.region.y - 3
        self.c_digits.styles.offset = (x_offset, y_offset)

    @on(DataTable.CellHighlighted)
    def highlighted(self, event: DataTable.CellHighlighted) -> None:
        on_cell_highlighted_(self, event.coordinate)

    @on(DataTable.CellSelected)
    async def selected(self, event: DataTable.CellSelected) -> None:
        self._coord = event.coordinate
        if event.value is not None:
            self.e_third.value = str(event.value)
        self.e_third.focus()

    @on(Input.Submitted)
    def submitted(self, event: Input.Submitted) -> None:
        if self._coord is not None:
            e_tables = self.query_one(
                f"#{self.f_right.current}", DataTable)
            e_tables.update_cell_at(self._coord, event.value)
            switches = self.f_right.current.split("-")[-1]
            tst = self.get_all_data(e_tables)
            self.app.configs[switches] = tst
            self.notify(f"{self.app.configs}")
            self.e_images.config = self.app.configs
            self.e_images.mutate_reactive(
                ImageTab.config)
            self.e_third.value = ""
            self._coord = None
            e_tables.focus()

    @on(Button.Pressed)
    def pressed(self, event: Button.Pressed) -> None:
        id = event.button.id
        if id == "button-0":
            pass
        elif id == "button-1":
            pass
        elif id == "button-2":
            pass
        if id == "button-5":
            pass
        elif id == "button-6":
            pass
        elif id == "button-3":
            pass
        elif id == "button-4":
            pass

    @on(events.Resize)
    def on_resize(self, event: events.Resize) -> None:
        self.d_digits.styles.offset = (0, 0)
        self.call_after_refresh(
            self._position_digits)

    @on(Key)
    async def key(self, event) -> None:
        await on_key_(self, event)
