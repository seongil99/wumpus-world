import random
from .cell import Cell


class Grid:
    def __init__(self) -> None:
        self.grid = [[Cell() for _ in range(6)] for _ in range(6)]
        # 1,1 is the starting point and is always safe
        self.grid[1][1].pit = False
        self.grid[1][1].wumpus = False
        self.grid[1][1].agent = True

    def get_cell(self, x: int, y: int) -> Cell:
        return self.grid[x][y]

    def print_grid(self) -> None:
        for row in self.grid:
            for cell in row:
                print(cell.__dict__)
            print()
    
    def get_sensor_input(self, x: int, y: int) -> list:
        return self.grid[x][y].get_sensor_input()