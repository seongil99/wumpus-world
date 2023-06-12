import tkinter as tk


class Application(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.title("Moving Ball")

        # Canvas where the ball will be drawn and moved
        self.canvas = tk.Canvas(self, width=600, height=400, bg="white")
        self.canvas.pack()

        # Draw a red ball
        self.ball = self.canvas.create_oval(50, 50, 100, 100, fill="red")

        # Create a "Move" button
        self.move_button = tk.Button(self, text="Move", command=self.move_ball)
        self.move_button.pack()

        # Variables to control the movement
        self.moving = False
        self.remaining_moves = 0

    def move_ball(self):
        """Start moving the ball."""
        self.moving = True
        self.remaining_moves = 100
        self.move_ball_step()

    def move_ball_step(self):
        """Move the ball 1 pixel to the right, and schedule the next move."""
        if self.moving and self.remaining_moves > 0:
            self.canvas.move(self.ball, 1, 0)
            self.remaining_moves -= 1
            self.after(30, self.move_ball_step)  # Schedule the next move
        else:
            self.moving = False


if __name__ == "__main__":
    app = Application()
    app.mainloop()
