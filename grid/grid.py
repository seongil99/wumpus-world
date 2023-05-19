import random
from .cell import Cell


class Grid:
    def __init__(self) -> None:
        self.grid = [[Cell() for _ in range(6)] for _ in range(6)]
        # 1,1 is the starting point and is always safe
        self.grid[1][1].pit = False
        self.grid[1][1].wumpus = False
        self.grid[1][1].agent = True
        # set gold and glitter
        # gold is randomly placed in 4x4 grid not including 1,1
        gold_x = random.randint(1, 4)
        gold_y = random.randint(1, 4)
        if gold_x == 1 and gold_y == 1:
            gold_x = 2
            gold_y = 2
        self.grid[gold_x][gold_y].gold = True
        self.grid[gold_x][gold_y].glitter = True
        # gold is in a safe cell and is not a pit or wumpus
        self.grid[gold_x][gold_y].safe = True
        self.grid[gold_x][gold_y].pit = False
        self.grid[gold_x][gold_y].wumpus = False
        # set stench and breeze
        for i in range(6):
            for j in range(6):
                if self.grid[i][j].wumpus:
                    if i > 0 and i < 5 and j > 0 and j < 5:
                        self.grid[i][j].stench = True
                        self.grid[i - 1][j].stench = True
                        self.grid[i + 1][j].stench = True
                        self.grid[i][j - 1].stench = True
                        self.grid[i][j + 1].stench = True
                if self.grid[i][j].pit:
                    if i > 0 and i < 5 and j > 0 and j < 5:
                        self.grid[i][j].breeze = True
                        self.grid[i - 1][j].breeze = True
                        self.grid[i + 1][j].breeze = True
                        self.grid[i][j - 1].breeze = True
                        self.grid[i][j + 1].breeze = True
                        # set walls around the grid
        # wall has no stench or breeze
        # wall has no wumpus or pit
        for i in range(6):
            self.grid[i][0].breeze = False
            self.grid[i][0].stench = False
            self.grid[i][0].pit = False
            self.grid[i][0].wumpus = False
            self.grid[i][0].safe = False
            self.grid[i][5].breeze = False
            self.grid[i][5].stench = False
            self.grid[i][5].pit = False
            self.grid[i][5].wumpus = False
            self.grid[i][5].safe = False
            self.grid[0][i].breeze = False
            self.grid[0][i].stench = False
            self.grid[0][i].pit = False
            self.grid[0][i].wumpus = False
            self.grid[0][i].safe = False
            self.grid[5][i].breeze = False
            self.grid[5][i].stench = False
            self.grid[5][i].pit = False
            self.grid[5][i].wumpus = False
            self.grid[5][i].safe = False

    def get_cell(self, x: int, y: int) -> Cell:
        return self.grid[x][y]

    def get_grid(self) -> list:
        return self.grid

    def kill_wumpus(self) -> None:
        for row in self.grid:
            for cell in row:
                cell.kill_wumpus()

    def print_grid(self) -> None:
        for row in self.grid:
            for cell in row:
                print(cell.__dict__)
            print()
