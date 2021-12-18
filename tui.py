import converter
import py_cui
import py_cui.keys
import py_cui.widgets

root = py_cui.PyCUI(2, 3)


def help_popup():
    root.show_menu_popup(
        "aide",
        [
            "pour quitter appuyez sur 'q' ",
            "pour naviguer entre les widgets/menus appuyez sur les touches directionnelles ou la souris",
            "pour pouvoir éditer un widget appuyez sur 'enter'",
            "si vous le voulez vous pouvez directement utiliser la souris pour sélectionner et editer un champ",
            "pour quitter le mode édition d'un widget appuyez sur 'escape'",
        ],
        lambda s: s,
    )


root.set_status_bar_text("appuyez sur 'h' pour avoir de l'aide")


def input_box_init(box: py_cui.widgets.TextBox) -> py_cui.widgets.TextBox:
    box.add_mouse_command(py_cui.keys.LEFT_MOUSE_CLICK, lambda: root.move_focus(box))
    return box


box = input_box_init(root.add_text_box("base 10", 1, 0))
hex_box = input_box_init(root.add_text_box("hex", 1, 1))
bin_box = input_box_init(root.add_text_box("binary", 1, 2))

root.add_key_command(py_cui.keys.KEY_H_LOWER, help_popup)

root.set_refresh_timeout(0.1)


def get_box_value(cur):
    if cur == bin_box:
        return converter.val_from_bin(cur.get())
    if cur == hex_box:
        return converter.val_from_hex(cur.get())
    if cur == box:
        return converter.val_from_dec(cur.get())


def update_other_box(cur):
    val = get_box_value(cur)

    if cur != bin_box:
        bin_box.set_text(converter.val_to_bin(val))
    if cur != hex_box:
        hex_box.set_text(converter.val_to_hex(val))
    if cur != box:
        box.set_text(converter.val_to_dec(val))


def tui_update():
    widg = root.get_selected_widget()
    if isinstance(widg, py_cui.widgets.TextBox):
        val = widg.get()
        update_other_box(widg)


root.set_on_draw_update_func(tui_update)


def tui_run():
    root.start()
