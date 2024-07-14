# CODSOFT
Python task offred by CODSOFT

import tkinter as tk
from tkinter import messagebox

def add_task():
    task = entry.get()
    if task:
        listbox.insert(tk.END, task)
        entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "You must enter a task.")

def delete_task():
    try:
        selected_task_index = listbox.curselection()[0]
        listbox.delete(selected_task_index)
    except IndexError:
        messagebox.showwarning("Warning", "You must select a task.")

def delete_all_tasks():
    listbox.delete(0, tk.END)

def exit_app():
    root.quit()

# Create the main window
root = tk.Tk()
root.title("To-Do List Manager")

# Configure the window background color
root.configure(bg='beige')

# Create the main title label
title_label = tk.Label(root, text="The To-Do List", font=("Helvetica", 18, "bold"), bg="beige", fg="brown")
title_label.pack(pady=10)

# Create a frame for the input and buttons
input_frame = tk.Frame(root, bg="beige")
input_frame.pack(pady=10)

# Create the entry label
entry_label = tk.Label(input_frame, text="Enter the Task:", font=("Helvetica", 12), bg="beige")
entry_label.grid(row=0, column=0, padx=5, pady=5)

# Create the entry box
entry = tk.Entry(input_frame, width=25)
entry.grid(row=0, column=1, padx=5, pady=5)

# Create the listbox
listbox = tk.Listbox(root, width=50, height=10, font=("Helvetica", 12))
listbox.pack(pady=10)

# Create the buttons frame
buttons_frame = tk.Frame(root, bg="beige")
buttons_frame.pack(pady=10)

# Create the buttons
add_button = tk.Button(buttons_frame, text="Add Task", width=15, command=add_task)
add_button.grid(row=0, column=0, padx=5, pady=5)

delete_button = tk.Button(buttons_frame, text="Delete Task", width=15, command=delete_task)
delete_button.grid(row=1, column=0, padx=5, pady=5)

delete_all_button = tk.Button(buttons_frame, text="Delete All Tasks", width=15, command=delete_all_tasks)
delete_all_button.grid(row=2, column=0, padx=5, pady=5)

exit_button = tk.Button(buttons_frame, text="Exit", width=15, command=exit_app)
exit_button.grid(row=3, column=0, padx=5, pady=5)

# Start the Tkinter event loop
root.mainloop()
