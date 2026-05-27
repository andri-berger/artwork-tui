from textual.widgets import DirectoryTree
from textual.reactive import reactive
from textual_image.widget import Image
from textual.widgets import DataTable
from textual.widget import Widget
from .script import tui_to_web, web_to_tui
from pathlib import Path
from textual import on
from .scripts import opencv
from .script import testlauf
from textual.app import ComposeResult
import shutil
import base64
import time
import json
import cv2


CWD = Path.cwd()
APP = Path(__file__)
APP_DIR = Path(__file__).parent
ASSETS_DIR = APP_DIR.parent / "Fontend"
ASSETS = ASSETS_DIR / "model.png"
CONFIGS = ASSETS_DIR / "model.json"

class ImageTab(Widget):
    config: reactive[dict] = reactive(dict, init=False)

    def compose(self) -> ComposeResult:
        yield Image()

    async def watch_config(self, value: dict):
        f0 = self.app.query_one("#cont-switch-1")
        f1 = int(f0.current.split("-")[-1])
        f2 = self.app.query(DataTable)
        f3 = self.app.stores
        f4 = self.app.store
        f5 = self.app.page
        f6,f7 = value.pop("_", [])
        f8 = tui_to_web(value,f4) or {}
        f9 = [9, 100, 301, 300, 6, 6]
        f10 = f8.get('0', {})
        self.query_one(
            Image).remove()
        self.notify(
            f"{f7} - {f8}")

        if f6 >= 1:
            with self.app.batch_update():
                f2[f1].clear(columns=False)
                f07 = self.app.store[f"1-{f1}"]
                for row_i in range(len(f07)):
                    row = [f07[row_i][0]]
                    row.extend([""]*f9[f1])
                    f2[f1].add_row(*row)

        if f7 >= 0:
            f11 = await (
                f5.evaluate(
                f4['4-2'][3],[f7,f8]))
            b64 = f11[0].split(',')[1]
            f12 = base64.b64decode(b64)

            if f10.get('80',0) in range(1,5):
                f20 = { "set": f10.get('80',0),
                    "set0": f10.get('81',0),
                    "set1": f10.get('82',0),
                    "set2": f10.get('83',0),
                    "set3": f10.get('83',0)}
                f12 = opencv(f12,f20)

        if f7 == 4:
            f25 = int(time.time())
            f26 = CWD / f"{f25}.png"
            with open(f26, "wb") as f:
                f.write(f12)

        if f7 <= 3:
            with open(ASSETS, "wb") as f:
                f.write(f12)
            self.mount(Image(ASSETS))
            testlauf(self,ASSETS,Image,cv2)

        if f7 == 2:
            here = web_to_tui(f11[1], f4)
            f3 = {**f3, **here}

        if f6 >= 1:
            ss = [0,6] if f6 == 2 else [1,4]
            with self.app.batch_update():
                for i in range(*ss):
                    uv = int(i) == 3
                    st = 2 if uv else i
                    f7 = f4[f"1-{st}"]
                    test = f3.get(str(i),{})
                    if test is not None:
                        f2[i].clear(columns=False)
                        cols = [str(col_i) for
                                col_i in range(f9[i])]
                        for row_i in range(len(f7)):
                            row_key = str(row_i)
                            yes = test.get(row_key)
                            row = [f7[row_i][0]]
                            if yes is not None:
                                for f1 in cols:
                                    row.append(
                                    str(yes.get(f1,"")))
                            f2[i].add_row(*row)

        CONFIGS.write_text(
        json.dumps(f3))

    def render(self):
        return ""


class FileTypeTree(DirectoryTree):
    show_root = False

    def __init__(self, path, file_type: str, **kwargs):
        self.file_type = file_type
        super().__init__(path, **kwargs)
        self.store = self.app.store["4-2"][0]

    def on_mount(self):
        self.e_images = self.app.query_one(ImageTab)

    def filter_paths(self, paths):
        return [p for p in paths if not p.name.startswith(".") and self._is_allowed(p)]

    def _is_allowed(self, p):
        if p.is_dir():
            return True  # always show dirs for navigation

        match self.file_type:
            case "image":
                return p.suffix.lower() == ".png"
            case "font":
                return p.suffix.lower() == ".otf"
            case "json":
                return p.suffix.lower() == ".json"
        return False


    @on(DirectoryTree.FileSelected)
    async def selected(self, event: DirectoryTree.FileSelected) -> None:
        f0 = event.path
        f1 = self.app.stores
        f2 = int(time.time())
        f4 = event.control.id
        f5 = f4.split("-")[-1]
        f6 = ["module","modules"]
        f7 = ['4','5'][int(f5)-1]
        f8 = ['6','6'][int(f5)-1]
        f9 = f6[int(f5)-1]
        if not f0.is_file():
            return

        for f in ASSETS_DIR.glob("*.png"):
            if f.name != "model.png"\
                    and f.name != f0.name:
                f.unlink()

        for f in ASSETS_DIR.glob("*.otf"):
            if f.name != "model.otf"\
                    and f.name != f0.name:
                f.unlink()

        if f4 == "dir-tree-0":
            f20 = "model.json"
            f21 = ASSETS_DIR / f20
            shutil.copy2(f0, f21)
            f22 = f0.read_text()
            f36 = json.loads(f22)
            f36.update({'_': [2,1]})
            self.app.stores = f36
            self.e_images.config = f36
            await self.reload()

        elif (f4 == "dir-tree-1"
              or f4 == "dir-tree-2"):
                f30 = f0.suffix
                f31 = f"{f2}{f30}"
                f33 = ASSETS_DIR / f9 / f31
                f34 = f1.setdefault(f7, {})
                f35 = f34.setdefault('0', {})
                shutil.copy2(f0, f33)
                f35[f8] = f"{f2}"
                f36 = {**self.app.stores}
                f36.update({'_': [0,1]})
                self.e_images.config = f36
                self.notify(
                self.store.format(src=f0))
                await self.reload()

                # f40 = self.app.query_one("#cont-switch-1")
                # f41 = self.app.query_one(f"#{f40.current}")
                # f41.focus()

# filepicker full functionality (full cycle)
# export functionality (within 0-prefix)


