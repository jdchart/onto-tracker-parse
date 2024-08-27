from .utils import read_md

class FreezeItem:
    def __init__(self, path, tree) -> None:
        self.path = path
        self.tree = tree
        
        self.metadata = None
        self.content = None
        self._read_content()

    def _read_content(self):
        file_read = read_md(self.path)
        self.metadata = file_read["yaml"]
        self.content = file_read["markdown"]