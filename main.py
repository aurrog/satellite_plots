import tkinter as tk
import os
from satellite_plots import class_file

classes = []

for file in os.listdir('../testing/navdata'):
    classes.append(class_file.File(file))

root = tk.Tk()
root.geometry('800x500')

label = tk.Label(text='Файл')
label.place(x=10, y=20, width=150)

buttons = []
for i in range(len(classes)):
    btn = tk.Button(text=classes[i].path, command=classes[i].type_list)
    btn.place(x=10, y=60 + 50 * i, width=150, height=40)
    buttons.append(btn)

root.mainloop()
