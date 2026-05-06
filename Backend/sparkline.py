from textual.app import App, ComposeResult
from textual.widgets import Sparkline

data = [1, 2, 2, 1, 1, 4, 3, 1, 1, 8, 8, 2]


class SparklineBasicApp(App[None]):
    CSS_PATH = "sparkline.tcss"

    def compose(self) -> ComposeResult:
        yield Sparkline(
            data,
            summary_function=max,
        )


app = SparklineBasicApp()
if __name__ == "__main__":
    app.run()