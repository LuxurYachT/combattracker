import tkinter as tk

class Player:
    def __init__(self, root):
        self.root = root
        self.frame = tk.Frame(self.root)
        self.frame.pack()
        self.player_name_entry = tk.Entry(self.frame, width=20)
        self.player_name_entry.pack(side='left', padx=5)
        self.player_init_entry = tk.Entry(self.frame, width=5)
        self.player_init_entry.pack(side='left', padx=5)