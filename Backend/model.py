from textual.widgets import (DirectoryTree)
from textual.reactive import reactive
from textual_image.widget import Image
from textual.widget import Widget
from .script import hash_table
from pathlib import Path
from textual import on
from .style import opencv
import shutil
import base64
import time
import json
import cv2


CWD = Path.cwd()
APP = Path(__file__)
APP_DIR = Path(__file__).parent
ASSETS_DIR = APP_DIR.parent / "Fontend"


class ImageTab(Widget):
    image_outs = ASSETS_DIR / "model.png"
    config: reactive[tuple] = reactive(tuple, init=False)

    def __init__(self):
        super().__init__()

    async def watch_config(self, value: tuple):
        self.notify("will-it")
        rot = self.app.store
        prefix, start = value
        starts = start.items()
        d_transformed = hash_table(
            starts,rot)
        try:
            if prefix >= 1:
                self.query_one(Image).remove()
        except Exception:
            pass

        self.notify(f"{prefix}")
        self.notify(f"{self.app.helpful}")
        self.notify(f"{d_transformed}")
        config_ = [prefix,
                   self.app.helpful,
                   d_transformed]
        page = self.app.page
        data_url = await (
            page.evaluate(
            "async (store) => window.testlaufs(store)",config_))

        for i in data_url[1]:
            self.app.helpful[i] = data_url[1][i]
        b64 = data_url[0].split(',')[1]
        img_bytes = base64.b64decode(b64)

        # settings = {
        #     "setting": 1,
        #     "setting0": 0,
        #     "setting1": 0,
        #     "setting2": 0}
        # img_bytes = opencv(img_bytes,settings)
        # img_bytes = vignette(img_bytes)

        if prefix == 0:
            time_stamp = int(time.time())
            image_outs_ = CWD / f"{time_stamp}.png"
            with open(image_outs_, "wb") as f:
                f.write(img_bytes)

        if prefix >= 1:
            with open(self.image_outs, "wb") as f:
                f.write(img_bytes)


        if not self.is_mounted:
            return

        if prefix >= 1:
            self.mount(Image(self.image_outs))

            size = self.size
            cell_w, cell_h = 9, 18
            target_w = size.width * cell_w
            target_h = size.height * cell_h
            container_ratio = target_w / target_h

            img = cv2.imread(str(self.image_outs))
            height, width = img.shape[:2]
            img_ratio = width / height


            if img_ratio > container_ratio:
                self.query_one(Image).styles.width = "100%"
                self.query_one(Image).styles.height = "auto"
            else:
                self.query_one(Image).styles.width = "auto"
                self.query_one(Image).styles.height = "100%"

        # if prefix == 2:
        #   CONFIGS.write_text(
        #   json.dumps(self.app.stores))





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
        sps = str(int(spl)+3)
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
            self.app.helpful[sps] = stamps
            self.notify(
            self.store.format(src=src))
            self.e_images.config = \
                (1,self.app.stores)
            self.e_images.mutate_reactive(
                ImageTab.config)


