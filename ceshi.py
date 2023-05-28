
import tkinter as tk
from tkinter import filedialog

class TextEditor(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.text_area = tk.Text(self, bg='white', fg='black', font=('Arial', 12))
        self.text_area.pack(side="top", fill="both", expand=True)

        self.menu_bar = tk.Menu(self.master, bg='white', fg='black', font=('Arial', 12))
        self.file_menu = tk.Menu(self.menu_bar, tearoff=0, bg='white', fg='black', font=('Arial', 12))
        self.file_menu.add_command(label="Open", command=self.open_file)
        self.file_menu.add_command(label="Save", command=self.save_file)
        self.file_menu.add_separator()
        self.file_menu.add_command(label="Exit", command=self.master.destroy)
        self.menu_bar.add_cascade(label="File", menu=self.file_menu)

        self.master.config(menu=self.menu_bar)

    def open_file(self):
        file_path = filedialog.askopenfilename()
        if file_path:
            with open(file_path, "r") as file:
                self.text_area.delete("1.0", "end")
                self.text_area.insert("1.0", file.read())

    def save_file(self):
        file_path = filedialog.asksaveasfilename()
        if file_path:
            with open(file_path, "w") as file:
                file.write(self.text_area.get("1.0", "end"))

root = tk.Tk()
app = TextEditor(master=root)
app.mainloop()


