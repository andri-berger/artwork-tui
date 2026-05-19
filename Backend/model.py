from textual.widgets import (DirectoryTree)
from textual.reactive import reactive
from textual_image.widget import Image
from textual.widgets import DataTable
from textual.widget import Widget
from .script import tui_to_web, web_to_tui
from pathlib import Path
from textual import on
from .scripts import opencv
from .script import testlauf
import shutil
import base64
import time
import json
import cv2

from dataclasses import dataclass

@dataclass
class ConfigPayload:
    prefix: int
    data: dict


CWD = Path.cwd()
APP = Path(__file__)
APP_DIR = Path(__file__).parent
ASSETS_DIR = APP_DIR.parent / "Fontend"
image_outs = ASSETS_DIR / "model.png"
CONFIGS = ASSETS_DIR / "model.json"

class ImageTab(Widget):
    #config: reactive[tuple] = reactive(tuple, init=False)
    config: reactive[ConfigPayload | None] = reactive(None, init=False)


    async def watch_config(self, value: tuple):
        f0 = self.app.query(DataTable)
        f2 = self.app.stores
        f1 = self.app.store
        page = self.app.page
        f3, f4 = value
        f5 = tui_to_web(f4,f1)
        f6 = [None, 100, 301]
        self.notify(f"how many times {value}")


        if f3 == 2:
            with self.app.batch_update():
                for i in range(1,2):
                    f0[i].clear(columns=False)
                    f7 = self.app.store[f"1-{i}"]
                    for row_i in range(len(f7)):
                        row = [f7[row_i][0]]
                        row.extend([""]*f6[i])
                        f0[i].add_row(*row)



        # unclear !!!
        try:
            if f3 >= 1:
                self.query_one(Image).remove()
        except Exception:
            pass


        f10 = await (
            page.evaluate(
            f1['4-2'][3],[f3,f5]))
        b64 = f10[0].split(',')[1]
        f11 = base64.b64decode(b64)
        f12 = f5.get('0',{})



        if (any(str(k) in f12.keys()
               for k in range(80,84))):

            settings = {
                "set": f12.get('80',0),
                "set0": f12.get('81',0),
                "set1": f12.get('82',0),
                "set2": f12.get('83',0),
                "set3": f12.get('83',0) }
            f11 = opencv(
                f11,settings)

        if f3 == 0:
            time_stamp = int(time.time())
            image_outs_ = CWD / f"{time_stamp}.png"
            with open(image_outs_, "wb") as f:
                f.write(f11)

        if f3 >= 1:
            with open(image_outs, "wb") as f:
                f.write(f11)


        if not self.is_mounted:
            return

        if f3 >= 1:
            self.mount(Image(image_outs))
            testlauf(self, image_outs, Image, cv2)


        # raus !!!
        if any(f10[1]):
            l0 = f2.setdefault('0', {})
            l1 = l0.setdefault('38', {})
            if f10[1][0] is not None:
                l1['0'] = f10[1][0]
            if f10[1][1] is not None:
                l1['1'] = f10[1][1]
            if f10[1][2] is not None:
                l1['2'] = f10[1][2]



        if f3 == 2:
            f1['00'] = web_to_tui(f10[2], f1)
            with self.app.batch_update():
                for i in range(1,2):
                    f7 = f1[f"1-{i}"]
                    test = f1['00'].get(str(i))
                    f0[i].clear(columns=False)
                    cols = [str(col_i) for
                            col_i in range(f6[i])]
                    for row_i in range(len(f7)):
                        row_key = str(row_i)
                        yes = test.get(row_key, {})
                        row = [f7[row_i][0]]
                        for col in cols:
                            row.append(
                            str(yes.get(col,"")))
                        f0[i].add_row(*row)

            merged = {**f2, **f1['00']}
            CONFIGS.write_text(
            json.dumps(merged))


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
            yeah = "model.json"
            data = json.loads(src.read_text())
            shutil.copy2(src, ASSETS_DIR / yeah)
            self.e_images.config = (1,data)
            self.e_images.mutate_reactive(
                ImageTab.config)

        if int(spl) >= 1:
            dest = f"{stamps}{src.suffix}"
            dest_dir = ASSETS_DIR / dest
            shutil.copy2(src, dest_dir)
            await self.reload()
            self.app.stores[sps] = stamps
            self.notify(
            self.store.format(src=src))
            self.e_images.config = \
                (1,self.app.stores)
            self.e_images.mutate_reactive(
                ImageTab.config)


