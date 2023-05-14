import random


class Cell:
    def __init__(self) -> None:
        wumpus_prob = random.randint(1, 100)
        pit_prob = random.randint(1, 100)

        if wumpus_prob <= 10:
            self.wumpus = True
        else:
            self.wumpus = False

        if pit_prob <= 10 and not self.wumpus:
            self.pit = True
        else:
            self.pit = False

        self.stench = False
        self.breeze = False
        self.agent = False
        self.gold = False
        self.glitter = False
        self.bump = False
        self.scream = False

    def kill_wumpus(self) -> None:
        self.wumpus = False
        self.stench = False
