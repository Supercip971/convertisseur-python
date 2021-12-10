str_xdigits = ["0", "1", "2", "3", "4", "5", "6",
               "7", "8", "9", "a", "b", "c", "d", "e", "f"]


def convert_digit(value, base):
    return str_xdigits[value % base]


def convert_to_val(value, base):
    if value == None:
        return "Error"

    current: int = int(value)
    result: str = ""

    while current != 0:
        result = result + convert_digit(current, base)
        current = current // base

    if len(result) == 0:
        return "0"

    return result[::-1]  # reverse string


def val_to_hex(value):
    return "0x" + convert_to_val(value, 16)


def val_to_bin(value):
    return "0b" + convert_to_val(value, 2)


def val_to_raw(value):
    return convert_to_val(value, 10)


def val_from_str(value, base):
    value = value.lower()
    result: int = 0
    # pour chaque caractère de la valeur (de gauche a droite) on prend le résultat, on le mutliplie par la base, puis on rajoute la valeur currente.
    # donc si on a "544" on aura: (avec une base de 10)
    # 5
    # 5 * 10 + 4
    # (5 * 10 + 4) * 10 + 4 = 544
    for c in (value):
        # on vérifie si le caractère est une bonne valeur et qu'il fait partie de la base donnée
        if c not in str_xdigits or int(str_xdigits.index(c)) >= base:
            return None
        # donc on "pousse" le résultat vers la gauche puis on rajoute le chiffre
        # (quand on dit pousse c'est qu'on multiplie la valeur par la base, par exemple 0xf -> 0xf0; 0b10 -> 0b100)
        result = result * base + str_xdigits.index(c)

    return result


def val_from_hex(value: str):
    return val_from_str(value.removeprefix("0x"), 16)


def val_from_bin(value: str):
    return val_from_str(value.removeprefix("0b"), 2)


def val_from_raw(value: str):
    return val_from_str(value, 10)
