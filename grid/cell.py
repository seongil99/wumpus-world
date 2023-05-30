import random
from turtle import Turtle


class Cell:
    def __init__(self) -> None:
        self.SAFE = 0
        self.NOT_SAFE = 1
        self.UNKNOWN = 2

        self.wumpus = False
        self.pit = False
        self.stench = False
        self.breeze = False
        self.agent = False
        self.gold = False
        self.glitter = False
        self.bump = False
        self.scream = False
        self.safe = False
        self.visited = False
        self.status = self.UNKNOWN

    def kill_wumpus(self) -> None:
        self.wumpus = False
