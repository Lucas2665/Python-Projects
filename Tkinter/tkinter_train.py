import tkinter as tk
from tkinter import ttk

def button_func():
    print("hello")

# create a window
window = tk.Tk()
window.title("Window and widgets")
window.geometry("800x500")

# ttk label
label = ttk.Label(master=window, text="This is a test")
label.pack()

# tk text
text = tk.Text(master = window)
text.pack()

#ttk entry
entry = ttk.Entry(master=window)
entry.pack()

# ttk label
label1 = ttk.Label(master=window, text="my label")
label1.pack()

# ttk button
button = ttk.Button(master=window, text = "submit", command = button_func)
button.pack()

# run
window.mainloop()