import os
from .freeze import Freeze
from .utils import convert_date

class Vault:
    def __init__(self, path) -> None:
        self.path = path
        self.freezes = self._get_freezes()

    def _get_freezes(self):
        ret = []
        if os.path.isdir(os.path.join(self.path, "freezes")):
            for item in os.listdir(os.path.join(self.path, "freezes")):
                freeze_path = os.path.join(self.path, "freezes", item)
                if os.path.isdir(freeze_path) and os.path.isfile(os.path.join(freeze_path, "metadata.md")):
                    ret.append(Freeze(freeze_path))
            return ret
        else:
            return ret
        
    def get_latest_freeze(self) -> Freeze:
        ret = None
        for freeze in self.freezes:
            if ret == None:
                ret = {"date" : convert_date(freeze.metadata["Freeze date"]), "freeze" : freeze}
            if convert_date(freeze.metadata["Freeze date"]) > ret["date"]:
                ret = {"date" : convert_date(freeze.metadata["Freeze date"]), "freeze" : freeze}
        if ret == None:
            return None
        else:
            return ret["freeze"]
