from enum import Enum 

class CalValueType(Enum):
    VALUE_BIN = 0
    VALUE_HEX = 1
    VALUE_RAW = 2

class CalValue: 
    val : int
    val_type : CalValueType 
    def __init__(self): 
        self.val = 0
        self.val_type = CalValueType.VALUE_RAW

class GuiBackendType(Enum):
    NONE = 0
    TUI = 1
    GUI = 2
    CONSOLE = 3


class Backend: 
    values = []
    def __init__(self): 
        self.values = [] 
        pass 

    def run(self): 
        pass

    def exit(self):
        pass
