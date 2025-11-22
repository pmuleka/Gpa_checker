from tkinter import *

root = Tk()

import tkinter as tk

def convert_to_fahrenheit():
    c = entry.get()
    if c.replace('.', '', 1).isdigit():
        f = (9/5) * float(c) + 32
        result_label.config(text=f"{c}°C = {f:.2f}°F")
    else:
        result_label.config(text="Enter a valid number!")

def convert_to_celsius():
    f = entry.get()
    if f.replace('.', '', 1).isdigit():
        c = (float(f) - 32) * 5/9
        result_label.config(text=f"{f}°F = {c:.2f}°C")
    else:
        result_label.config(text="Enter a valid number!")

root = tk.Tk()
root.title("Temp Converter")

entry = tk.Entry(root)
entry.pack()

to_f_button = tk.Button(root, text="To Fahrenheit", command=convert_to_fahrenheit)
to_f_button.pack()

to_c_button = tk.Button(root, text="To Celsius", command=convert_to_celsius)
to_c_button.pack()

result_label = tk.Label(root, text="Result here")
result_label.pack()

root.mainloop()
