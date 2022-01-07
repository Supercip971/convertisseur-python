import tkinter
import converter

root = tkinter.Tk()
root.withdraw()
a = tkinter.Label(root, text="convertisseur python")
a.pack(padx=10, pady=10)

bin_text = tkinter.StringVar(value="0b0")
bin_box = tkinter.Entry(root, textvariable=bin_text)
bin_box.pack(pady=10, padx=10, fill='x')

hex_text = tkinter.StringVar(value="0x0")
hex_box = tkinter.Entry(root, textvariable=hex_text)
hex_box.pack(pady=10, padx=10, fill='x')

dec_text = tkinter.StringVar(value="0")
dec_box = tkinter.Entry(root, textvariable=dec_text)
dec_box.pack(pady=10, padx=10, fill='x')

info_text = tkinter.StringVar(
    value="info: vous pouvez rajouter des arguments \n à la ligne de commande pour changer le type d'interface")
info = tkinter.Label(root, textvariable=b_text)
info.pack(pady=10, padx=10, fill="x")

quit_button = tkinter.Button(root, text="exit", command=root.destroy)
quit_button.pack(pady=10, padx=10, side="bottom")


def get_box_value(cur: tkinter.Entry) -> int:
    if cur == bin_box:
        return converter.val_from_bin(bin_text.get())
    if cur == hex_box:
        return converter.val_from_hex(hex_text.get())
    if cur == dec_box:
        return converter.val_from_dec(dec_text.get())


def update_other_box(cur: tkinter.Entry):
    val = get_box_value(cur)

    if cur != bin_box:
        bin_text.set(converter.val_to_bin(val))
    if cur != hex_box:
        hex_text.set(converter.val_to_hex(val))
    if cur != dec_box:
        dec_text.set(converter.val_to_dec(val))


def gui_update():
    focused = root.focus_get()

    if isinstance(focused, tkinter.Entry):  # on ne fait rien l'utilisateur sélectionne le bouton
        update_other_box(focused)
    root.after(100, gui_update)


def gui_run():
    root.deiconify()
    root.after(100, gui_update)
    root.mainloop()
