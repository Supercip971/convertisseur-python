
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
    for c in (value):
        if c not in str_xdigits or int(str_xdigits.index(c)) >= base:
            return None
        result = result * base + str_xdigits.index(c)

    return result


def val_from_hex(value: str):
    return val_from_str(value.removeprefix("0x"), 16)


def val_from_bin(value: str):
    return val_from_str(value.removeprefix("0b"), 2)


def val_from_raw(value: str):
    return val_from_str(value, 10)
