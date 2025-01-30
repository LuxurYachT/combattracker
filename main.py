import tkinter as tk
from combatant_widget import Combatant

fields = []

root = tk.Tk()

button_frame = tk.Frame(root)
button_frame.pack()

def add_combatant():
    new_combatabt = Combatant(root)
    fields.append(new_combatabt)

def sort_combatants():
    combatants = []
    for i in fields:
        data_set = [i.combatant_name_entry.get(), i.combatant_init_entry.get()]
        if data_set[1] == "":
            data_set[1] = None
        else:
            data_set[1] = int(data_set[1])
        combatants.append(data_set)
    combatants = sorted(combatants, key=lambda x: (x[1] is None, -x[1] if x[1] is not None else 0))



add_combatant_button = tk.Button(button_frame, text="Add Combatant", command=add_combatant)
add_combatant_button.pack(side="left")

sort_button = tk.Button(button_frame, text="sort", command=sort_combatants)
sort_button.pack(side="left")


root.mainloop()