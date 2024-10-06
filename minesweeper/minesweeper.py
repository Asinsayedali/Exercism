neighbour = [(-1, -1), (-1, 0), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1), (-1, 1)]


def annotate(minefield):
    if len(minefield) == 0:
        return []
    length = len(minefield[0])
    result = []
    if any(len(string) != length or any(char not in ('*', ' ') for char in string) for string in minefield):
        raise ValueError("The board is invalid with current input.")
    for i in range(0, len(minefield)):
        new_row = []
        for j in range(0, length):
            if minefield[i][j] == '*':
                new_row.append('*')
                continue
            minefield_count = 0
            for dx, dy in neighbour:
                m = i + dx
                n = j + dy
                if 0 <= m < len(minefield) and 0 <= n < len(minefield[0]) and minefield[m][n] == '*':
                    minefield_count += 1
            if minefield_count > 0:
                new_row.append(str(minefield_count))
            else:
                new_row.append(' ')
        result.append(''.join(new_row))
    return result
