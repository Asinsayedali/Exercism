NEIGBOUR = [(dx, dy) for dx in range(-1, 2) for dy in range(-1, 2) if dx or dy]


def annotate(minefield: list[str]) -> list[str]:
    if len(minefield) == 0:
        return []
    length = len(minefield[0])
    result: list[str] = []
    if any(len(string) != length or any(char not in ('*', ' ') for char in string) for string in minefield):
        raise ValueError('The board is invalid with current input.')
    for i, row in enumerate(minefield):
        new_row: list[str] = []
        for j, minefield_Value in enumerate(row):
            if minefield_Value == '*':
                new_row.append('*')
                continue
            minefield_count = 0
            for dx, dy in NEIGBOUR:
                m = i + dx
                n = j + dy
                if 0 <= m < len(minefield) and 0 <= n < length and minefield[m][n] == '*':
                    minefield_count += 1
            new_row.append((str(minefield_count)) if minefield_count > 0 else ' ')
        result.append(''.join(new_row))
    return result
