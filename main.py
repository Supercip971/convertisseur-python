import sys
import backend


def arg_help():
    print("convpy con : use a console")
    print("convpy tui : use a text user interface")
    print("convpy gui : use a graphical user interface")


def arg_update(argv_list):
    if(len(sys.argv) != 2):
        print("usage: convpy [action]")
        print("you can do 'convpy help' for help")
        print("it will defaultr as a gui")
        return backend.GuiBackendType.from_str("gui")

    arg = argv_list[1]

    if arg == "help":
        arg_help()
        sys.exit(0)

    gui_type = backend.GuiBackendType.from_str(arg)

    if (gui_type == backend.GuiBackendType.NONE):
        print("argument: ", arg, "is not handled")
        sys.exit(-1)

    return gui_type


def main():
    gui_backend_type = arg_update(sys.argv)
    backend.run_backend(gui_backend_type)


if __name__ == "__main__":
    main()
