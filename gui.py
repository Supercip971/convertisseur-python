import tkinter
import os
import sys
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
info = tkinter.Label(root, textvariable=info_text)
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

    # on ne fait rien l'utilisateur sélectionne le bouton
    if isinstance(focused, tkinter.Entry):
        update_other_box(focused)
    root.after(100, gui_update)

# le fichier d'icon est différent si on est dans l'executable ou dans python
# si c'est un executable c'est directement 
def gui_get_icon():
    if getattr(sys, 'frozen', False):
        return tkinter.PhotoImage(file=os.path.join(sys._MEIPASS, "./resources/icon.png"))
    else:
        return tkinter.PhotoImage(file="./resources/icon.png")


def gui_run():
    root.deiconify()
    # met l'icone à cette fenêtre et à toute les fenêtre enfants
    root.iconphoto(True, gui_get_icon())

    root.after(100, gui_update)
    root.mainloop()
