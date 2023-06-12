import random
from .cell import Cell
from const import *
from kb import adjust_coords


class Grid:
    def __init__(self) -> None:
        self.grid = [[Cell() for _ in range(6)] for _ in range(6)]
        # wumpus and pit are randomly placed in the grid 1 <= x <= 4 and 1 <= y <= 4 (not in 1,1)
        # percent chance of pit and wumpus is 10%
        for x in range(1, 5):
            for y in range(1, 5):
                if x == 1 and y == 1:
                    continue
                if random.randint(1, 100) <= 10:
                    self.grid[x][y].wumpus = True
                if random.randint(1, 100) <= 10 and not self.grid[x][y].wumpus:
                    self.grid[x][y].pit = True
        # gold is randomly placed in the grid 1 <= x <= 4 and 1 <= y <= 4 (not in 1,1)
        x = random.randint(1, 4)
        y = random.randint(1, 4)
        while x == 1 and y == 1:
            x = random.randint(1, 4)
            y = random.randint(1, 4)
        self.grid[x][y].gold = True
        self.grid[x][y].glitter = True
        self.grid[x][y].wumpus = False
        self.grid[x][y].pit = False
        # set breeze and stench
        for x in range(1, 5):
            for y in range(1, 5):
                adj = adjust_coords(x, y)
                if self.grid[x][y].pit:
                    # self.grid[x][y].breeze = True
                    for px, py in adj:
                        self.grid[px][py].breeze = True
                if self.grid[x][y].wumpus:
                    # self.grid[x][y].stench = True
                    for px, py in adj:
                        self.grid[px][py].stench = True
        # set bump at four edges
        for x in range(6):
            self.grid[x][0].bump = True
            self.grid[x][5].bump = True
            self.grid[0][x].bump = True
            self.grid[5][x].bump = True

    def get_cell(self, x: int, y: int) -> Cell:
        return self.grid[x][y]

    def print_all_grid(self) -> None:
        for x in range(1, 5):
            for y in range(1, 5):
                if self.grid[x][y].wumpus:
                    print("W", end=" ")
                elif self.grid[x][y].pit:
                    print("P", end=" ")
                elif self.grid[x][y].gold:
                    print("G", end=" ")
                else:
                    print("-", end=" ")
            print()
        # for i in range(1, 5):
        #     for j in range(1, 5):
        #         print(
        #             "{}, {} sensor input: {} ".format(i, j, self.get_sensor_input(i, j))
        #         )
        #     print()

    def get_sensor_input(self, x: int, y: int) -> dict:
        return self.grid[x][y].get_sensor_input()

    def set_scream(self, is_scream: bool) -> None:
        for x in range(1, 5):
            for y in range(1, 5):
                self.grid[x][y].scream = is_scream
