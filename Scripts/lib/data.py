import threading
import time
from enum import Enum, auto

class SubWindowType(Enum):
    SearchDirWin = auto()
    SearchNameWin = auto()
    SearchDiffWin = auto()

class SubWindowData:
    def __init__(self, _type, _window):
        self.window = _window
        self.type = _type
    
    def GetWindowType(self):
        return self.type
    
    def GetWindow(self):
        return self.window


class SubWindowManager:

    _instance_lock = threading.Lock()
    def __new__(cls, *args, **kwargs):
        time.sleep(1)
        if not hasattr(cls, "_instance"):
            with cls._instance_lock:
                if not hasattr(cls, "_instance"):
                    cls._instance = object.__new__(cls)
        return cls._instance

    def __init__(self):
        self.allSubWindowList = {}


    def GetSubWindow(self, _mdiId):
        if _mdiId in self.allSubWindowList:
            return self.allSubWindowList.get(_mdiId)
        else:
            return None
    

    def RegisterSubWindow(self, _mdiId, _subWindow):
        self.allSubWindowList.update({_mdiId : _subWindow})
        #print(self.allSubWindowList)


    def RemoveSubWindow(self, _mdiId):
        self.allSubWindowList.pop(_mdiId)
        #print(self.allSubWindowList)
