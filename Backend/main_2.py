from textual.widgets import (DirectoryTree)
from .main_1 import ImageTab
from pathlib import Path
from textual import on
import shutil
import time



CWD = Path.cwd()
APP = Path(__file__)
APP_DIR = Path(__file__).parent
ASSETS_DIR = APP_DIR.parent / "Fontend"


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


