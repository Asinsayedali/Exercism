# Globals for the directions
# Change the values as you see fit
NORTH = 0
EAST = 1
SOUTH = 2
WEST = 3


class Robot:
    def __init__(self, direction=NORTH, x_pos=0, y_pos=0):
        self.direction = direction
        self.coordinates = (x_pos, y_pos)
        self.moves = {
            NORTH: (0, 1),
            EAST: (1, 0),
            SOUTH: (0, -1),
            WEST: (-1, 0)
        }

    def move(self, instructions):
        for instruction in instructions:
            if instruction == "R":
                self.direction = (self.direction + 1) % 4
            if instruction == "L":
                self.direction = (self.direction - 1) % 4
            if instruction == "A":
                x, y = self.coordinates
                dx, dy = self.moves[self.direction]
                self.coordinates = (x+dx, y+dy)
