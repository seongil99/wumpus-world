from grid import Grid
from agent import Agent
import time
import datetime


def main():
    start = time.time()

    grid = Grid()
    agent = Agent()
    grid.print_all_grid()
    print()
    while True:
        print(f"time: {agent.t}")
        agent.visit(agent.x, agent.y)
        if grid.get_cell(agent.x, agent.y).wumpus:
            agent.die("wumpus")
            print("dead by wumpus")
            agent.restart()
        elif grid.get_cell(agent.x, agent.y).pit:
            agent.die("pit")
            print("dead by pit")
            agent.restart()
        else:
            agent.perceive(grid.get_sensor_input(agent.x, agent.y))
            agent.print_kb_grid_state()
            agent.reasoning()
            action = agent.action()
            if action == "grab":
                grid.grab_gold()
        if agent.win is True:
            print("WIN!")
            break

    end = time.time()
    sec = end - start
    result_time = datetime.timedelta(seconds=sec)
    print(str(result_time) + " sec")


if __name__ == "__main__":
    main()
