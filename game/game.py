import math
import time
import tkinter

from agent.agent import Agent
from grid.grid import Grid


class Game:
    def __init__(self) -> None:
        self.root = tkinter.Tk()
        self.root.title("wumpus world")
        self.root.geometry("800x800")
        self.root.resizable(False, False)

        self.agent_position = [100, 100]  # Agent's current position

        self.agnet_id = 0

        self.agent_image = tkinter.PhotoImage(file="assets/agent.png").subsample(10, 10)

        self.grid_canvas = tkinter.Canvas(
            self.root, relief="solid", bd=2, width=800, height=800
        )
        self.draw_grid()
        self.draw_agent()
        self.grid_canvas.pack(side="top")

    def draw_grid(self) -> None:
        # draw 4 by 4 grid each cell is 200 by 200
        for i in range(4):
            for j in range(4):
                self.grid_canvas.create_rectangle(
                    i * 200,
                    j * 200,
                    (i + 1) * 200,
                    (j + 1) * 200,
                    fill="white",
                    outline="black",
                )
                self.grid_canvas.create_text(
                    i * 200 + 100,
                    j * 200 + 100,
                    text="({},{})".format(i + 1, j + 1),
                    fill="black",
                )

    def draw_agent(self) -> None:
        self.agent_id = self.grid_canvas.create_image(100, 100, image=self.agent_image)

    def move_agent_step(self, x: int, y: int) -> None:
        if self.moving and self.remaining_moves > 0:
            self.grid_canvas.move(self.agent_id, x, y)
            self.remaining_moves -= 1
            self.root.after(30, self.move_agent_step, x, y)  # Schedule the next move
        else:
            self.moving = False

    def move_agent(self, x: int, y: int) -> None:
        self.moving = True
        self.remaining_moves = 100
        self.move_agent_step(x, y)
