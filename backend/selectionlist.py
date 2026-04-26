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
from textual.widgets import Footer, Header, SelectionList


class SelectionListApp(App[None]):
    CSS_PATH = "selectionlist.tcss"

    def compose(self) -> ComposeResult:
        yield Header()
        yield SelectionList[int](
            ("Falken's Maze", 0, True),
            ("Black Jack", 1),
            ("Gin Rummy", 2),
            ("Hearts", 3),
            ("Bridge", 4),
            ("Checkers", 5),
            ("Chess", 6, True),
            ("Poker", 7),
            ("Fighter Combat", 8, True),
        )
        yield Footer()

    def on_mount(self) -> None:
        self.query_one(SelectionList).border_title = "Shall we play some games?"


if __name__ == "__main__":
    SelectionListApp().run()