from turtle import Turtle, Screen

from agent.agent import Agent
from grid.grid import Grid


class Game:
    def __init__(self) -> None:
        self.screen = Screen()
        self.screen.setup(width=1200, height=1000)
        self.screen.title("Wumpus World")
        # self.screen.tracer(0)
        self.grid = Grid()
        self.agent = Agent()
        # draw grid
        self.draw_grid()
        # draw agent
        # self.draw_agent()
        self.screen.mainloop()

    def draw_grid(self) -> None:
        for i in range(6):
            for j in range(6):
                cell = self.grid.get_cell(i, j)
                x = -300 + i * 100
                y = 300 - j * 100
                self.draw_cell(x, y)
                if cell.breeze:
                    self.draw_breeze(x, y)
                if cell.stench:
                    self.draw_stench(x, y)
                if cell.pit:
                    self.draw_pit(x, y)
                if cell.wumpus:
                    self.draw_wumpus(x, y)
                if cell.gold:
                    self.draw_gold(x, y)
                if cell.agent:
                    self.draw_agent(x, y)

    def draw_cell(self, x: int, y: int) -> None:
        t = Turtle()
        t.hideturtle()
        t.penup()
        t.speed(0)
        t.color("black")
        t.goto(x, y)
        t.pendown()
        for _ in range(4):
            t.forward(100)
            t.right(90)

    def draw_breeze(self, x: int, y: int) -> None:
        t = Turtle()
        t.hideturtle()
        t.penup()
        t.speed(0)
        t.color("blue")
        t.goto(x + 50, y - 30)
        t.pendown()
        t.circle(10)

    def draw_stench(self, x: int, y: int) -> None:
        t = Turtle()
        t.hideturtle()
        t.penup()
        t.speed(0)
        t.color("red")
        t.goto(x + 50, y - 40)
        t.pendown()
        t.circle(10)

    def draw_pit(self, x: int, y: int) -> None:
        t = Turtle()
        t.hideturtle()
        t.penup()
        t.speed(0)
        t.color("black")
        t.goto(x + 50, y - 50)
        t.pendown()
        t.begin_fill()
        t.circle(10)
        t.end_fill()

    def draw_wumpus(self, x: int, y: int) -> None:
        t = Turtle()
        t.hideturtle()
        t.penup()
        t.speed(0)
        t.color("green")
        t.goto(x + 50, y - 60)
        t.pendown()
        t.circle(10)

    def draw_gold(self, x: int, y: int) -> None:
        t = Turtle()
        t.hideturtle()
        t.penup()
        t.speed(0)
        t.color("orange")
        t.goto(x + 50, y - 70)
        t.pendown()
        t.circle(10)

    def draw_agent(self, x: int, y: int) -> None:
        # agent is a circle in the center of the cell
        t = self.agent.turtle
        t.hideturtle()
        t.penup()
        t.speed(0)
        t.color("black")
        t.goto(x + 50, y - 80)
        t.pendown()
        t.circle(10)
