str_xdigits = [
    "0",
    "1",
    "2",
    "3",
    "4",
    "5",
    "6",
    "7",
    "8",
    "9",
    "a",
    "b",
    "c",
    "d",
    "e",
    "f",
]


def convert_digit(value: int, base: int) -> str:
    return str_xdigits[value % base]


def convert_to_val(value: int, base: int) -> str:
    if value == None:
        return "Error"

    current = int(value)
    result = ""

    while current != 0:
        result = result + convert_digit(current, base)
        current = current // base

    if len(result) == 0:
        return "0"

    return result[::-1]  # reverse string


def val_to_hex(value: int) -> str:
    return "0x" + convert_to_val(value, 16)


def val_to_bin(value: int) -> str:
    return "0b" + convert_to_val(value, 2)


def val_to_dec(value: int) -> str:
    return convert_to_val(value, 10)


def val_from_str(value: str, base: int) -> int:
    value = value.lower()
    result = 0

    for c in value:
        if c not in str_xdigits or int(str_xdigits.index(c)) >= base:
            return None

        result = result * base + str_xdigits.index(c)

    return result


def val_from_hex(value: str) -> int:
    return val_from_str(value.removeprefix("0x"), 16)


def val_from_bin(value: str) -> int:
    return val_from_str(value.removeprefix("0b"), 2)


def val_from_dec(value: str) -> int:
    return val_from_str(value, 10)
