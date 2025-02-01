import tkinter as tk

class Combatant:
    def __init__(self, root):
        self.root = root
        self.frame = tk.Frame(self.root)
        self.frame.pack()
        self.combatant_name_entry = tk.Entry(self.frame, width=20)
        self.combatant_name_entry.pack(side='left', padx=5)
        self.combatant_init_entry = tk.Entry(self.frame, width=5)
        self.combatant_init_entry.pack(side='left', padx=5)
        self.combatant_init_entry.configure(validate="key", validatecommand=(self.combatant_init_entry.register(self.validate_input), '%P'))

    def validate_input(self, new_value):
        try:
            if new_value == "":
                return True
            float(new_value)
            return True
        except ValueError:
            return False
            
