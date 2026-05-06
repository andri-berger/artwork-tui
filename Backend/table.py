from textual.containers import VerticalScroll, HorizontalScroll, ScrollableContainer
from textual.containers import Center, Middle
from textual.widgets import DataTable, Input, Label
from textual.coordinate import Coordinate
from textual.screen import ModalScreen
from textual.app import ComposeResult
from textual.widget import Widget
from .imageTab import ImageTab
from textual.containers import Horizontal
from itertools import cycle
from textual import on
cursors = cycle(["cell"])


class CellEditModal(ModalScreen[str]):
    def __init__(self, value: str):
        super().__init__()
        self._value = value

    def compose(self) -> ComposeResult:
        yield Label("Edit value")
        yield Input(value=self._value, id="editor")

    def on_input_submitted(self, event: Input.Submitted) -> None:
        self.dismiss(event.value)  # return new value to caller

    def on_key(self, event) -> None:
        if event.key == "escape":
            self.dismiss(None)  # cancel — return None

class TableApp(Widget):
    DEFAULT_CSS = """   
    
    HorizontalScroll {
        height: 3fr; 
        width: 90%;
        align: center middle;                                                                                      
    }  
    
    ImageTab {
        align: center middle; 
    }
      
    Horizontal {
        height: 2fr;                                                                                       
    }                                                                                     
    """


    def __init__(self) -> None:
        super().__init__()
        self._cursor = None
        self._visual_start = None
        self._visual_mode = False
        self._clipboard = None

    def compose(self) -> ComposeResult:
        with HorizontalScroll():
            yield ImageTab()
        with Horizontal():
            yield DataTable()



    def on_mount(self) -> None:
        rows = self.app.config['5-1']
        table = self.query_one(DataTable)
        table.cursor_type = next(cursors)
        table.fixed_rows = 0
        table.fixed_columns = 3
        table.zebra_stripes = True
        table.add_columns(*rows[0])
        table.add_rows(rows[1:])

    def get_all_data(self, table: DataTable):
        skip_rows = 0
        skip_cols = 3

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

    def set_all_data(self):
        table = self.query_one(DataTable)
        images = self.query_one(ImageTab)
        tst = self.get_all_data(table)
        self.notify(f"TST: {tst}")
        images.config = tst

    @on(DataTable.CellHighlighted)
    def track_cursor(self, event: DataTable.CellHighlighted) -> None:
      self._cursor = event.coordinate

    @on(DataTable.CellSelected)
    async def on_cell_selected(self, event: DataTable.CellSelected) -> None:
      coord = event.coordinate

      def apply(new_value: str | None) -> None:
          if new_value is not None:
              self.query_one(DataTable).update_cell_at(coord, new_value)
              self.set_all_data()
      await self.app.push_screen(CellEditModal(str(event.value)), apply)

    async def on_key(self, event) -> None:
        table = self.query_one(DataTable)

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
        table = self.query_one(DataTable)
        table.cursor_type = next(cursors)