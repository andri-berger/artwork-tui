from textual.reactive import reactive
from textual_image.widget import Image
from textual.app import ComposeResult
from textual.widget import Widget
from PIL import Image as PILImage
from pathlib import Path
import base64
import time


class ImageTab(Widget):
    image_pat = Path(__file__).parent.parent / "Asset"
    image_outs = image_pat / "outputs.png"
    image_path = image_pat / "image.png"
    time_stamp = reactive(image_outs)
    config = reactive([], init=False)

    def __init__(self):
        super().__init__()
        self.setup = self.app.config['30']
        self.link = self.app.config['31']
        self.alt = self.app.config['90']

    # def compose(self) -> ComposeResult:
    #     yield Image(self.image_path)

    def compose(self) -> ComposeResult:
        img = PILImage.open(self.image_path)
        img.thumbnail((600, 800))
        yield Image(img)

    async def watch_config(self):
        self.query_one(Image).remove()
        configs = {"1": self.config}
        config_ = [3,[0,0],configs]
        page = self.app.page
        data_url = await (page.evaluate(
            self.setup,config_))
        int(time.time())
        b64 = data_url.split(',')[1]
        img_bytes = base64.b64decode(b64)
        with open(self.image_outs, "wb") as f:
            f.write(img_bytes)
        self.time_stamp = int(time.time())

    def watch_time_stamp(self):
        if not self.is_mounted:
            return
        self.notify('yes!!')
        self.mount(Image(self.image_outs))