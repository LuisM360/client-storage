import tkinter as tk
import sqlite3


class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()

        # Connect to the database and create the table if it doesn't exist
        conn = sqlite3.connect("database.db")
        c = conn.cursor()
        c.execute('''CREATE TABLE IF NOT EXISTS records
                     (name text, address text, amount real)''')
        conn.commit()
        conn.close()

    def create_widgets(self):
        self.name_label = tk.Label(self, text="Name:")
        self.name_label.pack()
        self.name_entry = tk.Entry(self)
        self.name_entry.pack()

        self.address_label = tk.Label(self, text="Address:")
        self.address_label.pack()
        self.address_entry = tk.Entry(self)
        self.address_entry.pack()

        self.amount_label = tk.Label(self, text="Amount:")
        self.amount_label.pack()
        self.amount_entry = tk.Entry(self)
        self.amount_entry.pack()

        self.submit_button = tk.Button(self, text="Submit",
                                       command=self.submit)
        self.submit_button.pack()

    def submit(self):
        # Get the values from the entry widgets
        name = self.name_entry.get()
        address = self.address_entry.get()
        amount = self.amount_entry.get()

        # Connect to the database
        conn = sqlite3.connect("database.db")
        c = conn.cursor()

        # Insert the values into the table
        c.execute("INSERT INTO records VALUES (?, ?, ?)", (name, address, amount))

        # Commit the changes and close the connection
        conn.commit()
        conn.close()


root = tk.Tk()
app = Application(master=root)
app.mainloop()
