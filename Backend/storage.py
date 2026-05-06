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