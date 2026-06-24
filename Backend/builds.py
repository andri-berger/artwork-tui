from .models import (
    on_highlighted,
    on_key, on_pressed,
    on_submitted, on_shift_tab)
from textual.widgets import (
    DataTable, Input,
    Button, DirectoryTree,
    ContentSwitcher, Digits, Label)
from .model import FileTree, MainTab
from textual.containers import Horizontal
from textual.app import ComposeResult
from textual.widget import Widget
from textual import events, on

class MainApp(Widget):
    def __init__(self) -> None:
        super().__init__()

    def on_mount(self) -> None:
        f4 = [8,8,8,8,8,8,8,8,8,8,8,30,60]
        f1 = [9,100,301,300,12,13]
        f2 = [28,22,18,18,14,14]
        f3 = [8,8,8,7,7,7]
        f5 = self.app.store
        f0 = self.query(
            DataTable)

        for h, h0 in enumerate(f0):
            f6 = '2' if h == 3 else h
            f7 = f5[f"1-{f6}"]
            h0.cursor_type = "cell"
            h0.zebra_stripes = True
            h0.fixed_columns = 1
            h0.fixed_rows = 0
            h0.add_column(
                "", width=f2[h])
            for _ in range(f1[h]):
                if h <= 3:
                    h0.add_column(
                        "",
                        width=f3[h])
                elif h >= 4:
                    checks0 = f4[_]
                    h0.add_column(
                        "",
                        width=checks0)
            h0.add_rows(f7[0:])

    def compose(self) -> ComposeResult:
        with Horizontal(id="layer-0"):
            yield MainTab(name="")
            yield Digits("A00",
                         id="digits-0")

        with Horizontal(id="layer-1"):
            with ContentSwitcher(
                    id="cont-switch-0",
                    initial="dir-tree-0"):
                yield FileTree(
                    "/",
                    file_type=".json",
                    id="dir-tree-0")
                yield FileTree(
                    "/",
                    file_type=".png",
                    id="dir-tree-1")
                yield FileTree(
                    "/",
                    file_type=".otf",
                    id="dir-tree-2")

            with ContentSwitcher(
                    id="cont-switch-1",
                    initial="data-table-0"):
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

        with Horizontal(id="layer-2"):
            yield Button("X", id="button-0")
            yield Button("AS", id="button-1")
            yield Button("BSS", id="button-2")
            yield Button("CSS", id="button-3")
            yield Button("CREATE", id="button-4")
            yield Button("EXPORT", id="button-5")
            yield Input(disabled=False, id="input-0")
            yield Input(disabled=False, id="input-1")

        with Horizontal(id="layer-3"):
            yield Label(id="label-0")

    def get_data(self, h0) -> dict:
        f0 = self.app.horizontal
        f1 = self.app.vertical

        def data(v) -> int | float | str:
            if not isinstance(v, str):
                return v
            for cast in (int, float):
                try:
                    return cast(v)
                except (ValueError,
                        TypeError):
                    pass
            return v

        return {
            str(row_i): d
            for row_i, r in enumerate(
                range(f0, len(h0.rows)))
            if (d := {
                str(i): data(v)
                for i, v in enumerate(
                    h0.get_row_at(r)[f1:])
                if v is not None and v != ''})}

    def position_digits(self) -> None:
        f0 = self.query_one("#cont-switch-0")
        f1 = self.query_one("#digits-0")
        f2 = f0.region.x - f1.region.x
        f3 = f0.region.y - f1.region.y
        f1.styles.offset = (f2, f3 - 3)

    @on(DataTable.CellHighlighted)
    def highlighted(self, event: DataTable.CellHighlighted):
        on_highlighted(self, event.coordinate)

    @on(Input.Submitted)
    def submitted(self, event: Input.Submitted):
        on_submitted(self,event)

    @on(Button.Pressed)
    def pressed(self, event: Button.Pressed):
        on_pressed(self, event)

    @on(events.Key)
    async def key(self, event: events.Key):
        await on_key(self, event)

    @on(events.Resize)
    def resized(self):
        f0 = self.query_one(
            "#digits-0")
        f0.styles.offset = (0, 0)
        self.call_after_refresh(
            self.position_digits)

    @on(events.Click)
    def clicked(self):
        f0 = self.app
        f1 = f0.focused
        f2 = f0.textfields
        f3 = DirectoryTree
        f4 = DataTable
        if f2 is not None:
            f0.textfields.stop()
            f0.textfields = None
        f5 = isinstance(f1, f3)
        f6 = isinstance(f1, f4)
        if f5 or f6:
            on_shift_tab(self,
                     None,
                     0)
