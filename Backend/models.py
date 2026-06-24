from textual.widgets import (DataTable, Input)
from .model import MainTab
from pathlib import Path
from .script import script_f5, script_f6
import shutil
import time
import json

PORT = Path.cwd()
PORT_0 = Path(__file__).parent
PORT_1 = PORT_0.parent / "Formula"
PATH_1 = PORT_1 / "za.json"

def on_submitted(self, event) -> None:
    f0 = self.query_one("#cont-switch-1")
    f1 = self.query_one(f"#{f0.current}")
    f2 = self.query_one(MainTab)
    f3 = f1.cursor_coordinate
    f4 = f0.current.split("-")
    f5 = self.app.stores
    f6 = event.value
    f7 = event.input
    f8 = int(f4[-1])
    f9 = str(f8)
    f10 = f3.row
    f7.value = ""
    f1.focus()

    f11 = ((11,23,31),
           (18,36,54,73,92),
           (10,22,33,44,55,65),
           (10,22,33,44,55,65),(),())

    if f10 not in f11[f8]:
        f1.update_cell_at(f3,f6)
        f5[f9] = self.get_data(f1)
        f12 = f10 in range(24, 31)
        f13 = f10 in range(0, 10)
        f14 = 0 if f12 else 1
        f15 = 2 if f13 else f14
        f16 = f15 if f8 == 0 else 1

        f17 = {**self.app.stores}
        f17.update({'_': [0,f16]})
        f2.config = f17

    if not event.value:
        on_highlighted(
            self, f3)

def on_shift_tab(self, event, prefix) -> None:
    f0 = self.query_one("#cont-switch-0")
    f1 = self.query_one("#cont-switch-1")
    f2 = self.query_one("#dir-tree-0")
    f3 = self.query_one("#digits-0")
    f4 = self.query_one("#button-5")
    f5 = self.query_one("#input-1")
    f6 = self.query_one("#input-0")
    f7 = self.query_one("#label-0")
    f8 = self.app.store["4-0"]
    f9 = self.app.store["4-1"]
    f89 = self.app.stores
    f10 = self.app.focused
    f11 = f8.index(f10.id)
    f12 = f11 + prefix
    f13 = f12 % len(f8)
    f14 = min(prefix,0)
    f15 = f8[f13] or ""
    f16 = f11 + f14

    if (event is not None and
            f16 in (-1,0,1,3,4,5,6,7,14)):
        event.prevent_default()
        event.stop()

    if f13 in (0,1,2,9,10,11,12,13,14):
        self.app.textfield = f9[f13]
        f7.update(f9[f13])
        f3.update("")
        f5.value = ""
        f6.value = ""

    if f13 in (3,4,5,6,7,8):
        f17 = self.query_one(f"#{f15}")
        f18 = f17.cursor_coordinate
        on_highlighted(self, f18)
        f1.current = f15

    if f13 in (0,1,2):
        f0.current = f15
    if f16 == 14: f2.focus()
    if f16 == -1: f4.focus()

    f24 = f89.setdefault('0', {})
    f25 = f24.setdefault('40', {})
    f25["0"] = f13 or "" or 0
    PATH_1.write_text(
        json.dumps(f89))

def on_highlighted(self, event) -> None:
    f0 = self.query_one("#cont-switch-1")
    f1 = self.query_one(f"#{f0.current}")
    f2 = self.query_one("#digits-0")
    f3 = self.query_one("#label-0")
    f4 = self.query_one("#input-0")
    f5 = self.query_one("#input-1")
    f6 = f0.current.split("-")[-1]
    f7 = '2' if f6 == '3' else f6
    f8 = f1.cursor_coordinate
    f9 = f1.get_cell_at(f8)
    f10 = self.app.store
    f11 = f10[f"2-{f7}"]
    f12 = f10[f"3-{f7}"]
    f13 = event.column
    f14 = event.row
    f2.update("")
    f3.update("")
    f5.value = ""
    f4.value = ""

    if int(f6) in (1,2,3):
        f15 = len(f11) > f14
        f16 = len(f12) > f14
        f17 = f12[f14] if f16 else ""
        f18 = f11[f14] if f15 else []
        f19 = isinstance(f17, str)
        f20 = f17 if f19 \
            else f12[f17]

        if len(f20) > 0:
            f3.update(f20)
        if len(f18) > 2:
            f4.value = f18[1]
            f5.value = f9 or f18[2] \
                if isinstance(f18[2],str) \
                else f10["00"][f18[2]][f13]

            f2.update(("", [""] +
                       [f"{f18[0][0]}{n:02d}"
                        for n in range(100)],
                       ["","00"] +
                       [f"{letter}{n:02d}"
                        for letter in "ABC"
                        for n in range(100)],
                       [""] +
                       [f"{letter}{n:02d}"
                        for letter in "DEF"
                        for n in range(100)])
                      [int(f6)][f13])

    elif int(f6) in (0,4,5):
        f21 = f11[f14] if len(f11) > f14 else []
        f22 = f21[f13] if len(f21) > f13 else []
        f23 = f12[f14] if len(f12) > f14 else []
        f24 = f23[f13] if len(f23) > f13 else ""

        if len(f24) > 0:
            if int(f6) == 0:
                f3.update(f24)
        if int(f6) in (4,5):
            f22 = f12[f13]
            f3.update(f22)
        if len(f22) > 2:
            f2.update(f22[0])
            f4.value = f9 or f22[1]
            f5.value = f9 or f22[2]

def on_pressed(self, event) -> None:
    f0 = self.query_one("#label-0")
    f1 = self.query_one(MainTab)
    f2 = self.app.store
    f3 = self.app.stores
    f4 = event.button.id
    f5 = f4.split("-")[-1]
    f6 = f3.setdefault("0",{})
    f7 = f6.setdefault("38",{})
    f8 = f6.setdefault("39",{})
    f9 =  f2["4-0"].index(f4) \
        if f4 in f2["4-0"] else -1
    f10 = f2["4-1"][f9]
    f11 = {"0": 2, "4": 1}
    f12 = {"0": 1, "4": 2}
    self.app.textfield = f10
    f0.update(f10)

    if int(f5) == 1:
        f13 = f7.get("0",0)
        f7[0] = 1 - f13

    elif int(f5) == 2:
        f14 = f7.get("1",0)
        f7[1] = 1 - f14

    elif int(f5) == 3:
        f15 = f7.get("2",0)
        f7[2] = 1 - f15

    elif int(f5) == 4:
        f16 = int(time.time())
        f17 = f6.get('38', {})
        for h in ('0','1','2'):
            if f17.get(h, 0) == 0:
                f8[h] = f16

    elif int(f5) == 5:
        f18 = int(time.time())
        f19 = PORT / f"{f18}.json"
        shutil.copy2(PATH_1,f19)
        f20 = {**self.app.stores}
        f20.update({'_': [0,4]})
        f1.config = f20

    elif int(f5) == 0:
        self.app.stores = {}

    if int(f5) in (0,4):
        f21 = {**self.app.stores}
        f22 = [f11[f5],f12[f5]]
        f21.update({'_': f22})
        f1.config = f21

    if int(f5) in (1,2,3):
        f23 = int(f5) - 1
        f24 = f7.get(
            str(f23), 0)
        f25 = ['', 'de']
        f26 = f25[f24]
        script_f6(
            self, f4, f26)

    if int(f5) in (0,4,5):
        script_f6(self, f4, "")

async def on_key(self, event) -> None:
    f0 = ("delete","f1","f2","f3",
          "f4","f5","f6","f7","f8","f9")
    f1 = ("backspace", "space", "enter")
    f2 = self.query_one("#cont-switch-0")
    f3 = self.query_one("#cont-switch-1")
    f4 = self.query_one(f"#{f3.current}")
    f5 = self.query_one("#button-0")
    f6 = self.query_one("#button-1")
    f7 = self.query_one("#button-2")
    f8 = self.query_one("#button-3")
    f9 = self.query_one("#button-4")
    f10 = self.query_one("#button-5")
    f11 = self.query_one("#input-1")
    f12 = f3.current.split("-")[-1]
    f13 = f4.cursor_coordinate
    f14 = f4.get_cell_at(f13)
    f70 = self.app.clipboards
    f15 = self.app.focused
    f16 = str(f14 or "")
    f17 = event.key

    if f17 in f0:
        script_f5(
            self, f17)

    if not isinstance(f15, Input):
        if f17 == "shift+tab":
            on_shift_tab(
                self, event, -1)
        elif f17 == "tab":
            on_shift_tab(
                self, event, 1)

    if isinstance(f15, Input):
        if f17 == "tab":
            event.stop()
            event.prevent_default()
            self.post_message(
                Input.Submitted(
                f11, f11.value))
        if event.key == "escape":
            on_highlighted(
                self, f13)
            f4.focus()

    if isinstance(f15, DataTable):
        if (len(f17) == 1
                or f17 in f1):
            f18 = int(f12) in (4,5)
            f19 = f13.column == 12
            f20 = int(f12) - 3
            event.stop()

            if f18 and f19:
                f21 = self.query_one(
                    f"dir-tree-{f20}")
                f22 = f"dir-tree-{f20}"
                f2.current = f22
                f21.focus()

            elif (not f18
                  or not f19):
                f11.focus()
                if f17 in f1:
                    f11.value = f16

                elif len(f17) == 1:
                    f11.value = f17
                    f23 = 'cursor_position'
                    self.call_after_refresh(
                        lambda: setattr(
                            f11, f23, len(f17)))

    match f17:
        case "delete":
            self.post_message(
                Input.Submitted(
                    f11, ""))

        case "f1":
            f39 = self.app
            f39.clipboards = f16
            self.post_message(
                Input.Submitted(
                    f11, ""))

        case "f2":
            f39 = self.app
            f39.clipboards = f16

        case "f3":
            self.post_message(
                Input.Submitted(
                    f11, f70))

        case "f4": f6.press()
        case "f5": f7.press()
        case "f6": f8.press()
        case "f7": f5.press()
        case "f8": f9.press()
        case "f9": f10.press()
