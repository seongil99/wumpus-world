from .cell import Cell


class Grid:
    def __init__(self) -> None:
        self.grid = [[Cell() for _ in range(6)] for _ in range(6)]
        # 1,1 is the starting point and is always safe
        self.grid[1][1].pit = False
        self.grid[1][1].wumpus = False
        self.grid[1][1].agent = True
        # set walls
        for i in range(6):
            self.grid[i][0].bump = True
            self.grid[i][5].bump = True
            self.grid[0][i].bump = True
            self.grid[5][i].bump = True
        # set stench and breeze
        for i in range(6):
            for j in range(6):
                if self.grid[i][j].wumpus:
                    if i > 0:
                        self.grid[i - 1][j].stench = True
                    if i < 5:
                        self.grid[i + 1][j].stench = True
                    if j > 0:
                        self.grid[i][j - 1].stench = True
                    if j < 5:
                        self.grid[i][j + 1].stench = True
                if self.grid[i][j].pit:
                    if i > 0:
                        self.grid[i - 1][j].breeze = True
                    if i < 5:
                        self.grid[i + 1][j].breeze = True
                    if j > 0:
                        self.grid[i][j - 1].breeze = True
                    if j < 5:
                        self.grid[i][j + 1].breeze = True

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
