from textual.widgets import (DirectoryTree)
import mimetypes

class FileTypeTree(DirectoryTree):
    show_root = False
    def __init__(self, path, file_type: str, **kwargs):
        self.file_type = file_type
        super().__init__(path, **kwargs)

    def filter_paths(self, paths):
        return [p for p in paths if not p.name.startswith(".") and self._is_allowed(p)]

    def _is_allowed(self, p):
        if p.is_dir():
            return True  # always show dirs for navigation

        mime, _ = mimetypes.guess_type(p.name)
        category = mime.split("/")[0] if mime else None
        FONT_EXTENSIONS = {".otf", ".ttf", ".woff", ".woff2", ".eot"}

        match self.file_type:
            case "image":
                return category == "image"
            case "font":
                return p.suffix.lower() in FONT_EXTENSIONS
            case "json":
                return p.suffix.lower() == ".json"
        return False