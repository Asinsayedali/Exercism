seven_bit_mask = 0x7f
eight_bit_mask = 0x80


def encode_single(number):
    byte_string = [number & seven_bit_mask]
    number >>= 7
    while number > 0:
        byte_string.append(number & seven_bit_mask | eight_bit_mask)
        number >>= 7
    return byte_string[::-1]


def encode(numbers):
    return [byte for number in numbers for byte in encode_single(number)]


def decode(bytes_string):
    orginal_value = []
    number = 0

    for index, byte in enumerate(bytes_string):
        number <<= 7
        number = number + (byte & seven_bit_mask)

        if byte & eight_bit_mask == 0:
            orginal_value.append(number)
            number = 0
        elif index == len(bytes_string) - 1:
            raise ValueError("incomplete sequence")
    return orginal_value

