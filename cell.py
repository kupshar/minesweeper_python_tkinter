from tkinter import Button, Label
import random
import settings
import ctypes
import sys


class Cell:
    all = []
    cell_count = settings.CELL_COUNT
    cell_count_label_object = None

    def __init__(self, x, y, is_mine=False):
        self.is_mine = is_mine
        self.is_opened = False
        self.cell_btn_object = None
        self.probably_a_mine = False
        self.x = x
        self.y = y

        Cell.all.append(self)

    def create_btn_object(self, location):
        btn = Button(
            location,
            width=12,
            height=4,
        )
        btn.bind('<Button-1>', self.left_click_action)
        btn.bind('<Button-3>', self.right_click_action)
        self.cell_btn_object = btn

    @staticmethod
    def create_cell_count_label(location):
        label = Label(location, bg='black', fg='white',
                      text=f'Cells left:{Cell.cell_count}',
                      width=12, height=4,
                      font=("", 24))
        Cell.cell_count_label_object = label

    def left_click_action(self, event):
        if self.is_mine:
            self.show_mine()
        else:
            if self.surrounding_cells_mine_length == 0:
                for cell_obj in self.surrounding_cells:
                    cell_obj.show_cell()
            self.show_cell()

            if Cell.cell_count == settings.MINE_COUNT:
                ctypes.windll.user32.MessageBoxW(0, 'C0ngr4tz ur 1337', 'G4M3 0V3R', 0)



        self.cell_btn_object.unbind('<Button-1>')
        self.cell_btn_object.unbind('<Button-3>')

    def get_cell_by_axis(self, x, y):
        for cell in Cell.all:
            if cell.x == x and cell.y == y:
                return cell

    @property
    def surrounding_cells(self):
        cells = [self.get_cell_by_axis(self.x - 1, self.y - 1),
                 self.get_cell_by_axis(self.x - 1, self.y),
                 self.get_cell_by_axis(self.x - 1, self.y + 1),
                 self.get_cell_by_axis(self.x, self.y - 1),
                 self.get_cell_by_axis(self.x + 1, self.y - 1),
                 self.get_cell_by_axis(self.x + 1, self.y),
                 self.get_cell_by_axis(self.x + 1, self.y + 1),
                 self.get_cell_by_axis(self.x, self.y + 1)
                 ]
        cells = [cell for cell in cells if cell is not None]
        return cells

    @property
    def surrounding_cells_mine_length(self):
        counter = 0
        for cell in self.surrounding_cells:
            if cell.is_mine:
                counter += 1

        return counter

    def show_cell(self):
        if not self.is_opened:
            Cell.cell_count -= 1
            self.cell_btn_object.configure(text=self.surrounding_cells_mine_length)
            if Cell.cell_count_label_object:
                Cell.cell_count_label_object.configure(
                    text=f'Cells Left:{Cell.cell_count}'
                )
            self.cell_btn_object.configure(
                bg='SystemButtonFace'
                )
        self.is_opened = True

    def show_mine(self):
        self.cell_btn_object.configure(bg='red', text='B00M')
        ctypes.windll.user32.MessageBoxW(0, 'Y0u 3xpl0d3d N00B', 'G4M3 0V3R', 0)
        sys.exit()

    def right_click_action(self, event):
        if not self.probably_a_mine:
            self.cell_btn_object.configure(
                bg='orange'
            )
            self.probably_a_mine = True
        else:
            self.cell_btn_object.configure(
                bg='SystemButtonFace'
            )
            self.probably_a_mine = False

    @staticmethod
    def randomize_mines():
        chosen_cells = random.sample(Cell.all, settings.MINE_COUNT)
        for chosen_cell in chosen_cells:
            chosen_cell.is_mine = True

    def __repr__(self):
        return f'Cell({self.x}, {self.y})'
