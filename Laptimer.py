import tkinter as tk
from time import time


def create_window():
    root = tk.Tk()
    root.geometry('600x800')
    root.configure(background='black')

    time_var = tk.StringVar()
    time_label = tk.Label(root, textvariable=time_var, font=('Young', 50))
    time_label.pack(expand=True)

    button_frame = tk.Frame(root)
    button_frame.pack(expand=True)

    start_stop_button = tk.Button(button_frame, text='Start', bg='#FF0000', fg='#FFFFFF', font=('Arial', 20),
                                   command=start_stop_handler)
    start_stop_button.pack(side=tk.LEFT, expand=True)

    lap_button = tk.Button(button_frame, text='Lap', bg='#FF0000', fg='#FFFFFF', font=('Arial', 20),
                           command=lap_handler, state=tk.DISABLED)
    lap_button.pack(side=tk.LEFT, expand=True)

    laps_frame = tk.Frame(root)
    laps_frame.pack(expand=True)

    names_lb = tk.Listbox(laps_frame, font=('Arial', 15))
    names_lb.pack(side=tk.LEFT, fill=tk.Y)

    return root, time_var, start_stop_button, lap_button, laps_frame, names_lb


def start_stop_handler():
    global start_time, active
    if active:
        active = False
        start_stop_button.config(text='Reset')
        lap_button.config(state=tk.DISABLED)
    else:
        if start_time > 0:
            root.destroy()
        else:
            start_time = time()
            active = True
            start_stop_button.config(text='Stop')
            lap_button.config(state=tk.NORMAL)


def lap_handler():
    global lap_amount
    elapsed_time = round(time() - start_time, 1)
    lap_label = tk.Label(laps_frame, text='Lap {}: {}'.format(lap_amount, elapsed_time), font=('Arial', 15))
    lap_label.pack(side=tk.TOP, fill=tk.X)
    lap_amount += 1
    lap_name = get_lap_name(lap_amount)
    names_lb.insert(tk.END, lap_name)


def add_name():
    name = name_entry.get()
    if name != '':
        names.append(name)
        name_entry.delete(0, tk.END)


def get_lap_name(lap_num):
    if len(names) >= lap_num - 1:
        return names[lap_num - 2]
    else:
        return 'Lap {}'.format(lap_num)


root, time_var, start_stop_button, lap_button, laps_frame, names_lb = create_window()
start_time = 0
active = False
lap_amount = 1
names = []

name_frame = tk.Frame(root)
name_frame.pack(expand=True)

name_entry = tk.Entry(name_frame, font=('Arial', 20))
name_entry.pack(side=tk.LEFT, expand=True)

add_name_button = tk.Button(name_frame, text='Add Name', bg='#FF0000', fg='#FFFFFF', font=('Arial', 20),
                            command=add_name)
add_name_button.pack(side=tk.LEFT, expand=True)

while True:
    root.update()
    if not active:
        start_time = 0

    if active:
        elapsed_time = round(time() - start_time, 1)
        time_var.set(elapsed_time)
        lap_button.config(state=tk.NORMAL)

    if not active and start_time > 0:
        start_stop_button.config(text='Start')

    if not active and lap_amount > 1:
        start_stop_button.config(text='Start')
        lap_button.config(state=tk.DISABLED)
        lap_amount = 1
        names = []

    if active and start_time > 0:
        start_stop_button.config(text='Stop')

    if active and lap_amount == 1:
        lap_button.config(state=tk.NORMAL)

    if lap_amount >1:
        start_stop_button.config(text='Reset')

    if lap_amount > 10:
        root.destroy()


