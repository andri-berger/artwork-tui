
from textual.widgets import (DataTable, Input, Button, ContentSwitcher, DirectoryTree, Digits)
from .data_img import ImageTab
from textual.containers import Horizontal
from textual.coordinate import Coordinate
from textual.app import ComposeResult
from textual.widget import Widget
from textual.events import Key
from itertools import cycle
import mimetypes
from textual import on
cursors = cycle(["cell"])



class NoSelectInput(Input):
    def on_focus(self):
        self.cursor_position = len(self.value)


class FileTypeTree(DirectoryTree):
    show_root = False
    def __init__(self, path, file_type: str, **kwargs):
        self.file_type = file_type
        super().__init__(path, **kwargs)

    def filter_paths(self, paths):
        return [p for p in paths if not p.name.startswith(".") and self._is_allowed(p)]

    def _is_allowed(self, p):
        if p.is_dir():
            return True  # always show dirs for navigation

        mime, _ = mimetypes.guess_type(p.name)
        category = mime.split("/")[0] if mime else None
        FONT_EXTENSIONS = {".otf", ".ttf", ".woff", ".woff2", ".eot"}

        match self.file_type:
            case "image":
                return category == "image"
            case "font":
                return p.suffix.lower() in FONT_EXTENSIONS
            case "json":
                return p.suffix.lower() == ".json"
        return False


# def filter_paths(self, paths):
#     allowed_mimes = {"font", "image"}
#     allowed_extensions = {".json"}
#
#     def is_allowed(p):
#         mime, _ = mimetypes.guess_type(p.name)
#         if mime:
#             category = mime.split("/")[0]  # "image", "font", "application"...
#             if category in allowed_mimes:
#                 return True
#         return p.suffix.lower() in allowed_extensions
#
#     return [p for p in paths and is_allowed(p)]

# class JDirectoryTree(DirectoryTree):
#     allowed_extensions = {".json"}
#     show_root = False
#     def filter_paths(self, paths):
#         return p.suffix.lower() in allowed_extensions]
#
# class PDirectoryTree(DirectoryTree):
#     show_root = False
#     def filter_paths(self, paths):
#         return [p for p in paths if not p.name.startswith(".")]
#
# class FDirectoryTree(DirectoryTree):
#     show_root = False
#     def filter_paths(self, paths):
#         return [p for p in paths if not p.name.startswith(".")]


class TableApp(Widget):
    def __init__(self) -> None:
        super().__init__()
        self._cursor = None
        self._visual_start = None
        self._visual_mode = False
        self._clipboard = None
        self._coord = None

    def on_mount(self) -> None:
        tables = self.query(DataTable)
        for i, table in enumerate(tables):
            rows = self.app.config[f"1-{i}"]
            table.cursor_type = next(cursors)
            table.zebra_stripes = True
            table.fixed_columns = 1
            table.fixed_rows = 0
            table.add_columns(*rows[0])
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
            yield Button("CREATE", id="button-3")
            yield Button("SAVE", id="button-4")
            yield Input(placeholder="Select 7", disabled=True, id="second")
            yield Input(id="third", disabled=True)

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

    @on(Input.Submitted)
    def on_input_submitted(self, event: Input.Submitted):
        switcher = self.query_one("#cont-switch-1", ContentSwitcher)
        tables = self.query_one(f"#{switcher.current}", DataTable)
        images = self.query_one(ImageTab)
        third = self.query_one("#third", Input)

        if self._coord is not None:
            tables.update_cell_at(self._coord, event.value)
            tst = self.get_all_data(tables)
            self.notify(f"TST: {tst}")
            images.config = tst
            third.value = ""
            self._coord = None
            tables.focus()


    @on(DataTable.CellHighlighted)
    def on_cell_highlighted(self, event: DataTable.CellHighlighted) -> None:
        digits = self.query_one("#digits-0",Digits)
        config = self.app.config["4-0"]
        row, col = event.coordinate
        try:
            test = config[row][col]
        except IndexError:
            digits.update("")
            return
        digits.update(str(test))

    @on(DataTable.CellSelected)
    async def on_cell_selected(self, event: DataTable.CellSelected) -> None:
        third = self.query_one("#third", Input)
        self._coord = event.coordinate
        third.disabled = False
        if event.value is not None:
            third.value = str(event.value)
        third.focus()


    def action_next_table(self, event, prefix) -> None:
        full_IDs = self.app.config["7-0"]
        testlauf = (full_IDs.index(self.app.focused.id) + prefix) % len(full_IDs)

        if testlauf in {1, 2, 4, 5}:
            event.stop()
            event.prevent_default()

        if testlauf < 6:
            switcher_id = "#cont-switch-1" if testlauf >= 3 else "#cont-switch-0"
            self.query_one(switcher_id, ContentSwitcher).current = full_IDs[testlauf]

    def action_prev_table(self) -> None:
        switcher = self.query_one("#cont-switch-1", ContentSwitcher)
        ids = [t.id for t in self.query(DataTable)]
        self.notify(f"ids: {ids}")
        switcher.current = ids[(ids.index(switcher.current) - 1) % len(ids)]



    @on(Key)
    async def on_key(self, event) -> None:
        editor = self.query_one("#third", Input)
        switcher = self.query_one("#cont-switch-1", ContentSwitcher)
        table = self.query_one(f"#{switcher.current}", DataTable)


        if event.key == "tab":
            self.action_next_table(event,1)

        elif event.key == "shift+tab":
            self.action_next_table(event,-1)


        if isinstance(self.app.focused, DataTable):
            cursor_coord = table.cursor_coordinate

            if len(event.key) == 1 and event.key.isprintable():
                current_value = table.get_cell_at(cursor_coord)

                if len(event.key) == 1 and event.key.isprintable():
                    editor.value = event.key
                    editor.cursor_position = len(event.key)
                    self.notify("yes")
                else:
                    self.notify("no")
                    editor.value = str(current_value)

                self._coord = cursor_coord
                editor.focus()
                event.stop()

                def after_focus():
                    editor.cursor_position = len(editor.value)
                self.call_after_refresh(after_focus)

        if isinstance(self.app.focused, Input):
            if event.key == "escape":
                self._coord = None
                editor.value = ""
                table.focus()

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
        switcher = self.query_one("#cont-switch-1", ContentSwitcher)
        table = self.query_one(f"#{switcher.current}", DataTable)
        table.cursor_type = next(cursors)