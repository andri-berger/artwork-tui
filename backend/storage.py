# SPDX-License-Identifier: AGPL-3.0-or-later
# SPDX-FileCopyrightText: 2024 Andri Berger
#
# This file is part of layout-tui.
#
# layout-tui is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

import json
  from pathlib import Path
  from platformdirs import user_data_dir

  STATE_FILE = Path(user_data_dir("layoutgen")) / "state.json"

  # on exit — dump DataTable
  def save_state(self) -> None:
      table = self.query_one(DataTable)
      data = self.get_all_data(table)
      STATE_FILE.parent.mkdir(parents=True, exist_ok=True)
      STATE_FILE.write_text(json.dumps(data, indent=2))

  # on launch — restore DataTable
  def load_state(self) -> dict:
      if STATE_FILE.exists():
          return json.loads(STATE_FILE.read_text())
      return {}

  class CLIApp(App):
      async def on_mount(self) -> None:
          data = load_state()
          table = self.query_one(DataTable)
          for row in data.values():
              table.add_row(*row.values())

      async def on_unmount(self) -> None:
          save_state(self)