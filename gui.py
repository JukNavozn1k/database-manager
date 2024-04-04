import tkinter as tk
from tkinter import ttk

class TableApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Table App")

        self.labels = ["Name", "Age", "Occupation"]

        # Create labels and entry widgets
        for i, label_text in enumerate(self.labels):
            label = tk.Label(root, text=label_text)
            label.grid(row=0, column=i, padx=5, pady=5)

        # Create entry widgets
        self.entries = []
        for i in range(len(self.labels)):
            entry = tk.Entry(root)
            entry.grid(row=1, column=i, padx=5, pady=5)
            self.entries.append(entry)

        # Create a button
        self.button = tk.Button(root, text="Submit", command=self.submit_data)
        self.button.grid(row=2, columnspan=len(self.labels), padx=5, pady=5)

        # Create a table
        self.tree = ttk.Treeview(root, columns=self.labels, show="headings")
        for col in self.labels:
            self.tree.heading(col, text=col)
        self.tree.grid(row=3, column=0, columnspan=len(self.labels), padx=5, pady=5)

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
