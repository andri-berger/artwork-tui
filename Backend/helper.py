
from textual.widgets import (
    DataTable, Input, ContentSwitcher, Digits, Label)
from textual.coordinate import Coordinate


def action_next_table(self, event, prefix) -> None:
    testlauf = (self.full_IDs.index(self.app.focused.id) + prefix) % len(self.full_IDs)

    if testlauf in {1, 2, 4, 5}:
        event.stop()
        event.prevent_default()

    if testlauf < 3 or testlauf >= 6:
        self.label.update("hello")
        self.c_digits.update("")
        self.e_third.value = ""
        self.e_fourth.value = ""

    if testlauf < 6:
        switcher_id = "#cont-switch-1" if testlauf >= 3 else "#cont-switch-0"
        self.query_one(switcher_id, ContentSwitcher).current = self.full_IDs[testlauf]

        if testlauf >= 3:
            self.notify("hello-yes")
            table = self.query_one(f"#{self.full_IDs[testlauf]}", DataTable)
            coordinates = table.cursor_coordinate
            on_cell_highlighted_(self, coordinates)

def on_cell_highlighted_(self, coordinate) -> None:
    digits = self.query_one("#digits-0", Digits)
    label = self.query_one("#label-0", Label)
    fourth = self.query_one("#fourth", Input)
    third = self.query_one("#third", Input)

    switches = int(self.query_one(
        "#cont-switch-1", ContentSwitcher)
                   .current.split("-")[-1])
    config4 = self.app.config[f"4-{switches}"]
    configss = self.app.config[f"3-{switches}"]
    config = self.app.config[f"0-{switches}"]
    lookup = self.app.config["00-0"]
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
        if switches == 0:
            values = safe(config4, row, col)
            configs = safe(configss, row, col)
            cell = safe(config, row, col)
            value = safe(lookup, cell)

            if value is not None:
                label.update(value)

            if values is not None:
                digits.update(values)

            if configs is not None:
                fourth.value = configs[0]
                third.value = configs[1]

        elif switches >= 1:
            value = safe(configss, row)
            cell = safe(config, row)
            values = safe(lookup, cell)
            test = safe(config4, row,0)

            if value is not None:
                fourth.value = value[0]
                third.value = value[1]

            if values is not None:
                label.update(values)

            if test is not None:
                entries = ("", [""] +
                           [f"{config4[row][0]}{n:02d}"
                                  for n in range(100)],
                           ["","00"] + [f"{letter}{n:02d}"
                            for letter in "ABCDEF"
                            for n in range(100)])
                digits.update(
                    entries[switches][col])


    except IndexError:
        return



async def on_key_(self, event) -> None:
    switcher = self.query_one("#cont-switch-1", ContentSwitcher)
    table = self.query_one(f"#{switcher.current}", DataTable)
    editor = self.query_one("#third", Input)

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