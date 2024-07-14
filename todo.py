import tkinter as tk

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

# start tkinter event loop
root.mainloop()