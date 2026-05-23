from textual.widgets import (
    DataTable, Input, ContentSwitcher, Digits, Label)
from textual.coordinate import Coordinate
from Backend.model import FileTypeTree
from pathlib import Path
import shutil
import time


CWD = Path.cwd()
PATH_FILE = Path(__file__).parent
STATIC_DIR = PATH_FILE.parent / "Fontend"
CONFIGS = STATIC_DIR / "model.json"

def action_next_table(self, event, prefix) -> None:
    f0 = self.query_one("#cont-switch-0", ContentSwitcher)
    f1 = self.query_one("#cont-switch-1", ContentSwitcher)
    f2 = self.full_IDs.index(self.app.focused.id)
    f3 = (f2 + prefix) % len(self.full_IDs)
    f4 = self.app.store["4-1"]
    f5 = self.full_IDs[f3]
    self.notify(f"{f3}")

    if f3 in [1, 2, 4, 5, 6, 7, 8]:
        event.prevent_default()
        event.stop()

    if f3 in [0, 1, 2, 9, 10, 11, 12]:
        self.label.update(f4[f3] or "")
        self.c_digits.update("")
        self.e_third.value = ""
        self.e_fourth.value = ""

    if f3 in [3,4,5,6,7,8]:
        f1.current = f5
        table = self.query_one(
            f"#{f5}", DataTable)
        coordinates = table.cursor_coordinate
        on_cell_highlighted_(self, coordinates)

    if f3 in [0,1,2]:
        f0.current = f5
        tree = self.query_one(
            f"#{f5}", FileTypeTree)
        tree.reload()


def on_cell_highlighted_(self, coordinate) -> None:
    f0 = self.query_one("#cont-switch-1")
    f1 = self.query_one("#digits-0", Digits)
    f2 = self.query_one("#label-0", Label)
    f3 = self.query_one("#fourth", Input)
    f4 = self.query_one("#third", Input)
    f5 = f0.current.split("-")[-1]
    f6 = '2' if f5 == '3' else f5
    f7 = self.app.store[f"2-{f6}"]
    f8 = self.app.store[f"3-{f6}"]
    row, col = coordinate
    f1.update("")
    f2.update("")
    f4.value = ""
    f3.value = ""

    def safe(obj, *keys):
        for key in keys:
            try:
                obj = obj[key]
            except (IndexError, KeyError, TypeError):
                return None
        return obj

    try:
        switches = int(f5)
        if switches in [0,4,5]:
            cell = safe(f8, row, col)
            values_ = safe(f7, row, col) or ""
            configs = safe(f7, row, col) or ""

            if cell is not None:
                f2.update(cell)

            if values_ is not None:
                f1.update(values_[0])

            if configs is not None:
                rrr = configs[1]
                rrt = configs[2]
                f3.value = rrr
                f4.value = rrt

        elif switches in [1,2,3]:
            value = safe(f7, row) or ""
            cell = safe(f8, row) or ""
            check = isinstance(cell, str)
            values = cell if check \
                else safe(f8, cell)
            test_ = safe(f7, row,0) or ""

            if value is not None:
                f3.value = value[1]
                f4.value = value[2] \
                    if isinstance(value[2],str) \
                    else self.app.store["00"][value[2]][col]

            if values is not None:
                f2.update(values)

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
                f1.update(
                    entries[switches][col])

    except IndexError:
        return



async def on_key_(self, event) -> None:
    f0 = self.query_one("#cont-switch-1")
    f1 = self.query_one(f"#{f0.current}")
    f2 = self.query_one("#third", Input)
    f3 = event.key

    match f3:
        case "f5":
            self.notify(f"{f3} pressed")
            self.query_one("#button-0").press()

        case "f6":
            self.notify(f"{f3} pressed")
            self.query_one("#button-1").press()

        case "f7":
            self.notify(f"{f3} pressed")
            self.query_one("#button-2").press()

        case "f8":
            self.notify(f"{f3} pressed")
            self.query_one("#button-6").press()

        case "f9":
            self.notify(f"{f3} pressed")
            self.query_one("#button-3").press()

        case "f10":
            self.notify(f"{f3} pressed")
            self.query_one("#button-4").press()

        case "tab":
            action_next_table(self,event,1)

        case "shift+tab":
            action_next_table(self,event,-1)

    if isinstance(self.app.focused, DataTable):
        cursor_coord = f1.cursor_coordinate

        if len(event.key) == 1 and event.key.isprintable() or event.key == "backspace":
            current_value = f1.get_cell_at(cursor_coord)

            if len(event.key) == 1 and event.key.isprintable() or event.key == "backspace":
                f2.value = "" if event.key == "backspace" else event.key
                f2.cursor_position = len(event.key)
                self.notify("yes")
            else:
                self.notify("no")
                f2.value = str(current_value)

            self.coord = cursor_coord
            f2.focus()
            event.stop()

            def after_focus():
                f2.cursor_position = len(f2.value)
            self.call_after_refresh(after_focus)

    if isinstance(self.app.focused, Input):
        if event.key == "escape":
            self.coord = None
            f2.value = ""
            f1.focus()


    # IS THIS NEEDED ?????
    # IS THIS NEEDED ?????

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
                [f1.get_cell_at(Coordinate(r, c)) for c in range(c1, c2 + 1)]
                for r in range(r1, r2 + 1)
            ]
            self._visual_mode = False
            self._visual_start = None
            self.notify(f"Yanked {r2 - r1 + 1}×{c2 - c1 + 1}")

        else:          # yank
            self._clipboard = f1.get_cell_at(self._cursor)
            self.notify(f"Copied: {self._clipboard}")  # toast confirmation

    elif event.key == "p" and self._clipboard is not None:  # paste
        if isinstance(self._clipboard, list):
            for ri, row in enumerate(self._clipboard):
                for ci, val in enumerate(row):
                    try:
                        f1.update_cell_at(
                            Coordinate(self._cursor.row + ri, self._cursor.column + ci),
                            val
                        )
                    except Exception:
                        pass  # silently skip out-of-bounds
            self.notify(f"Pasted {len(self._clipboard)}×{len(self._clipboard[0])}")

        else:
            f1.update_cell_at(self._cursor, self._clipboard)






def on_pressed(self, event) -> None:
    f0 = self.app.store
    f1 = self.app.stores
    f2 = event.button.id
    f3 = f2.split("-")[-1]
    f5 = f1.setdefault("0", {})
    f6 = f5.setdefault("37", {})
    f7 = f5.setdefault("38", {})
    f8 =  f0["4-0"].index(f2) \
        if f2 in f0["4-0"] else -1
    f9 = self.turi
    f10 = f0["4-1"][f8]
    self.label.update(f10)
    f11 = {"6": 2, "3": 1}
    f12 = {"6": 1, "3": 2}

    if f2 == "button-6":
        self.app.stores = {}

    elif f2 == "button-0":
        f6[0] = 1 - f6.get(0,0)
        self.app.clear_notifications()
        self.notify(f"A00 SEED {f9[f6[0]]} ")

    elif f2 == "button-1":
        f6[1] = 1 - f6.get(1,0)
        self.app.clear_notifications()
        self.notify(f"B00 SEED {f9[f6[1]]}")

    elif f2 == "button-2":
        f6[2] = 1 - f6.get(2,0)
        self.app.clear_notifications()
        self.notify(f"D00 SEED {f9[f6[2]]} ")

    elif f2 == "button-3":
        f12 = f5.get('37', {})
        f13 = int(time.time())
        for k in ['0', '1', '2']:
            if f12.get(k, 0) == 0:
                f7[k] = f13

    elif f2 == "button-4":
        f14 = int(time.time())
        f16 = STATIC_DIR / "model.png"
        f15 = STATIC_DIR / "model.json"
        image_outs = CWD / f"{f14}.json"
        image_outs_ = CWD / f"{f14}.png"
        shutil.copy2(f15, image_outs)
        shutil.copy2(f16, image_outs_)

    if (f2 == "button-6"
            or f2 == "button-3"):
        f17 = {**self.app.stores}
        f18 = {} if f3 == '6' else f17
        f19 = [f11[f3],f12[f3]]
        f18.update({'_': f19})
        self.e_images.config = f18


def on_submitted(self, event) -> None:
    if self.coord is not None:
        f0 = range(24, 31)
        f1 = range(0, 10)
        f2 = self.query_one(
            f"#{self.f_right.current}")
        f2.update_cell_at(self.coord, event.value)
        f3 = self.f_right.current.split("-")[-1]
        f4 = self.get_all_data(f2)
        f5 = any(int(k) in f0 for k in f4)
        f6 = any(int(k) in f1 for k in f4)
        f7 = 2 if f6 else (0 if f5 else 1)
        f8 = f7 if int(f3) == 0 else 1
        self.notify(f"here {f8}")
        self.app.stores[f3] = f4
        f9 = {**self.app.stores}
        f9.update({'_': [0,f8]})
        self.e_images.config = f9
        self.e_third.value = ""
        self.coord = None
        f2.focus()

