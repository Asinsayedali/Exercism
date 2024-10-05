def annotate(minefield):
    # Function body starts here
    if len(minefield) == 0: return []
    length = len(minefield[0])
    for string in minefield:
        if len(string) != length:
            raise ValueError("The board is invalid with current input.")
        for char in string:
            if char not in ('*', ' '):
                raise ValueError("The board is invalid with current input.")
    neighbour = [(-1, -1), (-1, 0), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1), (-1, 1)]
    new_minefield = [list(row) for row in minefield]
    for i in range(0, len(new_minefield)):
        for j in range(0, length):
            if new_minefield[i][j] == '*':
                continue
            minefield_count = 0
            for dx, dy in neighbour:
                m = i + dx
                n = j + dy
                if 0 <= m < len(new_minefield) and 0 <= n < len(new_minefield[0]):
                    if new_minefield[m][n] == '*':
                        minefield_count += 1
            if minefield_count > 0:
                new_minefield[i][j] = str(minefield_count)
    result = [''.join(row) for row in new_minefield]
    return result
