from textual.reactive import reactive
from textual_image.widget import Image
from textual.app import ComposeResult
from textual.widget import Widget
from PIL import Image as PILImage
from .helpers import hash_table
from pathlib import Path
import base64
import time





class ImageTab(Widget):
    launch_dir = Path.cwd()
    image_pat = Path(__file__).parent.parent / "Fontend"
    image_outs = image_pat / "model.png"
    config: reactive[tuple] = reactive(tuple, init=False)

    def __init__(self):
        super().__init__()

    async def watch_config(self, value: tuple):

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

        if prefix == 0:
            TIME_STAMP = int(time.time())
            image_outs_ = self.launch_dir / f"{TIME_STAMP}.png"
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
            img = PILImage.open(self.image_outs)
            img_ratio = img.width / img.height
            container_ratio = target_w / target_h

            if img_ratio > container_ratio:
                self.query_one(Image).styles.width = "100%"
                self.query_one(Image).styles.height = "auto"
            else:
                self.query_one(Image).styles.width = "auto"
                self.query_one(Image).styles.height = "100%"







