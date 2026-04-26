# SPDX-License-Identifier: AGPL-3.0-or-later
# SPDX-FileCopyrightText: 2024 Andri Berger
#
# This file is part of layout-tui.
#
# layout-tui is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

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