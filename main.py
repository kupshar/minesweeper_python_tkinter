from tkinter import *
from cell import Cell
import settings
import utils


root = Tk()
root.configure(bg='black')
root.geometry(f'{settings.WIDTH}x{settings.HEIGHT}')
root.title("Minesweeper'is")
root.resizable(False, False)

top_frame = Frame(
    root,
    bg='black',
    width=settings.WIDTH,
    height=utils.height_percent(25),
)
top_frame.place(x=0, y=0)

game_title = Label(
    top_frame,
    bg='black',
    fg='red',
    text='M1n35w33p3r',
    font=('', 48)
)

game_title.place(
    x=utils.width_percent(25), y=0
)

left_frame = Frame(
    root,
    bg='black',
    width=utils.width_percent(25),
    height=utils.height_percent(75)
)

left_frame.place(x=0, y=utils.height_percent(25))

center_frame = Frame(
    root,
    bg='black',
    width=utils.width_percent(75),
    height=utils.height_percent(75)
)

center_frame.place(
    x=utils.width_percent(25),
    y=utils.height_percent(25)
)

for x in range(settings.GRID_SIZE):
    for y in range(settings.GRID_SIZE):
        c = Cell(x, y)
        c.create_btn_object(center_frame)
        c.cell_btn_object.grid(
            column=x, row=y
        )

Cell.create_cell_count_label(left_frame)
Cell.cell_count_label_object.place(x=0, y=0)

Cell.randomize_mines()


root.mainloop()
