import json
import shutil
import time
from pathlib import Path

from textual.widgets import DataTable, Input

from .model import MainTab
from .script import script_f5, script_f6

PORT = Path.cwd()
PORT_0 = Path(__file__).parent
PORT_1 = PORT_0.parent / "Formula"
PATH_1 = PORT_1 / "var.json"


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
    f9 = f3.column
    f10 = f3.row
    f11 = str(f8)
    f7.value = ""
    f1.focus()

    f12 = (
        (11, 23, 31),
        (18, 36, 54, 73, 92),
        (10, 22, 33, 44, 55, 65),
        (10, 22, 33, 44, 55, 65),
        (),
        (),
    )

    if f10 not in f12[f8] and f9 >= 1:
        f13 = f10 in range(24, 31)
        f14 = f10 in range(0, 10)
        f15 = 0 if f13 else 1
        f16 = 2 if f14 else f15
        f17 = f16 if f8 == 0 else 1
        f1.update_cell_at(f3, f6)
        f5[f11] = self.get_data(f1)

        f18 = {**self.app.stores}
        f18.update({"_": [0, f17]})
        f2.config = f18

    if not event.value:
        on_highlighted(self, f3)


def on_shift_tab(self, event, prefix) -> None:
    f00 = (-1, 0, 1, 3, 4, 5, 6, 7, 14)
    f01 = (0, 1, 2, 9, 10, 11, 12, 13, 14)
    f0 = self.query_one("#cont-switch-0")
    f1 = self.query_one("#cont-switch-1")
    f2 = self.query_one("#dir-tree-0")
    f3 = self.query_one("#digits-0")
    f4 = self.query_one("#button-5")
    f5 = self.query_one("#input-1")
    f6 = self.query_one("#input-0")
    f7 = self.query_one("#label-0")
    f8 = self.app.store["4-0"]
    f9 = self.app.store["000"]
    f10 = self.app.stores
    f11 = self.app.focused
    f12 = f9.index(f11.id)
    f13 = f12 + prefix
    f14 = f13 % len(f9)
    f15 = min(prefix, 0)
    f16 = f9[f14] or ""
    f17 = f12 + f15

    if event is not None and f17 in f00:
        event.prevent_default()
        event.stop()

    if f14 in f01:
        f18 = f8.get(f9[f14], "")
        self.app.textfield = f18
        f7.update(f18)
        f3.update("")
        f5.value = ""
        f6.value = ""

    f19 = f10.setdefault("0", {})
    f20 = f19.setdefault("40", {})
    if f14 in (3, 4, 5, 6, 7, 8):
        f21 = self.query_one(f"#{f16}")
        f22 = f21.cursor_coordinate
        f20["2"] = f22.column
        f20["1"] = f22.row
        f1.current = f16
        on_highlighted(self, f22)

    if f14 in (0, 1, 2):
        f0.current = f16
    if f17 == 14:
        f2.focus()
    if f17 == -1:
        f4.focus()

    f20["0"] = f14 + 1
    PATH_1.write_text(json.dumps(f10))


def on_highlighted(self, event) -> None:
    f0 = self.query_one("#cont-switch-1")
    f1 = self.query_one(f"#{f0.current}")
    f2 = self.query_one("#digits-0")
    f3 = self.query_one("#label-0")
    f4 = self.query_one("#input-0")
    f5 = self.query_one("#input-1")
    f6 = f0.current.split("-")[-1]
    f7 = "2" if f6 == "3" else f6
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

    if int(f6) in (1, 2, 3):
        f15 = len(f11) > f14
        f16 = len(f12) > f14
        f17 = f12[f14] if f16 else ""
        f18 = f11[f14] if f15 else []
        f19 = isinstance(f17, str)
        f20 = f17 if f19 else f12[f17]

        if len(f20) > 0:
            f3.update(f20)
        if len(f18) > 2:
            f4.value = f18[1]
            f5.value = (
                f9 or f18[2]
                if isinstance(f18[2], str)
                else f10["00"][f18[2]][f13]
            )

            f2.update(
                (
                    "",
                    [""]
                    + [
                        f"{f18[0][0]}{h:02d}"
                        for h in range(100)
                    ],
                    ["", "00"]
                    + [
                        f"{h0}{h1:02d}"
                        for h0 in "ABC"
                        for h1 in range(100)
                    ],
                    [""]
                    + [
                        f"{h2}{h3:02d}"
                        for h2 in "DEF"
                        for h3 in range(100)
                    ],
                )[int(f6)][f13]
            )

    elif int(f6) in (0, 4, 5):
        f21 = f11[f14] if len(f11) > f14 else []
        f22 = f21[f13] if len(f21) > f13 else []
        f23 = f12[f14] if len(f12) > f14 else []
        f24 = f23[f13] if len(f23) > f13 else ""

        if len(f24) > 0:
            if int(f6) == 0:
                f3.update(f24)
        if int(f6) in (4, 5):
            f25 = f12[f13]
            f3.update(f25)
        if len(f22) > 2:
            f2.update(f22[0])
            f4.value = f9 or f22[1]
            f5.value = f9 or f22[2]


def on_pressed(self, event) -> None:
    f0 = self.query_one("#cont-switch-1")
    f1 = self.query_one(f"#{f0.current}")
    f2 = self.query_one("#label-0")
    f3 = self.query_one(MainTab)
    f4 = f1.cursor_coordinate
    f5 = self.app.store
    f6 = self.app.stores
    f7 = event.button.id
    f8 = {"0": 1, "4": 2}
    f9 = {"0": 2, "4": 1}
    f10 = f7.split("-")[-1]
    f11 = f6.setdefault("0", {})
    f12 = f11.setdefault("38", {})
    f13 = f11.setdefault("39", {})
    f14 = f5["4-0"].get(f7, "")
    self.app.textfield = f14
    f2.update(f14)

    if int(f10) == 1:
        f15 = f12.get("0", 0)
        f12[0] = 1 - f15

    elif int(f10) == 2:
        f16 = f12.get("1", 0)
        f12[1] = 1 - f16

    elif int(f10) == 3:
        f17 = f12.get("2", 0)
        f12[2] = 1 - f17

    elif int(f10) == 4:
        f18 = int(time.time())
        f19 = f11.get("38", {})
        for h in ("0", "1", "2"):
            if f19.get(h, 0) == 0:
                f13[h] = f18

    elif int(f10) == 5:
        f20 = int(time.time())
        f21 = PORT / f"{f20}.json"
        shutil.copy2(PATH_1, f21)
        f22 = {**self.app.stores}
        f22.update({"_": [0, 4]})
        f3.config = f22

    elif int(f10) == 0:
        self.app.stores = {}
        f23 = self.app.stores
        f24 = f23.setdefault("0", {})
        f25 = f24.setdefault("40", {})
        f23.setdefault("39", {})
        f25["2"] = f4.column
        f25["1"] = f4.row

    if int(f10) in (0, 4):
        f26 = {**self.app.stores}
        f27 = [f9[f10], f8[f10]]
        f26.update({"_": f27})
        f3.config = f26

    if int(f10) in (1, 2, 3):
        f28 = int(f10) - 1
        f29 = f12.get(str(f28), 0)
        f30 = ["", "de"]
        f31 = f30[f29]
        script_f6(self, f7, f31)

    if int(f10) in (0, 4, 5):
        script_f6(self, f7, "")


async def on_key(self, event) -> None:
    f0 = (
        "delete",
        "f1",
        "f2",
        "f3",
        "f4",
        "f5",
        "f6",
        "f7",
        "f8",
        "f9",
    )
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
        script_f5(self, f17)

    if not isinstance(f15, Input):
        if f17 == "shift+tab":
            on_shift_tab(self, event, -1)
        elif f17 == "tab":
            on_shift_tab(self, event, 1)

    if isinstance(f15, Input):
        if f17 == "tab":
            event.stop()
            event.prevent_default()
            self.post_message(
                Input.Submitted(f11, f11.value)
            )
        if event.key == "escape":
            on_highlighted(self, f13)
            f4.focus()

    if isinstance(f15, DataTable):
        if len(f17) == 1 or f17 in f1:
            f18 = int(f12) in (4, 5)
            f19 = f13.column == 12
            f20 = int(f12) - 3
            event.stop()

            if f18 and f19:
                f21 = self.query_one(
                    f"dir-tree-{f20}"
                )
                f22 = f"dir-tree-{f20}"
                f2.current = f22
                f21.focus()

            elif not f18 or not f19:
                f11.focus()
                if f17 in f1:
                    f11.value = f16

                elif len(f17) == 1:
                    f11.value = f17
                    f23 = "cursor_position"
                    self.call_after_refresh(
                        lambda: setattr(
                            f11, f23, len(f17)
                        )
                    )

    match f17:
        case "delete":
            self.post_message(
                Input.Submitted(f11, "")
            )

        case "f1":
            f39 = self.app
            f39.clipboards = f16
            self.post_message(
                Input.Submitted(f11, "")
            )

        case "f2":
            f39 = self.app
            f39.clipboards = f16

        case "f3":
            self.post_message(
                Input.Submitted(f11, f70)
            )

        case "f4":
            f6.press()
        case "f5":
            f7.press()
        case "f6":
            f8.press()
        case "f7":
            f5.press()
        case "f8":
            f9.press()
        case "f9":
            f10.press()
