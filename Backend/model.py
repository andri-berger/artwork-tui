from textual.widgets import DirectoryTree
from textual.reactive import reactive
from textual_image.widget import Image
from textual.widgets import DataTable
from textual.widget import Widget
from textual.binding import Binding
from textual.app import ComposeResult
from .script import script_f9, script_f8
from .scripts import scripts_f1
from .script import script_f7
from pathlib import Path
from textual import on

import shutil
import base64
import time
import json

PORT = Path.cwd()
PORT_0 = Path(__file__)
PORT_1 = Path(__file__).parent
PORT_2 = PORT_1.parent / "Fontend"
PORT_3 = PORT_1.parent / "Formula"
PORT_4 = PORT_2 / "modules"
PORT_5 = PORT_2 / "module"
PATH_5 = PORT_3 / "var.png"
PATH_6 = PORT_3 / "var.json"
PATH_7 = PORT_2 / "model.png"
PATH = ("async (store) => "
        "window.h11(store)")

class MainTab(Widget):
    config: reactive[dict] = reactive(
        dict, init=False)

    def compose(self) -> ComposeResult:
        yield Image(PATH_7)

    def on_mount(self) -> None:
        f0 = self.query_one(Image)
        f0.styles.width = "auto"
        f0.styles.height = "100%"

    async def watch_config(self, path: dict) -> None:
        f0 = self.app.query_one("#cont-switch-1")
        h2 = int(f0.current.split("-")[-1])
        f2 = [9, 100, 301, 300, 12, 13]
        f3 = self.app.query(DataTable)
        f4 = self.app.playwright
        f5 = self.app.stores
        f6 = self.app.store

        f7, f8 = path.pop("_", [])
        f9 = script_f9(path, f6)
        if self.query_one(Image):
            self.query_one(
                Image).remove()

        if f7 >= 1:
            f10 = f6[f"1-{h2}"]
            with self.app.batch_update():
                f3[h2].clear(columns=False)
                for h1 in range(len(f10)):
                    f29 = [f10[h1][0]] or []
                    f29.extend([""]*f2[h2])
                    f3[h2].add_row(*f29)

        if f8 >= 0:
            f11 = await (
                f4.evaluate(PATH, [f8, f9]))
            f12 = f11[0].split(',')[1]
            f13 = base64.b64decode(f12)
            f14 = f9.get('0', {})
            f15 = f14.get('80',0)

            if f15 in range(1,5):
                f16 = {"h": f15,
                    "h0": f14.get('81',0),
                    "h1": f14.get('82',0),
                    "h2": f14.get('83',0)}
                f13 = scripts_f1(f16, f13)

        if f8 == 4:
            f17 = int(time.time())
            f18 = PORT / f"{f17}.png"
            with open(f18, "wb") as f:
                f.write(f13)

        if f8 <= 3:
            with open(PATH_5, "wb") as f:
                f.write(f13)
            await self.mount(
                Image(PATH_5))
            script_f7(self,
                      PATH_5,
                      Image)

        if f8 == 2:
            f19 = script_f8(
                f11[1], f6)
            f5 = {**f5, **f19}

        if f7 >= 1:
            f20 = f7 == 2
            f21 = (0,6) if f20 else (1,4)
            with self.app.batch_update():
                for h in range(*f21):
                    f22 = int(h) == 3
                    f23 = 2 if f22 else h
                    f24 = f6[f"1-{f23}"]
                    f25 = f5.get(str(h),{})
                    if f25 is not None:
                        f3[h].clear(
                            columns=False)
                        f26 = [str(h0) for
                                h0 in range(f2[h])]
                        for h1 in range(len(f24)):
                            f28 = f25.get(str(h1))
                            f29 = [f24[h1][0]]
                            if f28 is not None:
                                for h2 in f26:
                                    f29.append(
                                    str(f28.get(
                                        h2,"")))
                            f3[h].add_row(*f29)

        PATH_6.write_text(
        json.dumps(f5))

    def render(self):
        return ""

class FileTree(DirectoryTree):
    show_root = False
    BINDINGS = [
        Binding("space",
        "select_cursor",
        "Select")]

    def __init__(self, path,
                 file_type, **kwargs) -> None:
        super().__init__(path, **kwargs)
        self.file_type = file_type

    def filter_paths(self, path) -> list:
        f0 = self.file_type
        return [h for h in path
                if (h.is_dir()
                or f0 == h.suffix.lower())
                and not h.name.startswith(".")]

    @on(DirectoryTree.FileSelected)
    def selected(self, event: DirectoryTree.FileSelected) -> None:
        f0 = self.app.query_one("#cont-switch-1")
        f1 = self.app.query_one(f"#{f0.current}")
        f2 = self.app.query_one(MainTab)
        f3 = f0.current.split("-")[-1]
        f4 = f1.cursor_coordinate
        f5 = event.control.id
        f6 = self.app.stores
        f7 = f5.split("-")[-1]
        f8 = ['4','5'][int(f7)-1]
        f9 = ["module","modules"]
        f10 = ['png','otf']
        f11 = event.path

        if int(f7) >= 1:
            f12 = f4.column
            f13 = str(f4.row)
            f14 = f10[int(f7)-1]
            f15 = f9[int(f7)-1]
            f16 = PORT_2 / f15
            f17 = f16 / f11.name

            if (int(f3) >= 4
                    and f12 == 12):
                f18 = f6.setdefault(f8, {})
                f19 = f18.setdefault(f13, {})
                f20 = f11.name.split(".")
                f19[str(f12-1)] = f20[0]
                f21 = f1.get_cell_at(f4)
                f22 = f"{str(f21)}.{f14}"
                f23 = f16 / f22 / ""
                if f23.exists():
                    f23.unlink()
                f1.update_cell_at(
                    f4,f20[0])

            elif int(f3) <= 3 or f12 != 12:
                f24 = f6.setdefault('0', {})
                f25 = f24.setdefault('40', {})
                f25[str(int(f7)+2)] = f11.name
                if f17.exists():
                    f17.unlink()

            shutil.copy2(f11, f17)
            f26 = {**self.app.stores}
            f26.update({'_':  [0,1]})
            f2.config = f26

        elif int(f7) == 0:
            f27 = f11.read_text()
            f28 = json.loads(f27)
            f28.update({'_': [2,1]})
            self.app.stores = f28
            f2.config = f28
