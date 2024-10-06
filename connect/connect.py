class ConnectGame:
    def __init__(self, board):
        self.board = [[stone for stone in row] for row in board.replace(' ', '').splitlines()]
        self.neighbours = [(0, 1), (1, 0), (1, -1), (0, -1), (-1, 0), (-1, 1)]

    def get_winner(self):
        for player in ['O', 'X']:
            result = self.checker(player)
            if result is True:
                return player
        return ''

    def checker(self, player):
        if player == 'O':
            boardarray = self.board
        elif player == 'X':
            boardarray = list(zip(*self.board))
        stones = [(index, 0) for index, stone in enumerate(boardarray[0]) if stone == player]
        ends = [(index, len(boardarray)-1) for index, stone in enumerate(boardarray[-1])if stone == player]
        for stone in stones:
            for neighbour in self.neighbours:
                row = stone[1] + neighbour[1]
                column = stone[0] + neighbour[0]
                if row >= 0 and column >=0:
                    try:
                        if boardarray[row][column] == player and (column,row) not in stones:
                            stones.append((column,row))
                    except IndexError:
                        continue
        for end in ends:
            if end in stones:
                return True