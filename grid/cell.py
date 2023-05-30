import random
from turtle import Turtle


class Cell:
    def __init__(self) -> None:
        self.wumpus = False
        self.pit = False
        self.stench = False
        self.breeze = False
        self.agent = False
        self.gold = False
        self.glitter = False
        self.bump = False
        self.scream = False
        self.safe = True
        self.visited = False

    def kill_wumpus(self) -> None:
        self.wumpus = False
        self.stench = False
