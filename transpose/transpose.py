import itertools

def transpose(lines):
    updated = []
    for row, line in enumerate(lines.splitlines()):
        for c, char in enumerate(line):
            while len(updated) <= c:
                updated.append([])
            while len(updated[c]) < row:
                updated[c].append(' ')
            updated[c].append(char)
    return ('\n'.join(''.join(row) for row in updated))

