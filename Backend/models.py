from textual.widgets import (
    DataTable, Input, ContentSwitcher, Digits, Button, Label)
from textual.coordinate import Coordinate
from Backend.model import FileTypeTree
from pathlib import Path
import json



PATH_FILE = Path(__file__).parent
STATIC_DIR = PATH_FILE.parent / "Fontend"
CONFIGS = STATIC_DIR / "model.json"


def action_next_table(self, event, prefix) -> None:
    sw = self.query_one("#cont-switch-0", ContentSwitcher)
    st = self.query_one("#cont-switch-1", ContentSwitcher)
    l1 = self.full_IDs.index(self.app.focused.id)
    testlauf = (l1 + prefix) % len(self.full_IDs)
    arr = self.app.store["4-1"]
    self.notify(f"{testlauf}")
    yes = self.full_IDs[testlauf]

    if testlauf in [1, 2, 4, 5, 6, 7, 8]:
        event.prevent_default()
        event.stop()

    if testlauf in [0, 1, 2, 9, 10, 11, 12]:
        self.label.update(arr[testlauf] or "")
        self.c_digits.update("")
        self.e_third.value = ""
        self.e_fourth.value = ""

    if testlauf in [3,4,5,6,7,8]:
        st.current = yes
        table = self.query_one(
            f"#{yes}", DataTable)
        coordinates = table.cursor_coordinate
        on_cell_highlighted_(self, coordinates)

    if testlauf in [0,1,2]:
        sw.current = yes
        tree = self.query_one(
            f"#{yes}", FileTypeTree)
        tree.reload()


def on_cell_highlighted_(self, coordinate) -> None:
    cool = self.query_one("#cont-switch-1",ContentSwitcher)
    digits = self.query_one("#digits-0", Digits)
    label = self.query_one("#label-0", Label)
    fourth = self.query_one("#fourth", Input)
    third = self.query_one("#third", Input)
    switch = cool.current.split("-")[-1]
    switchers = '2' if switch == '3' else switch
    config9 = self.app.store[f"2-{switchers}"]
    config = self.app.store[f"3-{switchers}"]
    row, col = coordinate
    digits.update("")
    label.update("")
    third.value = ""
    fourth.value = ""

    def safe(obj, *keys):
        for key in keys:
            try:
                obj = obj[key]
            except (IndexError, KeyError, TypeError):
                return None
        return obj

    try:
        switches = int(switch)
        if switches in [0,4,5]:
            cell = safe(config, row, col)
            values_ = safe(config9, row, col) or ""
            configs = safe(config9, row, col) or ""

            if cell is not None:
                label.update(cell)

            if values_ is not None:
                digits.update(values_[0])

            if configs is not None:
                rrr = configs[1]
                rrt = configs[2]
                fourth.value = rrr
                third.value = rrt

        elif switches in [1,2,3]:
            value = safe(config9, row) or ""
            cell = safe(config, row) or ""
            check = isinstance(cell, str)
            values = cell if check \
                else safe(config, cell)
            test_ = safe(config9, row,0) or ""

            if value is not None:
                fourth.value = value[1]
                third.value = value[2] \
                    if isinstance(value[2],str) \
                    else self.app.store["00"][value[2]][col]

            if values is not None:
                label.update(values)

            if test_ is not None:
                entries = ("", [""] +
                           [f"{test_[0]}{n:02d}"
                                  for n in range(100)],
                           ["","00"] + [f"{letter}{n:02d}"
                            for letter in "ABC"
                            for n in range(100)],
                           [""] + [f"{letter}{n:02d}"
                            for letter in "DEF"
                            for n in range(100)])
                digits.update(
                    entries[switches][col])

    except IndexError:
        return



async def on_key_(self, event) -> None:
    switcher = self.query_one("#cont-switch-1", ContentSwitcher)
    table = self.query_one(f"#{switcher.current}", DataTable)
    editor = self.query_one("#third", Input)

    if event.key == "f5":
        self.notify(f"{event.key} pressed")
        self.query_one("#button-0", Button).press()

    if event.key == "f6":
        self.notify(f"{event.key} pressed")
        self.query_one("#button-1", Button).press()

    if event.key == "f7":
        self.notify(f"{event.key} pressed")
        self.query_one("#button-2", Button).press()

    if event.key == "f8":
        self.notify(f"{event.key} pressed")
        self.query_one("#button-6", Button).press()

    if event.key == "f9":
        self.notify(f"{event.key} pressed")
        self.query_one("#button-3", Button).press()

    if event.key == "f10":
        self.notify(f"{event.key} pressed")
        self.query_one("#button-4", Button).press()

    if event.key == "tab":
        action_next_table(self,event,1)

    elif event.key == "shift+tab":
        action_next_table(self,event,-1)

    if isinstance(self.app.focused, DataTable):
        cursor_coord = table.cursor_coordinate

        if len(event.key) == 1 and event.key.isprintable() or event.key == "backspace":
            current_value = table.get_cell_at(cursor_coord)

            if len(event.key) == 1 and event.key.isprintable() or event.key == "backspace":
                editor.value = "" if event.key == "backspace" else event.key
                editor.cursor_position = len(event.key)
                self.notify("yes")
            else:
                self.notify("no")
                editor.value = str(current_value)

            self.coord = cursor_coord
            editor.focus()
            event.stop()

            def after_focus():
                editor.cursor_position = len(editor.value)
            self.call_after_refresh(after_focus)

    if isinstance(self.app.focused, Input):
        if event.key == "escape":
            self.coord = None
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


def on_pressed(self, event, ImageTab) -> None:
    zz = self.app.store
    yy = self.app.stores
    id = event.button.id
    arr = zz["4-0"]
    arr0 = zz["4-1"]
    yes = yy.setdefault("0", {})
    yay = yes.setdefault("42", {})
    arr1 = arr.index(id) \
        if id in arr else -1

    self.notify(f"Button {id} {arr1} pressed")
    texts = arr0[arr1]
    self.label.update(texts)

    if id == "button-0":
        yay[0] = 1 - (yay.get(0) or 0)
        self.app.clear_notifications()
        self.notify(
            f"A00 SEED {self.turi[yay[0]]} ")
    elif id == "button-1":
        yay[1] = 1 - (yay.get(1) or 0)
        self.app.clear_notifications()
        self.notify(
            f"B00 SEED {self.turi[yay[1]]}")
    elif id == "button-2":
        yay[2] = 1 - (yay.get(2) or 0)
        self.app.clear_notifications()
        self.notify(
            f"D00 SEED {self.turi[yay[2]]} ")

    if 12 <= arr1 <= 14:
        self.notify("models-0")
        pre = (1,2,0)[arr1-12]
        post = {**self.app.stores}
        load = ({},post,post)[arr1-12]
        load.update({'_': pre})
        self.e_images.config = load
        # self.e_images.mutate_reactive(
        #     ImageTab.config)

    if arr1 == 12:
        CONFIGS.write_text(
        json.dumps({}))


def on_submitted(self, event, image) -> None:
    if self.coord is not None:
        e_tables = self.query_one(
            f"#{self.f_right.current}", DataTable)
        e_tables.update_cell_at(self.coord, event.value)
        switches = self.f_right.current.split("-")[-1]
        checker = 2 if 7 <= self.coord.row <= 16 else 1
        checkers = checker if int(switches) == 0 else 1
        tst = self.get_all_data(e_tables)
        self.app.stores[switches] = tst
        yays = {**self.app.stores}
        yays.update({'_': checkers})

        self.notify("models-1")
        self.e_images.config = yays
        self.e_third.value = ""
        self.coord = None
        e_tables.focus()

        CONFIGS.write_text(
        json.dumps(self.app.stores))


