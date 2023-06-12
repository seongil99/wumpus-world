from const import *


class Cell:
    def __init__(self) -> None:
        self.wumpus = False
        self.pit = False
        self.stench = False
        self.breeze = False
        self.gold = False
        self.glitter = False
        self.bump = False
        self.scream = False
        self.visited = False

    def kill_wumpus(self) -> None:
        self.wumpus = False

    def get_sensor_input(self) -> dict:
        return {
            "stench": self.stench,
            "breeze": self.breeze,
            "glitter": self.glitter,
            "bump": self.bump,
            "scream": self.scream,
        }
