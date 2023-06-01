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

from game import Game
from agent import Agent
from grid import Grid

agent = Agent()
grid = Grid()

if __name__ == '__main__':
    game = Game()
    game.root.after(100, lambda: game.move_agent(2, 1))  # Start the animation 100 ms after the mainloop starts
    game.root.mainloop()  # Start the mainloop

