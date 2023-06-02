from const import *
from grid.cell import Cell


class Agent:
    def __init__(self) -> None:
        self.x = 1
        self.y = 1
        self.direction = EAST
        self.gold = False
        self.dead = False
        self.grid_state = [[Cell() for _ in range(6)] for _ in range(6)]

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
        if self.direction == EAST:
            self.x += 1
        elif self.direction == WEST:
            self.x -= 1
        elif self.direction == NORTH:
            self.y += 1
        elif self.direction == SOUTH:
            self.y -= 1

        self.path.append([self.x, self.y])

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

    def find_path(self, x: int, y: int) -> list:
        # BFS
        queue = [(self.x, self.y)]
        visited = set()
        path = []
        
        return path
    
    def get_sensor_input(self, sensor_input: list) -> None:
        if sensor_input[0]:
            self.grid_state[self.x][self.y].stench = True
        if sensor_input[1]:
            self.grid_state[self.x][self.y].breeze = True
        if sensor_input[2]:
            self.grid_state[self.x][self.y].glitter = True
        if sensor_input[3]:
            self.grid_state[self.x][self.y].bump = True
        if sensor_input[4]:
            self.grid_state[self.x][self.y].scream = True
