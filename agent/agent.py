from const import *
from grid import Cell
from kb import *


class Agent:
    def __init__(self) -> None:
        self.x = 1
        self.y = 1
        self.arrow = 2
        self.t = 0
        self.direction = EAST
        self.gold = False
        self.dead = False
        self.kb = WumpusKB()
        self.actions = {
            "go_forward": False,
            "turn_left": False,
            "turn_right": False,
            "grab": False,
            "shoot": False,
            "climb": False,
        }
        self.path = []
        self.action_sequence = []
        self.visited = set()
        self.plan = []

    def visit(self, x: int, y: int) -> None:
        self.visited.add((x, y))
        self.path.append((x, y))
        self.t += 1

    def perceive(self, sensor_input: dict) -> None:
        self.kb.tell(expr(f"~P{self.x}{self.y}"))
        self.kb.tell(expr(f"~W{self.x}{self.y}"))
        if sensor_input.get("stench") is True:
            self.kb.tell(expr(f"S{self.x}{self.y}"))
        elif sensor_input.get("stench") is False:
            self.kb.tell(expr(f"~S{self.x}{self.y}"))
        if sensor_input.get("breeze") is True:
            self.kb.tell(expr(f"B{self.x}{self.y}"))
        elif sensor_input.get("breeze") is False:
            self.kb.tell(expr(f"~B{self.x}{self.y}"))
        if sensor_input.get("glitter") is True:
            self.kb.tell(expr(f"G{self.x}{self.y}"))
        # print(f"{self.x},{self.y} : {sensor_input}")

    def reasoning(self) -> None:
        result = self.kb.dpll_satisfiable()

    def action(self) -> None:
        pass

    def restart(self) -> None:
        self.arrow = 2
        self.x = 1
        self.y = 1
        self.direction = EAST
        self.gold = False
        self.dead = False

    def shoot(self) -> None:
        self.arrow -= 1

    def move(self) -> None:
        if self.direction == EAST:
            self.x += 1
        elif self.direction == WEST:
            self.x -= 1
        elif self.direction == NORTH:
            self.y += 1
        elif self.direction == SOUTH:
            self.y -= 1

    def move(self, x: int, y: int) -> None:
        self.x = x
        self.y = y

    def turn_left(self) -> None:
        if self.direction == EAST:
            self.direction = NORTH
        elif self.direction == WEST:
            self.direction = SOUTH
        elif self.direction == NORTH:
            self.direction = WEST
        elif self.direction == SOUTH:
            self.direction = EAST

    def turn_right(self) -> None:
        if self.direction == EAST:
            self.direction = SOUTH
        elif self.direction == WEST:
            self.direction = NORTH
        elif self.direction == NORTH:
            self.direction = EAST
        elif self.direction == SOUTH:
            self.direction = WEST

    def climb(self) -> None:
        pass

    def grab(self) -> None:
        pass

    def die(self, reason: str) -> None:
        if reason == "wumpus":
            self.kb.tell(expr(f"W{self.x}{self.y}"))
        elif reason == "pit":
            self.kb.tell(expr(f"P{self.x}{self.y}"))
        self.dead = True
        self.t = 0

    def find_safe_path(self) -> list:
        ret = []
        return ret

    def print_kb_grid_state(self) -> None:
        for x in range(1, 5):
            for y in range(1, 5):
                result = self.kb.dpll_satisfiable()
                if result is False:
                    print("unsatisfiable")
                    return
                elif result is True or result.get(expr(f"P{x}{y}")) is True:
                    print("P", end=" ")
                elif result is True or result.get(expr(f"W{x}{y}")) is True:
                    print("W", end=" ")
                elif result is True or result.get(expr(f"G{x}{y}")) is True:
                    print("G", end=" ")
                else:
                    print("-", end=" ")
            print()
