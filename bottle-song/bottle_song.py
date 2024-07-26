def recite(start, take=1):
    output = []
    dict = {
        10: 'Ten',
        9: 'Nine',
        8: 'Eight',
        7: 'Seven',
        6: 'Six',
        5: 'Five',
        4: 'Four',
        3: 'Three',
        2: 'Two',
        1: 'One',
        0: 'no'
    }

    for i in range(take):
        item = dict[start]
        minus = dict[start - 1].lower()
        if start == 2:
            space = ""
        else:
            space = 's'

        if item == 'One':
            space2 = ""
        else:
            space2 = 's'

        lyrics = [
                 f"{item} green bottle{space2} hanging on the wall,",
                 f"{item} green bottle{space2} hanging on the wall,",
                 "And if one green bottle should accidentally fall,",
                 f"There'll be {minus} green bottle{space} hanging on the wall.",
                "",
                ]
        for lyric in lyrics:
            output.append(lyric)
        start = start - 1

    return output[:-1]

