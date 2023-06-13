from collections import deque
from const import *
from kb import expr, WumpusKB, adjust_coords, next_coords
from grid import Cell


class Agent:
    def __init__(self) -> None:
        self.x = 1
        self.y = 1
        self.arrow = 2
        self.t = 0
        self.direction = EAST
        self.gold_here = False
        self.gold = False
        self.dead = False
        self.win = False
        self.kb = WumpusKB()
        self.state = {}
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
        self.plan_action = []

    def visit(self, x: int, y: int) -> None:
        self.visited.add((x, y))
        self.path.append((x, y))
        self.t += 1

    def perceive(self, sensor_input: dict) -> None:
        print("percept: ", end="")
        self.kb.tell(expr(f"~P{self.x}{self.y}"))
        self.kb.tell(expr(f"~W{self.x}{self.y}"))
        if sensor_input.get("stench") is True:
            self.kb.tell(expr(f"S{self.x}{self.y}"))
            print(f"stench", end=" ")
        elif sensor_input.get("stench") is False:
            self.kb.tell(expr(f"~S{self.x}{self.y}"))
        if sensor_input.get("breeze") is True:
            self.kb.tell(expr(f"B{self.x}{self.y}"))
            print(f"breeze", end=" ")
        elif sensor_input.get("breeze") is False:
            self.kb.tell(expr(f"~B{self.x}{self.y}"))
        if sensor_input.get("glitter") is True:
            self.gold_here = True
            print(f"glitter", end=" ")
        if sensor_input.get("bump") is True:
            self.bump = True
            print(f"bump", end=" ")
        print()
        # print(f"{self.x},{self.y} : {sensor_input}")

    def reasoning(self) -> None:
        self.state = self.kb.dpll_satisfiable()
        # CLIMB
        if self.gold is True and self.x == 1 and self.y == 1:
            self.plan_action.append("climb")
        # GOLD
        elif self.gold_here is True:
            self.plan_action.append("grab")
        # SHOOT
        # next_x, next_y = next_coords(self.x, self.y, self.direction)
        # if (
        #     next_x is not None
        #     and self.state.get(expr(f"W{next_x}{next_y}")) is True
        #     and self.arrow > 0
        # ):
        #     self.plan_action.append("shoot")
        # MOVE: TURN LEFT or TURN RIGHT or GO FORWARD
        elif len(self.plan_action) == 0:
            plan = None
            if self.gold is True:
                plan = self.find_path_to_start()
            else:
                plan = self.find_first_unvisited_safe_path()
                if plan is None:
                    plan = self.find_first_unvisited_path()
            # print("plan: ", end="")
            # print(plan)
            if plan is None:
                raise Exception("도달할 수 없음")
            # print("plan: ", end="")
            # print(plan)
            actions = self.make_action(plan)
            self.plan_action += actions
            # print("plan_action: ", end="")
            # print(self.plan_action)

    def action(self) -> str:
        action_now = self.plan_action.pop(0)
        print("action: " + action_now)
        self.action_sequence.append(action_now)
        if action_now == "go_forward":
            self.move()
        elif action_now == "turn_left":
            self.turn_left()
        elif action_now == "turn_right":
            self.turn_right()
        elif action_now == "grab":
            self.grab()
        elif action_now == "shoot":
            self.shoot()
        elif action_now == "climb":
            self.climb()
        return action_now

    def restart(self) -> None:
        self.arrow = 2
        self.x = 1
        self.y = 1
        self.t = 0
        self.direction = EAST
        self.gold = False
        self.dead = False
        self.plan = []

    def shoot(self) -> None:
        self.arrow -= 1

    def move(self) -> None:
        if self.direction == EAST:
            self.y += 1
        elif self.direction == WEST:
            self.y -= 1
        elif self.direction == NORTH:
            self.x -= 1
        elif self.direction == SOUTH:
            self.x += 1

    def move_to(self, x: int, y: int) -> None:
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
        self.win = True

    def grab(self) -> None:
        self.gold = True
        self.gold_here = False

    def die(self, reason: str) -> None:
        if reason == "wumpus":
            self.kb.tell(expr(f"W{self.x}{self.y}"))
        elif reason == "pit":
            self.kb.tell(expr(f"P{self.x}{self.y}"))
        self.dead = True
        self.t = 0

    def make_action(
        self,
        plan: list[int, int],
    ) -> list:
        ret = []
        now_x, now_y = self.x, self.y
        now_direction = self.direction
        while len(plan) > 0:
            next_coord = plan.pop(0)
            next_x, next_y = next_coord
            if now_x == next_x and now_y == next_y:
                return [" "]
            if now_x == next_x:
                if now_y < next_y:
                    if now_direction == EAST:
                        ret += ["go_forward"]
                    elif now_direction == WEST:
                        ret += ["turn_right", "turn_right", "go_forward"]
                    elif now_direction == NORTH:
                        ret += ["turn_right", "go_forward"]
                    elif now_direction == SOUTH:
                        ret += ["turn_left", "go_forward"]
                    now_direction = EAST
                else:
                    if now_direction == EAST:
                        ret += ["turn_left", "turn_left", "go_forward"]
                    elif now_direction == WEST:
                        ret += ["go_forward"]
                    elif now_direction == NORTH:
                        ret += ["turn_left", "go_forward"]
                    elif now_direction == SOUTH:
                        ret += ["turn_right", "go_forward"]
                    now_direction = WEST
            elif now_y == next_y:
                if now_x < next_x:
                    if now_direction == EAST:
                        ret += ["turn_right", "go_forward"]
                    elif now_direction == WEST:
                        ret += ["turn_left", "go_forward"]
                    elif now_direction == NORTH:
                        ret += ["turn_right", "turn_right", "go_forward"]
                    elif now_direction == SOUTH:
                        ret += ["go_forward"]
                    now_direction = SOUTH
                else:
                    if now_direction == EAST:
                        ret += ["turn_left", "go_forward"]
                    elif now_direction == WEST:
                        ret += ["turn_right", "go_forward"]
                    elif now_direction == NORTH:
                        ret += ["go_forward"]
                    elif now_direction == SOUTH:
                        ret += ["turn_right", "turn_right", "go_forward"]
                    now_direction = NORTH
            now_x, now_y = next_x, next_y
        return ret

    def find_first_unvisited_safe_path(self) -> list[tuple[int, int]]:
        queue = deque([(self.x, self.y, [])])
        visited = [[False for _ in range(6)] for _ in range(6)]
        visited[self.x][self.y] = True

        while queue:
            # print(queue)
            x, y, path = queue.popleft()
            adj = adjust_coords(x, y)
            # print(f"adj: {adj}")
            for dx, dy in adj:
                if not visited[dx][dy]:
                    if (
                        ((dx, dy) not in self.visited)
                        and (self.state.get(expr(f"P{dx}{dy}")) is False)
                        and (self.state.get(expr(f"W{dx}{dy}")) is False)
                    ):
                        return path + [(dx, dy)]
                    if (self.state.get(expr(f"P{dx}{dy}")) is False) and (
                        self.state.get(expr(f"W{dx}{dy}")) is False
                    ):
                        visited[dx][dy] = True
                        queue.append((dx, dy, path + [(dx, dy)]))

        return None

    def find_first_unvisited_path(self) -> list[tuple[int, int]]:
        queue = deque([(self.x, self.y, [])])
        visited = [[False for _ in range(6)] for _ in range(6)]
        visited[self.x][self.y] = True

        while queue:
            x, y, path = queue.popleft()
            adj = adjust_coords(x, y)
            for dx, dy in adj:
                if not visited[dx][dy]:
                    if (dx, dy) not in self.visited:
                        return path + [(dx, dy)]
                    if (self.state.get(expr(f"P{dx}{dy}")) is False) and (
                        self.state.get(expr(f"W{dx}{dy}")) is False
                    ):
                        visited[dx][dy] = True
                        queue.append((dx, dy, path + [(dx, dy)]))

        return None

    def find_path_to_start(self) -> list[tuple[int, int]]:
        queue = deque([(self.x, self.y, [])])
        visited = [[False for _ in range(6)] for _ in range(6)]
        visited[self.x][self.y] = True

        while queue:
            x, y, path = queue.popleft()
            adj = adjust_coords(x, y)
            for dx, dy in adj:
                if not visited[dx][dy]:
                    if dx == 1 and dy == 1:
                        return path + [(dx, dy)]
                    if (self.state.get(expr(f"P{dx}{dy}")) is False) and (
                        self.state.get(expr(f"W{dx}{dy}")) is False
                    ):
                        visited[dx][dy] = True
                        queue.append((dx, dy, path + [(dx, dy)]))

        return None

    def next_direction(self, next_x: int, next_y: int) -> int:
        if next_x == self.y + 1:
            return EAST
        elif next_x == self.y - 1:
            return WEST
        elif next_y == self.x + 1:
            return NORTH
        elif next_y == self.x - 1:
            return SOUTH

    def change_direction(self, direction: int) -> None:
        if direction == self.direction:
            return
        else:
            self.direction = direction

    def print_kb_grid_state(self) -> None:
        for x in range(1, 5):
            for y in range(1, 5):
                result = self.kb.dpll_satisfiable()
                if result is False:
                    print("unsatisfiable", end=" ")
                elif self.x == x and self.y == y:
                    print("A ", end=" ")
                elif (
                    (x + 1, y) not in self.visited
                    and (x - 1, y) not in self.visited
                    and (x, y + 1) not in self.visited
                    and (x, y - 1) not in self.visited
                ):
                    print("? ", end=" ")
                elif isinstance(result, dict):
                    if result.get(expr(f"P{x}{y}")) and (x, y) in self.visited:
                        print("P ", end=" ")
                    elif result.get(expr(f"P{x}{y}")) and (x, y) not in self.visited:
                        print("P?", end=" ")
                    elif result.get(expr(f"W{x}{y}")) and (x, y) in self.visited:
                        print("W ", end=" ")
                    elif result.get(expr(f"W{x}{y}")) and (x, y) not in self.visited:
                        print("W?", end=" ")
                    elif result.get(expr(f"G{x}{y}")) and (x, y) in self.visited:
                        print("G" , end=" ")
                    else:
                        print("- ", end=" ")
                else:
                    print("-", end=" ")
            print()
