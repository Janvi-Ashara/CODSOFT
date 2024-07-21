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

#create the window
root = tk.Tk()
root.title("My To-Do List")

# background color
root.configure(bg='white')

# main title
t_label = tk.Label(root,text = "My To-Do List",font=("Helvetica",20,"bold"),bg='#DBA39A',fg="#FFB4B4")
t_label.pack(pady=20)

#frame for the input button

root.geometry("500x500")
input_frame=tk.Frame(root,bg='white')
input_frame.pack(pady=5)

# entry label
e1=tk.Label(input_frame,text="Enter Your task :",font=("Helvetica",12),bg="beige")
e1.grid(row=0,column=0,padx=10,pady=5)

#entry box
entry = tk.Entry(input_frame, width=25)
entry.grid(row=0, column=2, padx=5, pady=5)

#listbox
listbox=tk.Listbox(root,width=50, height=10, font=("Helvetica", 12))
listbox.pack(pady=10)

# create buttons frame:
b_frame=tk.Frame(root,bg='white')
b_frame.pack(pady=10)

# create the buttons

add_button = tk.Button(b_frame, text="Add Task", width=15, command=add_task)
add_button.grid(row=0, column=0, padx=5, pady=5)

delete_button = tk.Button(b_frame, text="Delete Task", width=15, command=delete_task)
delete_button.grid(row=1, column=0, padx=5, pady=5)

delete_all_button = tk.Button(b_frame, text="Delete All Tasks", width=15, command=delete_all_tasks)
delete_all_button.grid(row=2, column=0, padx=5, pady=5)

exit_button = tk.Button(b_frame, text="Exit", width=15, command=exit_app)
exit_button.grid(row=3, column=0, padx=5, pady=5)

# start tkinter event loop
root.mainloop()