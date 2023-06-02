from turtle import Turtle
from grid.cell import Cell


class Agent:
    def __init__(self) -> None:
        self.EAST = 0
        self.NORTH = 1
        self.WEST = 2
        self.SOUTH = 3
        self.arrow = 2
        self.x = 1
        self.y = 1
        self.direction = self.EAST
        self.gold = False
        self.dead = False
        self.grid_state = [[Cell() for _ in range(6)] for _ in range(6)]
        self.grid_state[1][1].agent = True

    def process_percepts(self, percepts) -> None:
        """
        에이전트는 이 메소드를 통해 주어진 센서 입력을 처리합니다.
        """
        # 센서 입력 처리 로직 구현
        pass

    def decide_action(self) -> None:
        """
        에이전트는 이 메소드를 통해 다음 행동을 결정합니다.
        """
        # 행동 결정 로직 구현
        pass

    def action(self, action) -> None:
        """
        에이전트는 이 메소드를 통해 행동을 수행합니다.
        """
        # 행동 수행 로직 구현
        pass

    def restart(self) -> None:
        self.arrow = 2
        self.x = 1
        self.y = 1
        self.direction = self.EAST
        self.gold = False
        self.dead = False
        self.path = []

    def shoot(self) -> None:
        self.arrow -= 1

    def move(self) -> None:
        if self.direction == self.EAST:
            self.x += 1
        elif self.direction == self.WEST:
            self.x -= 1
        elif self.direction == self.NORTH:
            self.y += 1
        elif self.direction == self.SOUTH:
            self.y -= 1

        self.path.append([self.x, self.y])

    def turn_left(self) -> None:
        if self.direction == self.EAST:
            self.direction = self.NORTH
        elif self.direction == self.WEST:
            self.direction = self.SOUTH
        elif self.direction == self.NORTH:
            self.direction = self.WEST
        elif self.direction == self.SOUTH:
            self.direction = self.EAST

    def turn_right(self) -> None:
        if self.direction == self.EAST:
            self.direction = self.SOUTH
        elif self.direction == self.WEST:
            self.direction = self.NORTH
        elif self.direction == self.NORTH:
            self.direction = self.EAST
        elif self.direction == self.SOUTH:
            self.direction = self.WEST

    def climb(self) -> None:
        pass

    def grab(self) -> None:
        pass

    def find_path(self, x: int, y: int) -> list:
        # BFS
        queue = [(self.x, self.y)]
        visited = set()
        path = []
        
        return path
