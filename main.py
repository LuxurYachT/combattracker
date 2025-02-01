import tkinter as tk
from combatant_widget import Combatant

rows = []

root = tk.Tk()

button_frame = tk.Frame(root)
button_frame.pack()

def add_combatant():
    new_combatant = Combatant(root, remove_row)
    rows.append(new_combatant)

def get_combatant_data():
    combatants = []
    for i in rows:
        data_set = [i.combatant_name_entry.get(), i.combatant_init_entry.get()]
        if data_set[1] == "":
            data_set[1] = None
        else:
            data_set[1] = float(data_set[1])
        combatants.append(data_set)
    return combatants

def sort_combatants():
    combatants = sorted(get_combatant_data(), key=lambda x: (x[1] is None, -x[1] if x[1] is not None else 0))
    for j in range(len(rows)):
        rows[j].combatant_name_entry.delete(0, tk.END)
        rows[j].combatant_name_entry.insert(0, combatants[j][0])
        rows[j].combatant_init_entry.delete(0, tk.END)
        rows[j].combatant_init_entry.insert(0, str(combatants[j][1]))

def advance_turn():
    combatants = get_combatant_data()
    for i in range(len(rows)):
        rows[i].combatant_name_entry.delete(0, tk.END)
        rows[i].combatant_init_entry.delete(0, tk.END)
        if i < len(rows) - 1:
            rows[i].combatant_name_entry.insert(0, combatants[i+1][0])
            rows[i].combatant_init_entry.insert(0, str(combatants[i+1][1]))
        else:
            rows[i].combatant_name_entry.insert(0, combatants[0][0])
            rows[i].combatant_init_entry.insert(0, str(combatants[0][1]))            

def reverse_turn():
    combatants = get_combatant_data()
    for i in range(len(rows)):
        rows[i].combatant_name_entry.delete(0, tk.END)
        rows[i].combatant_init_entry.delete(0, tk.END)
        if i > 0:
            rows[i].combatant_name_entry.insert(0, combatants[i-1][0])
            rows[i].combatant_init_entry.insert(0, str(combatants[i-1][1]))
        else:
            rows[i].combatant_name_entry.insert(0, combatants[len(rows)-1][0])
            rows[i].combatant_init_entry.insert(0, str(combatants[len(rows)-1][1])) 

def remove_row(row):
    if row in rows:
        rows.remove(row)
    else:
        print("row not found")


add_combatant_button = tk.Button(button_frame, text="Add Combatant", command=add_combatant)
add_combatant_button.pack(side="left")

sort_button = tk.Button(button_frame, text="sort", command=sort_combatants)
sort_button.pack(side="left")

reverse_button = tk.Button(button_frame, text="<", command=reverse_turn)
reverse_button.pack(side="left")

advance_button = tk.Button(button_frame, text=">", command=advance_turn)
advance_button.pack(side="left")

root.title("Oroboros Combat Tracker")
root.mainloop()