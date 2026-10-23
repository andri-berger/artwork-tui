import json
import time
from pathlib import Path

from textual.coordinate import Coordinate
from textual.widgets import DataTable, Input
from textual_image.widget import Image

from .model import MainTab
from .script import (
    script_f00,
    script_f5,
    script_f6,
)

PORT_0 = script_f00()
PORT_1 = Path(__file__).parent
PORT_2 = PORT_1.parent / "Formula"
PATH_2 = PORT_0 / "1700000000.json"
PATH_3 = ["", "00"] + [
    f"{h}{h0:02d}"
    for h in "ABC"
    for h0 in range(100)
]
PATH_4 = [""] + [
    f"{h}{h0:02d}"
    for h in "DEF"
    for h0 in range(100)
]


def on_display(self, h) -> None:
    for h0 in range(6):
        f0 = self.query_one(f"#button-{h0}")
        f0.display = h
    for h1 in range(2):
        f1 = self.query_one(f"#input-{h1}")
        f1.display = h
    f2 = self.query_one("#input-2")
    f2.display = not h


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

    if f10 == 34 and f8 == 0:
        self.app.theme = "textual-dark"

    if f10 not in f12[f8] and f9 >= 1:
        f14 = f10 in range(24, 31)
        f15 = f10 in range(0, 10)
        f16 = 0 if f14 else 1
        f17 = 2 if f15 else f16
        f18 = f17 if f8 == 0 else 1
        f1.update_cell_at(f3, f6)
        # Keep keys past the table rows
        # (table 0: 35 locks, 36 seeds,
        # 37 cursor and picked assets)
        f13 = f5.get(f11) or {}
        f5[f11] = {
            **{
                h: h0
                for h, h0 in f13.items()
                if int(h) >= f1.row_count
            },
            **self.get_data(f1),
        }

        f19 = {**self.app.stores}
        f19.update({"_": [0, f18]})
        f2.config = f19

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

    if f14 != 8:
        on_display(self, True)

    if event is not None and f17 in f00:
        event.prevent_default()
        event.stop()

    if f14 in f01:
        f22 = f8.get(f9[f14], "")
        f7.update(f22)
        f3.update("")
        f5.value = ""
        f6.value = ""

    f19 = f10.setdefault("0", {})
    f20 = f19.setdefault("37", {})
    if f14 in (3, 4, 5, 6, 7, 8):
        f23 = self.query_one(f"#{f16}")
        f24 = f23.cursor_coordinate
        f20["2"] = f24.column
        f20["1"] = f24.row
        f1.current = f16
        on_highlighted(self, f24)

    if f14 in (0, 1, 2):
        f0.current = f16
    if f17 == 14:
        f2.focus()
    if f17 == -1:
        f4.focus()

    f20["0"] = f14 + 1
    PATH_2.write_text(json.dumps(f10))


def on_theme(self, prefix) -> None:
    # F10/F11: previous/next theme, kept in
    # the table 0 theme cell ("34"/"0") and
    # autosaved, like an edit plus CREATE
    f0 = self.app.store["001"]
    f1 = self.query(DataTable)[0]
    f2 = self.app.stores
    f3 = self.app.theme
    f4 = f0.index(f3) if f3 in f0 else 0
    f5 = (f4 + prefix) % len(f0)
    self.app.theme = f0[f5]
    f1.update_cell_at(Coordinate(34, 1), str(f5))
    f6 = f2.setdefault("0", {})
    f6.setdefault("34", {})["0"] = f5
    PATH_2.write_text(json.dumps(f2))
    self.notify(f0[f5], title=f"Theme {f5}")


def on_highlighted(self, event) -> None:
    f0 = self.query_one("#cont-switch-1")
    f1 = self.query_one(f"#{f0.current}")
    f2 = self.query_one("#digits-0")
    f3 = self.query_one("#label-0")
    f4 = self.query_one("#input-0")
    f5 = self.query_one("#input-1")
    f05 = self.query_one("#input-2")
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
    f05.value = ""
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

            if int(f6) == 1:
                f34 = [""] + [
                    f"{f18[0][0]}{h:02d}"
                    for h in range(100)
                ]
            else:
                f34 = (PATH_3, PATH_4)[
                    int(f6) - 2
                ]
            f2.update(f34[f13])

    elif int(f6) in (0, 4, 5):
        f21 = f11[f14] if len(f11) > f14 else []
        f22 = f21[f13] if len(f21) > f13 else []
        f23 = f12[f14] if len(f12) > f14 else []
        f24 = f23[f13] if len(f23) > f13 else ""

        if int(f6) == 5:
            on_display(self, f13 != 13)

        if len(f24) > 0:
            if int(f6) == 0:
                f3.update(f24)
        if int(f6) in (4, 5):
            f33 = f12[f13]
            f3.update(f33)
        if len(f22) > 2:
            f2.update(f22[0])
            f4.value = f22[1]
            f5.value = f9 or f22[2]
            f05.value = f9 or f22[2]


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
    f12 = f11.setdefault("35", {})
    f13 = f11.setdefault("36", {})
    f14 = f5["4-0"].get(f7, "")
    f2.update(f14)
    f32 = str(event.button.label)

    if int(f10) in (1, 2, 3):
        f15 = str(int(f10) - 1)
        f12[f15] = 1 - f12.get(f15, 0)

    elif int(f10) == 4:
        f3.query(Image).remove()
        f3.hide_rows()
        f18 = int(time.time())
        f19 = f11.get("35", {})
        for h in ("0", "1", "2"):
            if f19.get(h, 0) == 0 or h not in f13:
                f13[h] = f18

    elif int(f10) == 5:
        f20 = int(time.time())
        f21 = PORT_0 / f"{f20}.json"
        # Save the open table and its cursor
        f23 = f11.setdefault("37", {})
        f23["0"] = int(f0.current[-1]) + 4
        f23["1"] = f4.row
        f23["2"] = f4.column
        f22 = {**self.app.stores}
        f22.pop("_", None)
        f21.write_text(json.dumps(f22))
        f22.update({"_": [0, 4, f20]})
        f3.config = f22

    elif int(f10) == 0:
        # Keep the seed locks and their seeds
        self.app.stores = {
            "0": {
                h: f11[h]
                for h in ("35", "36")
                if h in f11
            }
        }
        f23 = self.app.stores
        f24 = f23.setdefault("0", {})
        f25 = f24.setdefault("37", {})
        # Keep the open table and its cursor
        f25["0"] = int(f0.current[-1]) + 4
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
        script_f6(self, f7, f31, f32)

    if int(f10) in (0, 4, 5):
        script_f6(self, f7, "", f32)


async def on_key(self, event) -> None:
    f0 = ("delete", "f1", "f2", "f3")
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
    f11 = self.query_one("#input-2")
    f12 = self.query_one("#input-1")
    f13 = f3.current.split("-")[-1]
    f14 = f4.cursor_coordinate
    f15 = f4.get_cell_at(f14)
    f16 = self.app.clipboards
    f17 = self.app.focused
    f18 = str(f15 or "")
    f19 = int(f13) == 5
    f20 = f14.column == 13

    f21 = event.key
    f22 = f20 and f19
    f23 = f11 if f22 else f12

    if f21 in f0:
        script_f5(self, f21)

    if not isinstance(f17, Input):
        if f21 == "shift+tab":
            on_shift_tab(self, event, -1)
        elif f21 == "tab":
            on_shift_tab(self, event, 1)

    if isinstance(f17, Input):
        if f21 == "tab":
            event.stop()
            event.prevent_default()
            self.post_message(
                Input.Submitted(f23, f23.value)
            )
        if event.key == "escape":
            on_highlighted(self, f14)
            f4.focus()

    if isinstance(f17, DataTable):
        f24 = len(f21) == 1
        f25 = f21 == "minus"
        f26 = f21 if f24 else "-"
        if f25 or f24 or f21 in f1:
            f27 = int(f13) in (4, 5)
            f28 = f14.column == 12
            f29 = int(f13) - 3
            event.stop()

            if f27 and f28:
                f30 = self.query_one(
                    f"#dir-tree-{f29}"
                )
                f31 = f"dir-tree-{f29}"
                f2.current = f31
                f30.focus()

            elif not f27 or not f28:
                f23.focus()
                if f21 in f1:
                    f23.value = f18

                elif f25 or f24:
                    f23.value = f26
                    f32 = "cursor_position"
                    self.call_after_refresh(
                        lambda: setattr(
                            f23, f32, len(f21)
                        )
                    )

    match f21:
        case "delete" if not isinstance(
            f17, Input
        ):
            self.post_message(
                Input.Submitted(f23, "")
            )

        case "f1":
            f34 = self.app
            f34.clipboards = f18
            self.post_message(
                Input.Submitted(f23, "")
            )

        case "f2":
            f33 = self.app
            f33.clipboards = f18

        case "f3":
            self.post_message(
                Input.Submitted(f23, f16)
            )

        case "f4":
            f5.press()
        case "f5":
            f6.press()
        case "f6":
            f7.press()
        case "f7":
            f8.press()
        case "f8":
            f9.press()
        case "f9":
            f10.press()
        case "f10":
            on_theme(self, -1)
        case "f11":
            on_theme(self, 1)
