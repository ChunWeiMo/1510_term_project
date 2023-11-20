import tkinter as tk


def update_label(entry, label):
    new_text = entry.get()
    label.config(text=new_text)


def draw_map(map, character, canvas):
    cell_size = 40
    for coordinate in map:
        x, y = coordinate[0] * cell_size, coordinate[1] * cell_size

        if map[coordinate] == "Door":
            color = "dark goldenrod"
        elif map[coordinate] == "Enemy":
            color = "Red"
        elif map[coordinate] == "Chest":
            color = "yellow"
        elif map[coordinate] == "Boss":
            color = "Purple"
        elif map[coordinate] == "Healing_fountain":
            color = "sky blue"
        else:
            color = "white"

        canvas.create_rectangle(
            x, y, x + cell_size, y + cell_size, fill=color, outline='black')

    c_x, c_y = character["X-coordinate"] * \
        cell_size, character["Y-coordinate"] * cell_size

    canvas.create_rectangle(
        c_x, c_y, c_x + cell_size, c_y + cell_size, fill="blue", outline='black')


def draw_character(character, canvas):
    cell_size = 40
    x, y = character["X-coordinate"], character["Y-coordinate"]
    canvas.create_rectangle(
        x, y, x + cell_size, y + cell_size, fill="blue", outline='black')


def main():

    map = {(0, 0): 'Empty', (1, 0): 'Empty', (2, 0): 'Empty', (3, 0): 'Empty', (4, 0): 'Door', (5, 0): 'Empty', (6, 0): 'Empty', (7, 0): 'Empty', (8, 0): 'Empty', (9, 0): 'Empty', (0, 1): 'Empty', (1, 1): 'Enemy', (2, 1): 'Enemy', (3, 1): 'Enemy', (4, 1): 'Enemy', (5, 1): 'Enemy', (6, 1): 'Enemy', (7, 1): 'Enemy', (8, 1): 'Enemy', (9, 1): 'Empty', (0, 2): 'Empty', (1, 2): 'Enemy', (2, 2): 'Enemy', (3, 2): 'Enemy', (4, 2): 'Enemy', (5, 2): 'Enemy', (6, 2): 'Enemy', (7, 2): 'Enemy', (8, 2): 'Enemy', (9, 2): 'Empty', (0, 3): 'Empty', (1, 3): 'Enemy', (2, 3): 'Enemy', (3, 3): 'Empty', (4, 3): 'Empty', (5, 3): 'Boss', (6, 3): 'Empty', (7, 3): 'Enemy', (8, 3): 'Enemy', (9, 3): 'Empty', (0, 4): 'Empty', (1, 4): 'Enemy', (2, 4): 'Enemy', (3, 4): 'Healing_fountain', (4, 4): 'Chest', (5, 4): 'Chest', (6, 4): 'Healing_fountain', (7, 4): 'Enemy', (8, 4): 'Enemy', (9, 4): 'Door',
           (0, 5): 'Door', (1, 5): 'Enemy', (2, 5): 'Enemy', (3, 5): 'Healing_fountain', (4, 5): 'Chest', (5, 5): 'Chest', (6, 5): 'Healing_fountain', (7, 5): 'Enemy', (8, 5): 'Enemy', (9, 5): 'Empty', (0, 6): 'Empty', (1, 6): 'Enemy', (2, 6): 'Enemy', (3, 6): 'Empty', (4, 6): 'Boss', (5, 6): 'Empty', (6, 6): 'Empty', (7, 6): 'Enemy', (8, 6): 'Enemy', (9, 6): 'Empty', (0, 7): 'Empty', (1, 7): 'Enemy', (2, 7): 'Enemy', (3, 7): 'Enemy', (4, 7): 'Enemy', (5, 7): 'Enemy', (6, 7): 'Enemy', (7, 7): 'Enemy', (8, 7): 'Enemy', (9, 7): 'Empty', (0, 8): 'Empty', (1, 8): 'Enemy', (2, 8): 'Enemy', (3, 8): 'Enemy', (4, 8): 'Enemy', (5, 8): 'Enemy', (6, 8): 'Enemy', (7, 8): 'Enemy', (8, 8): 'Enemy', (9, 8): 'Empty', (0, 9): 'Empty', (1, 9): 'Empty', (2, 9): 'Empty', (3, 9): 'Empty', (4, 9): 'Empty', (5, 9): 'Door', (6, 9): 'Empty', (7, 9): 'Empty', (8, 9): 'Empty', (9, 9): 'Empty'}
    character_status = {'Level': 1, 'HP': 100, 'STR': 10,
                        'DEF': 1, 'CHR': 1, 'SPD': 1, 'LUK': 2}
    character = {"character_status": character_status,
                 "X-coordinate": 2, "Y-coordinate": 4}

    root = tk.Tk()
    root.title("1510_Patricia_Quest")

    # create command line and button
    entry = tk.Entry(root)
    entry.grid(row=15, column=0, padx=10, pady=10)
    entry_var = tk.StringVar()

    label = tk.Label(root, text="Hello, tkinter!")
    label.grid(row=16, column=0, padx=10, pady=10)

    button = tk.Button(root, text="Update Label",
                       command=update_label(entry, label))
    button.grid(row=17, column=0, padx=10, pady=10)

    # create empty canvas
    cell_size = 40
    rows, cols = 10, 10
    canvas = tk.Canvas(root, width=cols * cell_size, height=rows * cell_size)
    canvas.grid(row=5, column=0)

    # 画地图
    draw_map(map, character, canvas)
    # draw_character(character, canvas)

    root.mainloop()


if __name__ == "__main__":
    main()
