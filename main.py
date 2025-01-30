import tkinter as tk
from player_widget import Player


root = tk.Tk()

button_frame = tk.Frame(root)
button_frame.pack()

def add_palyer():
    Player(root)

add_player_button = tk.Button(button_frame, text="Add Combatant", command=add_palyer)
add_player_button.pack(side="left")

sort_button = tk.Button(button_frame, text="sort")
sort_button.pack(side="left")


root.mainloop()