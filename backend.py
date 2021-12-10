from enum import Enum
import tui
import console
import gui


class GuiBackendType(Enum):
    NONE = 0
    TUI = 1
    GUI = 2
    CONSOLE = 3

    def from_str(string: str) -> int:
        if (string == "tui"):
            return GuiBackendType.TUI
        elif (string == "gui"):
            return GuiBackendType.GUI
        elif (string == "con"):
            return GuiBackendType.CONSOLE

        return GuiBackendType.NONE


def run_backend(type: GuiBackendType):
    if(type == GuiBackendType.TUI):
        return tui.tui_run()
    elif(type == GuiBackendType.CONSOLE):
        return console.console_run()
    elif(type == GuiBackendType.GUI):
        return gui.gui_run()
    else:
        return 0
