import tkinter as tk
from tkinter import ttk

from models.config import *

class TableApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Товарный помощник")
        
        

        self.labels = list(metadata.tables['good'].columns.keys())

        # Create a table
        self.tree = ttk.Treeview(root, columns=self.labels, show="headings")
        for col in self.labels:
            self.tree.heading(col, text=col)
        self.tree.grid(row=2, column=0, columnspan=len(self.labels), padx=5, pady=5,sticky='nsew')



          # Labels & Edits
        for i, label_text in enumerate(self.labels):
            label = tk.Label(root, text=label_text)
            label.grid(row=3, column=i, padx=5, pady=5)

        self.entries = []
        for i in range(len(self.labels)):
            entry = tk.Entry(root)
            entry.grid(row=4, column=i, padx=5, pady=5)
            self.entries.append(entry)
       
         # CRUD Buttons
        self.insert_btn = tk.Button(root, text="Добавить/обновить запись", command=None)
        self.insert_btn.grid(row=5, columnspan=len(self.labels), padx=5, pady=5)

        self.upd_btn = tk.Button(root, text="Удалить запись", command=None)
        self.upd_btn.grid(row=5,column=1, columnspan=len(self.labels), padx=5, pady=5)

    def submit_data(self):
        data = [entry.get() for entry in self.entries]
        self.tree.insert("", "end", values=data)
        # Clear entry fields after submission
        for entry in self.entries:
            entry.delete(0, "end")

if __name__ == "__main__":
    root = tk.Tk()
    app = TableApp(root)
    root.mainloop()
