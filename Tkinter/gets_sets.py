import tkinter as tk
from tkinter import ttk

def button_func():
    entry.get()


#window
window = tk.Tk()
window.title("Getting and Setting")

# Widgets
label = ttk.Label(master=window, text="Getting and Setting")
label.pack()

entry = ttk.Entry(master=window)
entry.pack()

button = ttk.Button(master=window, text="button", command=button_func)
button.pack()

# run
window = tk.mainloop()