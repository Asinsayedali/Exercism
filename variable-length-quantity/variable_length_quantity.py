EIGHT_BIT_MASK = 1 << 7
SEVEN_BIT_MASK = EIGHT_BIT_MASK - 1

def encode_single(number: int) -> list[int]:
    byte_string = [number & SEVEN_BIT_MASK]
    while number := number >> 7:
        byte_string.append(number & SEVEN_BIT_MASK | EIGHT_BIT_MASK)
    return byte_string[::-1]


def encode(numbers: list[int]) -> list[int]:
    return [byte for number in numbers for byte in encode_single(number)]


def decode(bytes_string: list[int]) -> list[int]:
    original_value: list[int] = []
    number = 0

    for index, byte in enumerate(bytes_string):
        number <<= 7
        number += byte & SEVEN_BIT_MASK

        if not byte & EIGHT_BIT_MASK:
            original_value.append(number)
            number = 0
        elif index == len(bytes_string) - 1:
            raise ValueError("incomplete sequence")
    return original_value
