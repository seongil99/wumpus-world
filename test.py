# test mock data

# ========================
# | 1,1 | 1,2 | 1,3 | 1,4 |
# ========================
# | 2,1 | 2,2 | 2,3 | 2,4 |
# ========================
# | 3,1 | 3,2 | 3,3 | 3,4 |
# ========================
# | 4,1 | 4,2 | 4,3 | 4,4 |
# ========================

# agent is at (1, 1)
# agent is facing right
# wumpus is at (2, 2)
# pit is at (3, 3)
# gold is at (4, 4)
# ========================


from grid import Cell
from grid import Grid
from kb import PropKB, expr, adjust_coords, WumpusKB
from agent import Agent
import math
import time
import datetime


def test_kb():
    wumpus_kb = PropKB()

    P11, P12, P21, P22, P31, B11, B21 = expr("P11, P12, P21, P22, P31, B11, B21")
    wumpus_kb.tell(expr("~P11"))
    wumpus_kb.tell(expr("B11 <=> (P12 | P21)"))
    wumpus_kb.tell(expr("B21 <=> (P11 | P22 | P31)"))
    wumpus_kb.tell(expr("~B11"))
    wumpus_kb.tell(expr("B21"))

    # Statement: There is no pit in [1,1].
    assert wumpus_kb.ask(~P11) == {}

    # Statement: There is no pit in [1,2].
    assert wumpus_kb.ask(~P12) == {}

    # Statement: There is a pit in [2,2].
    assert not wumpus_kb.ask(P22)

    # Statement: There is a pit in [3,1].
    assert not wumpus_kb.ask(P31)

    # Statement: Neither [1,2] nor [2,1] contains a pit.
    assert wumpus_kb.ask(~P12 & ~P21) == {}

    # Statement: There is a pit in either [2,2] or [3,1].
    assert wumpus_kb.ask(P22 | P31) == {}

    print(wumpus_kb.clauses)


def make_test_grid() -> list[list[Cell]]:
    test_grid = [[Cell() for _ in range(6)] for _ in range(6)]
    test_grid[2][2].wumpus = True
    test_grid[3][3].pit = True
    test_grid[4][4].gold = True
    test_grid[4][4].glitter = True
    # set breeze and stench
    for x in range(1, 5):
        for y in range(1, 5):
            adj = adjust_coords(x, y)
            if test_grid[x][y].pit:
                # test_grid[x][y].breeze = True
                for px, py in adj:
                    test_grid[px][py].breeze = True
            if test_grid[x][y].wumpus:
                # test_grid[x][y].stench = True
                for px, py in adj:
                    test_grid[px][py].stench = True
    # set bump at four edges
    for x in range(6):
        test_grid[x][0].bump = True
        test_grid[x][5].bump = True
        test_grid[0][x].bump = True
        test_grid[5][x].bump = True
    return test_grid


def print_all_grid(self) -> None:
    for x in range(1, 5):
        for y in range(1, 5):
            if self[x][y].wumpus:
                print("W", end=" ")
            elif self[x][y].pit:
                print("P", end=" ")
            elif self[x][y].gold:
                print("G", end=" ")
            else:
                print("-", end=" ")
        print()


def main():
    # game = Game()
    # game.root.after(100, lambda: game.move_agent(2, 1))  # Start the animation 100 ms after the mainloop starts
    # game.root.mainloop()  # Start the mainloop
    start = time.time()
    # grid = make_test_grid()
    grid = Grid()
    agent = Agent()
    for x in range(1, 5):
        for y in range(1, 5):
            agent.move(x, y)
            # agent.perceive(grid[x][y].get_sensor_input())
            if grid.get_cell(x, y).wumpus:
                agent.die("wumpus")
            elif grid.get_cell(x, y).pit:
                agent.die("pit")
            else:
                agent.perceive(grid.get_sensor_input(x, y))
    agent.print_kb_grid_state()
    print()
    # print_all_grid(grid)
    grid.print_all_grid()

    kb = WumpusKB()
    result = kb.dpll_satisfiable()
    print(result.get(expr("P11")))
    end = time.time()
    sec = end - start
    result_time = datetime.timedelta(seconds=sec)
    print(str(result_time) + " sec")


if __name__ == "__main__":
    for i in range(10):
        main()
