import base64
import json
import shutil
import time
from pathlib import Path

from textual import on
from textual.app import ComposeResult
from textual.binding import Binding
from textual.reactive import reactive
from textual.widget import Widget
from textual.widgets import DataTable, DirectoryTree
from textual_image.widget import Image

from .script import script_f6, script_f7, script_f8, script_f9
from .scripts import scripts_f1

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
PATH = "async (store) => window.h11(store)"


class MainTab(Widget):
    config: reactive[dict] = reactive(dict, init=False)

    def compose(self) -> ComposeResult:
        yield Image(PATH_7)

    def on_mount(self) -> None:
        f0 = self.query_one(Image)
        f0.styles.width = "auto"
        f0.styles.height = "100%"

    async def watch_config(self, path: dict) -> None:
        f0 = self.app.query_one("#cont-switch-1")
        f1 = int(f0.current.split("-")[-1])
        f2 = [6, 100, 301, 300, 12, 13]
        f3 = self.app.query(DataTable)
        f4 = self.app.playwright
        f5 = self.app.stores
        f6 = self.app.store

        f7 = f5.get("0", {})
        f8 = f7.get("40", {})
        f9, f10 = path.pop("_", [])
        f11 = script_f9(path, f6)
        if self.query_one(Image):
            self.query_one(Image).remove()

        f12 = await f4.evaluate(PATH, [f10, f11])
        f13 = f12[0].split(",")[1]
        f14 = base64.b64decode(f13)
        f15 = f11.get("0", {})
        f16 = f15.get("80", 0)

        if f16 in range(1, 5):
            f17 = {"h": f16, "h0": f15.get("81", 0), "h1": f15.get("82", 0), "h2": f15.get("83", 0)}
            f14 = scripts_f1(f17, f14)

        if f10 == 4:
            f18 = int(time.time())
            f19 = PORT / f"{f18}.png"
            with open(f19, "wb") as f:
                f.write(f14)

        if f10 <= 3:
            with open(PATH_5, "wb") as f:
                f.write(f14)
            await self.mount(Image(PATH_5))
            script_f7(self, PATH_5, Image)

        if f10 == 2:
            f20 = script_f8(f12[1], f6)
            f5 = {**f5, **f20}

        if f9 >= 1:
            f21 = f9 == 2
            f22 = f1 == 3
            f23 = 2 if f22 else f1
            f24 = f6.get(f"1-{f23}")
            f25 = (0, 6) if f21 else (1, 4)
            with self.app.batch_update():
                f3[f23].clear(columns=False)
                for h in range(len(f24)):
                    f26 = [f24[h][0]] or []
                    f26.extend([""] * f2[f23])
                    f3[f23].add_row(*f26)

                for h0 in range(*f25):
                    f27 = int(h0) == 3
                    f28 = 2 if f27 else h0
                    f29 = f6.get(f"1-{f28}")
                    f30 = f5.get(str(h0), {})
                    if f30 is not None:
                        f3[h0].clear(columns=False)
                        f31 = [str(h1) for h1 in range(f2[h0])]
                        for h2 in range(len(f29)):
                            f32 = f30.get(str(h2))
                            f33 = [f29[h2][0]]
                            if f32 is not None:
                                for h3 in f31:
                                    f33.append(str(f32.get(h3, "")))
                            f3[h0].add_row(*f33)

                f34 = f8.get("1", 0)
                f35 = f8.get("2", 0)
                f3[f23].move_cursor(row=f34, column=f35)

        PATH_6.write_text(json.dumps(f5))

    def render(self):
        return ""


class FileTree(DirectoryTree):
    show_root = False
    show_guides = True
    guide_depth = 4
    BINDINGS = [Binding("space", "select_cursor", "Select")]

    def __init__(self, path, file_type, **kwargs) -> None:
        super().__init__(path, **kwargs)
        self.file_type = file_type

    def filter_paths(self, path) -> list:
        f0 = self.file_type
        return [
            h for h in path if (h.is_dir() or f0 == h.suffix.lower()) and not h.name.startswith(".")
        ]

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
        f8 = ["4", "5"][int(f7) - 1]
        f9 = ["module", "modules"]
        f10 = ["png", "otf"]
        f11 = event.path
        f12 = f11.name
        script_f6(self, f5, f12)

        if int(f7) >= 1:
            f13 = f4.column
            f14 = str(f4.row)
            f15 = f9[int(f7) - 1]
            f16 = f10[int(f7) - 1]
            f17 = f12.split(".")
            f18 = PORT_2 / f15
            f19 = f18 / f12

            if int(f3) >= 4 and f13 == 12:
                f20 = f6.setdefault(f8, {})
                f21 = f20.setdefault(f14, {})
                f21[str(f13 - 1)] = f17[0]
                f22 = f1.get_cell_at(f4)
                f23 = f"{str(f22)}.{f16}"
                f24 = f18 / f23 / ""
                if f24.exists():
                    f24.unlink()
                f1.update_cell_at(f4, f17[0])

            elif int(f3) <= 3 or f13 != 12:
                f25 = f6.setdefault("0", {})
                f26 = f25.setdefault("40", {})
                f26[str(int(f7) + 2)] = f12
                if f19.exists():
                    f19.unlink()

            shutil.copy2(f11, f19)
            f27 = {**self.app.stores}
            f27.update({"_": [0, 1]})
            f2.config = f27

        elif int(f7) == 0:
            f28 = f11.read_text()
            f29 = json.loads(f28)
            f29.update({"_": [2, 1]})
            self.app.stores = f29
            f2.config = f29
