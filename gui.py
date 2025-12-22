# gui.py
import tkinter as tk
from tkinter import ttk, messagebox
from controller import *
from config import *
from database import init_db
def run_gui():
    init_db()

    root = tk.Tk()
    root.title("Mini Perpustakaan")
    root.geometry("900x500")
    root.configure(bg=BG_COLOR)

    tk.Label(
        root, text="MINI PERPUSTAKAAN",
        font=TITLE_FONT,
        bg=PRIMARY_COLOR, fg="white"
    ).pack(fill="x", pady=10)

    entry_title = tk.Entry(root, width=40)
    entry_title.pack()

    table = ttk.Treeview(root, columns=("id","title","author","year"), show="headings")
    table.pack(fill="both", expand=True)

    def refresh():
        table.delete(*table.get_children())
        for book in get_books_controller():
            table.insert("", tk.END, values=book)

    def add_gui():
        if add_book_controller(entry_title.get(), "Anonim", "2025"):
            refresh()
        else:
            messagebox.showwarning("Error", "Judul kosong")

    tk.Button(root, text="Tambah Buku", command=add_gui).pack()

    refresh()
    root.mainloop()