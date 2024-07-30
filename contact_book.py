import tkinter as tk
from tkinter import messagebox, ttk

class ContactBook:
    def __init__(self, root):
        self.root = root
        self.root.title("Contact Management System")

        # Contact details
        self.contacts = []

        # Fields for entering contact details
        self.create_widgets()
        self.display_contacts()

    def create_widgets(self):

            # Entry labels and fields
        tk.Label(self.root, text="Name").grid(row=0, column=0, padx=10, pady=5)
        self.entry_name = tk.Entry(self.root)
        self.entry_name.grid(row=0, column=1, padx=10, pady=5)

        tk.Label(self.root, text="Phone").grid(row=1, column=0, padx=10, pady=5)
        self.entry_phone = tk.Entry(self.root)
        self.entry_phone.grid(row=1, column=1, padx=10, pady=5)

        tk.Label(self.root, text="Email").grid(row=2, column=0, padx=10, pady=5)
        self.entry_email = tk.Entry(self.root)
        self.entry_email.grid(row=2, column=1, padx=10, pady=5)

        tk.Label(self.root, text="Address").grid(row=3, column=0, padx=10, pady=5)
        self.entry_address = tk.Entry(self.root)
        self.entry_address.grid(row=3, column=1, padx=10, pady=5)

        # Buttons for managing contacts
        tk.Button(self.root, text="Add Contact", command=self.add_contact).grid(row=4, column=0, padx=10, pady=10)
        tk.Button(self.root, text="Update Contact", command=self.update_contact).grid(row=4, column=1, padx=10, pady=10)
        tk.Button(self.root, text="Delete Contact", command=self.delete_contact).grid(row=4, column=2, padx=10, pady=10)
        tk.Button(self.root, text="Clear Fields", command=self.clear_fields).grid(row=4, column=3, padx=10, pady=10)

        # Search functionality
        tk.Label(self.root, text="Search by Name/Phone").grid(row=5, column=0, padx=10, pady=5)
        self.entry_search = tk.Entry(self.root)
        self.entry_search.grid(row=5, column=1, padx=10, pady=5)
        tk.Button(self.root, text="Search", command=self.search_contact).grid(row=5, column=2, padx=10, pady=10)

        # Listbox to display contacts
        self.tree = ttk.Treeview(self.root, columns=("Name", "Phone", "Email", "Address"), show="headings")
        self.tree.heading("Name", text="Name")
        self.tree.heading("Phone", text="Phone")
        self.tree.heading("Email", text="Email")
        self.tree.heading("Address", text="Address")
        self.tree.grid(row=6, column=0, columnspan=4, padx=10, pady=10, sticky="nsew")
        self.tree.bind("<Double-1>", self.load_selected_contact)

    def add_contact(self):
        name = self.entry_name.get()
        phone = self.entry_phone.get()
        email = self.entry_email.get()
        address = self.entry_address.get()

        if not name or not phone:
            messagebox.showwarning("Input Error", "Name and Phone are required fields")
            return

        self.contacts.append({"Name": name, "Phone": phone, "Email": email, "Address": address})
        self.display_contacts()
        self.clear_fields()

    def display_contacts(self):
        for row in self.tree.get_children():
            self.tree.delete(row)

        for contact in self.contacts:
            self.tree.insert("", tk.END, values=(contact["Name"], contact["Phone"], contact["Email"], contact["Address"]))

    def clear_fields(self):
        self.entry_name.delete(0, tk.END)
        self.entry_phone.delete(0, tk.END)
        self.entry_email.delete(0, tk.END)
        self.entry_address.delete(0, tk.END)
        self.entry_search.delete(0, tk.END)

    def search_contact(self):
        search_term = self.entry_search.get().lower()
        for row in self.tree.get_children():
            self.tree.delete(row)

        for contact in self.contacts:
            if search_term in contact["Name"].lower() or search_term in contact["Phone"]:
                self.tree.insert("", tk.END, values=(contact["Name"], contact["Phone"], contact["Email"], contact["Address"]))

    def load_selected_contact(self, event):
        selected_item = self.tree.selection()[0]
        contact = self.tree.item(selected_item, "values")

        self.entry_name.delete(0, tk.END)
        self.entry_name.insert(0, contact[0])

        self.entry_phone.delete(0, tk.END)
        self.entry_phone.insert(0, contact[1])

        self.entry_email.delete(0, tk.END)
        self.entry_email.insert(0, contact[2])

        self.entry_address.delete(0, tk.END)
        self.entry_address.insert(0, contact[3])

    def update_contact(self):
        selected_item = self.tree.selection()
        if selected_item:
            index = self.tree.index(selected_item)
            self.contacts[index] = {
                "Name": self.entry_name.get(),
                "Phone": self.entry_phone.get(),
                "Email": self.entry_email.get(),
                "Address": self.entry_address.get()
            }
            self.display_contacts()
            self.clear_fields()
        else:
            messagebox.showwarning("Selection Error", "Please select a contact to update")

    def delete_contact(self):
        selected_item = self.tree.selection()
        if selected_item:
            index = self.tree.index(selected_item)
            del self.contacts[index]
            self.display_contacts()
        else:
            messagebox.showwarning("Selection Error", "Please select a contact to delete")

if __name__ == "__main__":
    root = tk.Tk()
    app = ContactBook(root)
    root.mainloop()
