import sys
import backend
from tui import Tui 

def arg_help():
    print("convpy con : use a console")
    print("convpy tui : use a text user interface")
    print("convpy gui : use a graphical user interface")

def get_backend(type: backend.GuiBackendType) -> backend.Backend:
    if(type == backend.GuiBackendType.TUI): 
        return Tui()
    else: 
        return backend.Backend() 

def arg_update(argv_list):
    if(len(sys.argv) != 2):
        print("usage: convpy [action]")
        print("you can do 'convpy help' for help")
        exit()

    arg = argv_list[1]
    if arg == "help":
        arg_help() 
    elif arg == "gui":
        return backend.GuiBackendType.GUI
    elif arg == "tui": 
        return backend.GuiBackendType.TUI
    elif arg == "con":
        return backend.GuiBackendType.CONSOLE
    else: 
        print("argument: ", arg, "is not handled")

    exit()

def main():
    gui_backend_type = arg_update(sys.argv)  
    gui_backend = get_backend(gui_backend_type)
    gui_backend.run()

    
if __name__ == "__main__":
    main()
    