from turtle import Turtle
from grid.cell import Cell


class Agent:
    def __init__(self) -> None:
        self.arrow = 2
        self.x = 1
        self.y = 1
        self.direction = "east"
        self.gold = False
        self.dead = False
        self.path = [[1, 1]]
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
        self.direction = "east"
        self.gold = False
        self.dead = False
        self.path = []

    def shoot(self) -> None:
        self.arrow -= 1

    def move(self) -> None:
        if self.direction == "east":
            self.x += 1
        elif self.direction == "west":
            self.x -= 1
        elif self.direction == "north":
            self.y += 1
        elif self.direction == "south":
            self.y -= 1

        self.path.append([self.x, self.y])

    def turn_left(self) -> None:
        if self.direction == "east":
            self.direction = "north"
        elif self.direction == "west":
            self.direction = "south"
        elif self.direction == "north":
            self.direction = "west"
        elif self.direction == "south":
            self.direction = "east"

    def turn_right(self) -> None:
        if self.direction == "east":
            self.direction = "south"
        elif self.direction == "west":
            self.direction = "north"
        elif self.direction == "north":
            self.direction = "east"
        elif self.direction == "south":
            self.direction = "west"

    def climb(self) -> None:
        pass

    def grab(self) -> None:
        pass

    def find_path(self, x: int, y: int) -> list:
        # BFS
        queue = [(self.x, self.y)]
        visited = set()
        path = []
        while queue:
            x, y = queue.pop(0)
            if (x, y) == (x, y):
                break
            if (x, y) not in visited and self.grid_state[x][y].safe:
                visited.add((x, y))
                path.append((x, y))
                if x > 1:
                    queue.append((x - 1, y))
                if x < 5:
                    queue.append((x + 1, y))
                if y > 1:
                    queue.append((x, y - 1))
                if y < 5:
                    queue.append((x, y + 1))
        return path
