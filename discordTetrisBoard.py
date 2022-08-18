# make discord message from tetris board

import tkinter as tk
from tkinter import font
from functools import partial

root = tk.Tk()

# variables

blank_image = tk.PhotoImage()
full_grid = {}
mouse_pressed = False

colors_list = ["black", "gray", "red", "orange", "yellow", "cyan", "lime", "blue", "purple"]
selected_color = "gray"
emoji_dict = {
    "black": ":black_large_square:",
    "gray": ":white_large_square:",
    "red": ":red_square:",
    "orange": ":orange_square:",
    "yellow": ":yellow_square:",
    "cyan": ":blue_square:",
    "lime": ":green_square:",
    "blue": ":stop_button:",
    "purple": "purple_square"
}

# methods

def setColor(color):
    global selected_color 
    selected_color = color

def changeColor(i, j):
    full_grid[f"{i} {j}"].config(bg=selected_color)

def process():
    for i in range(20):
        emojis_row = []
        for j in range(10):
            emojis_row.append(
                emoji_dict[
                    full_grid[f"{i} {j}"].cget("bg")
                ]
            )
        print("".join(str(i) for i in emojis_row))
    print("\n")

def clearBoard(event):
    for i in range(20):
        for j in range(10):
            full_grid[f"{i} {j}"].config(bg="black")

def mouseDown(event):
    global mouse_pressed
    mouse_pressed = True

def mouseUp(event):
    global mouse_pressed
    mouse_pressed = False

board = tk.Frame()
board.pack()

def mouseMoving(event):
    for i in range(20):
        for j in range(10):
            if mouse_pressed:
                if board.winfo_containing(event.x_root, event.y_root) is full_grid[f"{i} {j}"]:
                    full_grid[f"{i} {j}"].config(bg=selected_color)

# build grid

for i in range(20):
    for j in range(10):
        button = tk.Button(
            board,
            image = blank_image,
            borderwidth = 1,
            height = 20,
            width = 20,
            bg = "black",
            command = partial(changeColor, i, j)
        )
        full_grid.update({f"{i} {j}": button})
        button.grid(row = i, column = j)

board.bind_all("<Button-1>", mouseDown)
board.bind_all("<ButtonRelease-1>", mouseUp)
board.bind_all("<B1-Motion>", mouseMoving)
board.bind_all("c", clearBoard)

color_label = tk.Label(root, text = "block color")
color_label.pack()

block_colors = tk.Frame()
block_colors.pack()

for i in range(9):
    bcolor = tk.Button(
        block_colors,
        image = blank_image,
        borderwidth = 1,
        height = 20,
        width = 20,
        bg = colors_list[i],
        command = partial(setColor, colors_list[i])
    )
    bcolor.grid(row = 0, column = i)

process = tk.Button(
    root,
    text = "process",
    command = process
)
process.pack()

instructions = tk.Label(
    root,
    text = "press c to clear board",
)
instructions.pack()

root.mainloop()