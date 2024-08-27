from .utils import read_md, is_markdown_file
from .freeze_item import FreezeItem
import os

class Freeze:
    def __init__(self, path) -> None:
        self.path = path
        self.metadata = self._get_metadata()

    def _get_metadata(self):
        file_read = read_md(os.path.join(self.path, "metadata.md"))
        return file_read["yaml"]
    
    def iter(self, func):
        for root, dirs, files in os.walk(os.path.join(self.path, "content")):
            root_parts = os.path.relpath(root, os.path.join(self.path, "content")).split(os.sep)
            
            for file in files:
                if is_markdown_file(os.path.join(root, file)):
                    freeze_item = FreezeItem(os.path.join(root, file), root_parts)
                    func(freeze_item)