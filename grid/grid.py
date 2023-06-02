import random
from .cell import Cell


class Grid:
    def __init__(self) -> None:
        self.grid = [[Cell() for _ in range(6)] for _ in range(6)]
        # 1,1 is the starting point and is always safe
        self.grid[1][1].pit = False
        self.grid[1][1].wumpus = False
        self.grid[1][1].agent = True
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
        x = random.randint(1, 5)
        y = random.randint(1, 5)
        while x == 1 and y == 1:
            x = random.randint(1, 5)
            y = random.randint(1, 5)
        self.grid[x][y].gold = True
        self.grid[x][y].glitter = True
        self.grid[x][y].wumpus = False
        self.grid[x][y].pit = False
        # set breeze and stench
        for x in range(1, 5):
            for y in range(1, 5):
                if self.grid[x][y].pit:
                    self.grid[x-1][y].breeze = True
                    self.grid[x+1][y].breeze = True
                    self.grid[x][y-1].breeze = True
                    self.grid[x][y+1].breeze = True
                if self.grid[x][y].wumpus:
                    self.grid[x-1][y].stench = True
                    self.grid[x+1][y].stench = True
                    self.grid[x][y-1].stench = True
                    self.grid[x][y+1].stench = True

    def get_cell(self, x: int, y: int) -> Cell:
        return self.grid[x][y]

    def print_grid(self) -> None:
        for row in self.grid:
            for cell in row:
                if cell.agent:
                    print('A', end=' ')
                elif cell.wumpus:
                    print('W', end=' ')
                elif cell.pit:
                    print('P', end=' ')
                elif cell.gold:
                    print('G', end=' ')
                else:
                    print('-', end=' ')
            print()
    
    def get_sensor_input(self, x: int, y: int) -> list:
        return self.grid[x][y].get_sensor_input()