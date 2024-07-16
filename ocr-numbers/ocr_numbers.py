number_code_mapping = {
    (" _ ", "| |", "|_|", "   "): 0,
    ("   ", "  |", "  |", "   "): 1,
    (" _ ", " _|", "|_ ", "   "): 2,
    (" _ ", " _|", " _|", "   "): 3,
    ("   ", "|_|", "  |", "   "): 4,
    (" _ ", "|_ ", " _|", "   "): 5,
    (" _ ", "|_ ", "|_|", "   "): 6,
    (" _ ", "  |", "  |", "   "): 7,
    (" _ ", "|_|", "|_|", "   "): 8,
    (" _ ", "|_|", " _|", "   "): 9
}


def convert(input_grid):
    length = len(input_grid)
    row_length = len(input_grid[0])
    if length % 4 != 0:
        raise ValueError("Number of input lines is not a multiple of four")
    if row_length % 3 != 0:
        raise ValueError("Number of input columns is not a multiple of three")

    result = ""
    number = ""

    for i in range(0, length, 4):  # Process 4 rows at a time
        for j in range(0, row_length, 3):  # Process 3 columns at a time
            output = []
            for k in range(4):
                row = input_grid[i+k][j:j+3]
                output.append(row)

            digit = number_code_mapping.get(tuple(output), "?")
            number += str(digit)

        if number:
            if result:
                result += ","
            result += number
            number = ""

    return result