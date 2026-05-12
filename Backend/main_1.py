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
    config: reactive[dict] = reactive(dict, init=False)

    def compose(self) -> ComposeResult:
        yield Image(self.image_path)

    def __init__(self):
        super().__init__()
        self.setup = "async (config) => window.testlaufs(config)",
        self.link = "http://localhost:9000/model.html"

    async def watch_config(self):
        transformed_dict = {}
        for row_i, row in self.config.items():
            transformed_dict[row_i] = {}
            shot = self.app.config[f"5-{row_i}"]
            for col_i, col in row.items():
                for cell_i, cell in col.items():
                    tt = transformed_dict[row_i]
                    sht = str(shot[int(col_i)])
                    if row_i == '0':
                        tt[sht[int(cell_i)]] = cell
                    if row_i == '1':
                        if sht not in tt:
                            tt[sht] = {}
                        tt[sht][cell_i] = cell
                    if row_i == '2':
                        if cell_i not in tt:
                            tt[cell_i] = {}
                        tt[cell_i][sht] = cell

        self.notify(f"{transformed_dict}")

        try:
            self.query_one(Image).remove()
        except Exception:
            pass
        config_ = [5,[0,0],self.config]
        self.notify(f"{self.setup}")
        page = self.app.page
        data_url = await (
            page.evaluate(
            "async (config) => window.testlaufs(config)",config_))

        b64 = data_url.split(',')[1]
        img_bytes = base64.b64decode(b64)
        with open(self.image_outs, "wb") as f:
            f.write(img_bytes)

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







