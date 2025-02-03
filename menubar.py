import tkinter as tk

class MyMenu(tk.Menu):
    def __init__(self, root, save_session, load_session):
        super().__init__(root)

        file_menu = tk.Menu(self, tearoff=0)
        file_menu.add_command(label="New", command=None)
        file_menu.add_command(label="Open", command=load_session)
        file_menu.add_command(label="Save", command=save_session)
        file_menu.add_separator()
        file_menu.add_command(label="Exit", command=None)
        self.add_cascade(label="File", menu=file_menu)

        view_menu = tk.Menu(self, tearoff=0)
        view_menu.add_checkbutton(label="small", command=None)
        view_menu.add_checkbutton(label="large", command=None)
        self.add_cascade(label="View", menu=view_menu)

    def set_size(self, size):
        pass