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
image_outs = ASSETS_DIR / "model.png"
CONFIGS = ASSETS_DIR / "model.json"
CONFIGS_ = ASSETS_DIR / "models.json"
CONFIGS0_ = ASSETS_DIR / "models-.json"

class ImageTab(Widget):
    config: reactive[dict] = reactive(dict, init=False)

    def compose(self) -> ComposeResult:
        yield Image()

    async def watch_config(self, value: dict):
        cool = self.app.query_one("#cont-switch-1")
        col = int(cool.current.split("-")[-1])
        f0 = self.app.query(DataTable)
        f2 = self.app.stores
        f1 = self.app.store
        f3 = self.app.page
        f4,f04 = value.pop("_", [])
        f5 = tui_to_web(value,f1) or {}
        f6 = [9, 100, 301, 300, 6, 6]
        self.query_one(
            Image).remove()
        self.notify(
            f"{f04} - {f5}")

        if f4 >= 1:
            with self.app.batch_update():
                f0[col].clear(columns=False)
                f7 = self.app.store[f"1-{col}"]
                for row_i in range(len(f7)):
                    row = [f7[row_i][0]]
                    row.extend([""]*f6[col])
                    f0[col].add_row(*row)

        if f04 >= 0:
            f10 = await (
                f3.evaluate(
                f1['4-2'][3],[f04,f5]))
            b64 = f10[0].split(',')[1]
            f11 = base64.b64decode(b64)
            self.notify('done!!!')

        if f04 == 0:
            time_stamp = int(time.time())
            image_outs_ = CWD / f"{time_stamp}.png"
            with open(image_outs_, "wb") as f:
                f.write(f11)

        if f04 >= 1:
            with open(image_outs, "wb") as f:
                f.write(f11)
            self.mount(Image(image_outs))
            testlauf(self, image_outs, Image, cv2)

        if f04 == 3:
            here = web_to_tui(f10[1], f1)
            f2 = {**f2, **here}

        if f4 >= 1:
            ss = [0,6] if f4 == 2 else [1,4]
            with self.app.batch_update():
                for i in range(*ss):
                    uv = int(i) == 3
                    st = 2 if uv else i
                    f7 = f1[f"1-{st}"]
                    test = f2.get(str(i),{})
                    if test is not None:
                        f0[i].clear(columns=False)
                        cols = [str(col_i) for
                                col_i in range(f6[i])]
                        for row_i in range(len(f7)):
                            row_key = str(row_i)
                            yes = test.get(row_key)
                            row = [f7[row_i][0]]
                            if yes is not None:
                                for col in cols:
                                    row.append(
                                    str(yes.get(col,"")))
                            f0[i].add_row(*row)

        CONFIGS.write_text(
        json.dumps(f2))

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
        src = event.path
        stamp = int(time.time())
        stamps = str(stamp)[-7:]
        id = event.control.id
        spl = id.split("-")[-1]
        sps = str(int(spl)+145)
        if not src.is_file():
            return

        for f in ASSETS_DIR.glob("*.png"):
            if f.name != "model.png"\
                    and f.name != src.name:
                f.unlink()

        for f in ASSETS_DIR.glob("*.otf"):
            if f.name != "model.otf"\
                    and f.name != src.name:
                f.unlink()

        if int(spl) == 0:
            self.notify('model-0')
            yeah = "model.json"
            dir = ASSETS_DIR / yeah
            shutil.copy2(src, dir)
            cool = src.read_text()
            l20 = json.loads(cool)
            l20.update({'_': [2,2]})
            self.app.stores = l20
            self.e_images.config = l20

        if int(spl) >= 1:
            self.notify('model-1')
            dest = f"{stamps}{src.suffix}"
            dest_dir = ASSETS_DIR / dest
            shutil.copy2(src, dest_dir)
            await self.reload()
            self.app.stores[sps] = stamps
            l20 = {**self.app.stores}
            l20.update({'_': [0,2]})
            self.e_images.config = l20
            self.notify(
            self.store.format(src=src))

            # f12 = f5.get('0',{})
        # if (any(str(k) in f12.keys()
        #        for k in range(80,84))):
        #     settings = {
        #         "set": f12.get('80',0),
        #         "set0": f12.get('81',0),
        #         "set1": f12.get('82',0),
        #         "set2": f12.get('83',0),
        #         "set3": f12.get('83',0) }
        #     f11 = opencv(
        #         f11,settings)

        # raus !!!
        # if any(f10[1]):
        #     l0 = f2.setdefault('0', {})
        #     l1 = l0.setdefault('38', {})
        #     if f10[1][0] is not None:
        #         l1['0'] = f10[1][0]
        #     if f10[1][1] is not None:
        #         l1['1'] = f10[1][1]
        #     if f10[1][2] is not None:
        #         l1['2'] = f10[1][2]