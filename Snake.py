import tkinter as tk

class SnakeGame:
    def __init__(self, master):
        self.master = master
        self.canvas = tk.Canvas(self.master, bg='white', width=400, height=400)
        self.canvas.pack()
        self.snake_positions = [(100, 100), (90, 100), (80, 100), (70, 100), (60, 100)]
        self.food_positions = []
        self.direction = 'Right'
        self.score = 0

        self.create_food()
        self.create_snake()
        self.bind_keys()

    def create_food(self):
        x = self.canvas.create_rectangle(0, 0, 10, 10, fill='red')
        self.food_positions = self.canvas.coords(x)
        self.check_collision()

    def check_collision(self):
        x1, y1, x2, y2 = self.food_positions
        for pos in self.snake_positions:
            if pos[0] >= x1 and pos[0] <= x2:
                if pos[1] >= y1 and pos[1] <= y2:
                    self.canvas.delete(self.food)
                    self.create_food()

    def create_snake(self):
        for pos in self.snake_positions:
            self.canvas.create_rectangle(pos[0], pos[1], pos[0]+10, pos[1]+10, fill='green')

    def bind_keys(self):
        self.master.bind('<w>', self.move_up)
        self.master.bind('<s>', self.move_down)
        self.master.bind('<a>', self.move_left)
        self.master.bind('<d>', self.move_right)

    def move_up(self, event):
        if self.direction != 'Down':
            self.direction = 'Up'

    def move_down(self, event):
        if self.direction != 'Up':
            self.direction = 'Down'

    def move_left(self, event):
        if self.direction != 'Right':
            self.direction = 'Left'

    def move_right(self, event):
        if self.direction != 'Left':
            self.direction = 'Right'


if __name__ == '__main__':
    root = tk.Tk()
    SnakeGame(root)
    root.mainloop()
