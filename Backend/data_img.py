from textual.reactive import reactive
from textual_image.widget import Image
from textual.app import ComposeResult
from textual.widget import Widget
from PIL import Image as PILImage
from pathlib import Path
from textual.css.query import NoMatches
from textual.css.query import NoMatches
from textual.geometry import Size
import base64
import time
import io




class ImageTab(Widget):
    launch_dir = Path.cwd()
    TIME_STAMP = int(time.time())
    image_pat = Path(__file__).parent.parent / "Fontend"
    image_outs = Path.cwd() / f"{TIME_STAMP}.png"
    image_outs_ = Path.cwd() / f"_{TIME_STAMP}.png"
    image_path = image_pat / "image.png"
    time_stamp = reactive(image_outs)
    config = reactive([], init=False)



    def __init__(self):
        super().__init__()
        self.setup = self.app.config['30']
        self.link = self.app.config['31']
        self.alt = self.app.config['90']


    async def watch_config(self):
        # my_dict = {}
        # result = {}
        # for row in self.config:
        #     for cell in row:
        #         result = my_dict[cell]

        try:
            self.query_one(Image).remove()
        except Exception:
            pass
        configs = {"1": self.config}
        config_ = [5,[0,0],configs]
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



