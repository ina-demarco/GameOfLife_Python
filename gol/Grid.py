import random
from tkinter import *


class Grid:
    x = 4
    y = 4  # default grid 4*4
    current_matrix = 0
    canvas = 0

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.init_empty_matrix()
        self.populate_matrix()

    def init_empty_matrix(self):
        self.current_matrix = [[False for y in range(self.y)] for x in range(self.x)]

    def print_matrix(self):
        for i in self.current_matrix:
            print(i)

    def populate_matrix(self):
        for i, row in enumerate(self.current_matrix):
            for j, cell in enumerate(row):
                r = random
                self.current_matrix[i][j] = bool(r.getrandbits(1))

    def count_neighbors(self, x, y):
        live_neighbors = 0

        if self.check_is_valid_position(x, y):
            # right neighbor
            if x + 1 < len(self.current_matrix):
                if self.current_matrix[x + 1][y]:
                    live_neighbors += 1

            # left neighbor
            if x - 1 >= 0:
                if self.current_matrix[x - 1][y]:
                    live_neighbors += 1

            # top neighbor
            if y - 1 >= 0:
                if self.current_matrix[x][y - 1]:
                    live_neighbors += 1

            # down neighbor
            if y + 1 < len(self.current_matrix[x]):
                if self.current_matrix[x][y + 1]:
                    live_neighbors += 1

            # top left neighbor
            if x - 1 >= 0 and y - 1 >= 0:
                if self.current_matrix[x - 1][y - 1]:
                    live_neighbors += 1

            # top right neighbor
            if x - 1 >= 0 and y + 1 < len(self.current_matrix[x]):
                if self.current_matrix[x - 1][y + 1]:
                    live_neighbors += 1

            # down left neighbor
            if x + 1 < len(self.current_matrix) and y - 1 >= 0:
                if self.current_matrix[x + 1][y - 1]:
                    live_neighbors += 1

            # down right neighbor
            if x + 1 < len(self.current_matrix) and y + 1 < len(self.current_matrix[x]):
                if self.current_matrix[x + 1][y + 1]:
                    live_neighbors += 1

        return live_neighbors

    def check_is_valid_position(self, x, y):
        return 0 <= x < self.x and 0 <= y < self.y

    def check_is_alive(self, x, y):
        if self.check_is_valid_position(x, y):
            return self.current_matrix[x][y]
        else:
            return None

    def change_state(self, x, y, new_matrix):
        if self.check_is_valid_position(x, y):
            new_matrix[x][y] = not self.current_matrix[x][y]

    def next_generation(self):
        new_matrix = [row[:] for row in self.current_matrix]
        for i in range(self.x):
            for j in range(self.y):
                self.compute_next_generation(i, j, new_matrix)
        self.current_matrix = new_matrix

    def compute_next_generation(self, x, y, new_matrix):
        if self.check_is_valid_position(x, y):
            count_neighbors = self.count_neighbors(x, y)
            if self.check_is_alive(x, y):

                # underpopulation
                if count_neighbors < 2:
                    self.change_state(x, y, new_matrix)
                # overpopulation
                if count_neighbors > 3:
                    self.change_state(x, y, new_matrix)
                    # exactly 2 or 3 neighbors

                    # else do nothing
            else:
                if count_neighbors == 3:
                    self.change_state(x, y, new_matrix)

    def add_predefined_matrix(self, matrix):
        self.current_matrix = matrix
        self.x = len(matrix)
        self.y = len(matrix[0])

    def draw_cells(self):
        for i, row in enumerate(self.current_matrix):
            for j, cell in enumerate(row):
                color = "green" if cell else "black"
                self.canvas.create_rectangle(i * 50, j * 50, i * 50 + 50, j * 50 + 50, fill=color)

    def draw_matrix(self):

        root = Tk()
        root.wm_title("Game of Life")
        label = Label(root, text="Press Escape to close window\nPress any other key to continue simulation")
        label.pack()
        # create a canvas
        self.canvas = Canvas(root, width=len(self.current_matrix) * 50, height=len(self.current_matrix[0] * 50))

        # define event handling method
        def key(event):
            self.next_generation()
            self.draw_cells()
            self.canvas.update_idletasks()

        def escape(event):
            root.destroy()

        # keyboard focus for the canvas
        self.canvas.focus_set()
        # bind event handling method to canvas
        self.canvas.bind("<Key>", key)
        self.canvas.bind("<Escape>", escape)
        # draw first generation
        self.draw_cells()
        self.canvas.pack()
        # opens gui and starts event listening thread? (not sure yet, but its needed)
        root.mainloop()

    def show_gui_with_generations(self, count):
        for c in range(count):
            self.draw_matrix()
            self.next_generation()
