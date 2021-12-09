import sys
import backend
import tui
import gui


def arg_help():
    print("convpy con : use a console")
    print("convpy tui : use a text user interface")
    print("convpy gui : use a graphical user interface")


def run_backend(type: backend.GuiBackendType):
    if(type == backend.GuiBackendType.TUI):
        return tui.tui_run()
    if(type == backend.GuiBackendType.GUI):
        return gui.gui_run()
    else:
        return 0


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
    gui_backend = run_backend(gui_backend_type)


if __name__ == "__main__":
    main()
