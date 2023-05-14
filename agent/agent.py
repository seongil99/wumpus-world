class Agent:
    def __init__(self):
        self.arrow = 2
        self.x = 1
        self.y = 1
        self.direction = "east"
        self.gold = False
        self.dead = False
        self.path = [(1, 1)]
        self.grid_state = []

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

        self.path.append((self.x, self.y))

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
