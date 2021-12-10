import converter


def console_error_check(val: int, inputed_val: str, action: str):
    if val == None:
        print("erreur: l'action'", action,
              "' ne peut pas utiliser la valeur '", inputed_val, "'")
        exit()


input_message = "tappez: 'x' pour hexadécimal, 'd' pour décimal, 'b' pour binaire, 'q' pour quitter: (x/d/b/q):"


def console_run():
    while True:
        action = input(input_message)

        if not action in "xdbq":
            print("action invalide:", action)
            continue

        if action == 'q':
            exit()

        val = input("entez une valeur: ")
        converted_val = 0

        if action == 'b':
            converted_val = converter.val_from_bin(val)
        elif action == 'x':
            converted_val = converter.val_from_hex(val)
        else:
            converted_val = converter.val_from_raw(val)

        console_error_check(converted_val, val, action)

        print("valeur décimale:", converter.val_to_raw(converted_val))
        print("valeur hexadécimale:", converter.val_to_hex(converted_val))
        print("valeur binaire:", converter.val_to_bin(converted_val))
