#Window
import tkinter as tk

root = tk.Tk()
root.title("My Application")
root.geometry("300x200")

label = tk.Label(root, text="Hello, Tkinter!")
label.pack()

root.mainloop()

#Button
import tkinter as tk

def button_click():
    label.config(text="Button clicked!")

root = tk.Tk()
root.title("Button Click Event")

button = tk.Button(root, text="Click Me", command=button_click)
button.pack()

label = tk.Label(root, text="")
label.pack()

root.mainloop()

#Entry Widget with Validation
import tkinter as tk

def validate_entry():
    entry_text = entry.get()
    if entry_text.isdigit():
        label.config(text="Valid Entry")
    else:
        label.config(text="Invalid Entry")

root = tk.Tk()
root.title("Entry Validation")

entry = tk.Entry(root)
entry.pack()

button = tk.Button(root, text="Validate", command=validate_entry)
button.pack()

label = tk.Label(root, text="")
label.pack()

root.mainloop()

#Listbox Selection Event
import tkinter as tk

def selection_event(event):
    selected_item = listbox.get(listbox.curselection())
    label.config(text="Selected Item: " + selected_item)

root = tk.Tk()
root.title("Listbox Selection Event")

listbox = tk.Listbox(root)
listbox.pack()

listbox.insert(1, "Option 1")
listbox.insert(2, "Option 2")
listbox.insert(3, "Option 3")

listbox.bind("<<ListboxSelect>>", selection_event)

label = tk.Label(root, text="")
label.pack()

root.mainloop()

#Menu
import tkinter as tk

def file_new():
    label.config(text="New File created!")

def file_open():
    label.config(text="Open File selected!")

def file_save():
    label.config(text="File saved!")

root = tk.Tk()
root.title("Menu Bar")

menubar = tk.Menu(root)
root.config(menu=menubar)

file_menu = tk.Menu(menubar, tearoff=0)
menubar.add_cascade(label="File", menu=file_menu)

file_menu.add_command(label="New", command=file_new)
file_menu.add_command(label="Open", command=file_open)
file_menu.add_command(label="Save", command=file_save)

label = tk.Label(root, text="")
label.pack()

root.mainloop()

#Message Box
import tkinter as tk
from tkinter import messagebox

def show_message_box():
    messagebox.showinfo("Information", "This is a message box!")

root = tk.Tk()
root.title("Message Box")

button = tk.Button(root, text="Show Message Box", command=show_message_box)
button.pack()

root.mainloop()

#File Dialog
import tkinter as tk
from tkinter import filedialog

def open_file_dialog():
    file_path = filedialog.askopenfilename()
    label.config(text="Selected File: " + file_path)

root = tk.Tk()
root.title("File Dialog")

button = tk.Button(root, text="Open File", command=open_file_dialog)
button.pack()

label = tk.Label(root, text="")
label.pack()

root.mainloop()

#Canvas
import tkinter as tk

def draw_rectangle():
    canvas.create_rectangle(50, 50, 150, 150, fill="blue")

root = tk.Tk()
root.title("Canvas")

canvas = tk.Canvas(root, width=200, height=200)
canvas.pack()

button = tk.Button(root, text="Draw Rectangle", command=draw_rectangle)
button.pack()

root.mainloop()

#Scrolled Text
import tkinter as tk
from tkinter import scrolledtext

root = tk.Tk()
root.title("Scrolled Text")

text_area = scrolledtext.ScrolledText(root, width=30, height=10)
text_area.pack()

root.mainloop()


#Checkbutton
import tkinter as tk

def checkbox_clicked():
    if checkbox_var.get() == 1:
        label.config(text="Checkbox selected")
    else:
        label.config(text="Checkbox deselected")

root = tk.Tk()
root.title("Checkbutton")

checkbox_var = tk.IntVar()

checkbox = tk.Checkbutton(root, text="Select", variable=checkbox_var, command=checkbox_clicked)
checkbox.pack()

label = tk.Label(root, text="")
label.pack()

root.mainloop()



