import sqlite3
import tkinter as tk
from tkinter import messagebox, ttk

# ================= DATABASE =================
DB_NAME = "perpustakaan.sqlite"
def connection():
    return sqlite3.connect(DB_NAME)

def init_db():
    conn = connection()
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS books (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT,
            author TEXT,
            year TEXT
        )
    """)
    conn.commit()
    conn.close()

def add_book(title, author, year):
    conn = connection()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO books (title, author, year) VALUES (?, ?, ?)",
        (title, author, year)
    )
    conn.commit()
    conn.close()

def get_all_books():
    conn = connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM books")
    rows = cursor.fetchall()
    conn.close()
    return rows

def search_books(keyword):
    conn = connection()
    cursor = conn.cursor()
    cursor.execute(
        "SELECT * FROM books WHERE title LIKE ? OR author LIKE ?",
        (f"%{keyword}%", f"%{keyword}%")
    )
    rows = cursor.fetchall()
    conn.close()
    return rows

def delete_book(book_id):
    conn = connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM books WHERE id = ?", (book_id,))
    conn.commit()
    conn.close()

# ================= GUI FUNCTION =================
def refresh_table():
    for row in table.get_children():
        table.delete(row)

    for book in get_all_books():
        table.insert("", tk.END, values=book)

def add_book_gui():
    title = entry_title.get()
    author = entry_author.get()
    year = entry_year.get()

    if not title or not author or not year:
        messagebox.showwarning("Peringatan", "Semua data harus diisi")
        return

    add_book(title, author, year)
    refresh_table()

    entry_title.delete(0, tk.END)
    entry_author.delete(0, tk.END)
    entry_year.delete(0, tk.END)

    messagebox.showinfo("Sukses", "Buku berhasil ditambahkan")

def delete_gui():
    selected = table.focus()
    if not selected:
        messagebox.showwarning("Peringatan", "Pilih buku terlebih dahulu")
        return

    book_id = table.item(selected)["values"][0]
    delete_book(book_id)
    refresh_table()
    messagebox.showinfo("Sukses", "Buku berhasil dihapus")

def search_gui():
    keyword = entry_search.get()

    if not keyword:
        refresh_table()
        messagebox.showwarning("PERINGATAN !","Input dulu buku yang mau anda cari !!")

        return

    results = search_books(keyword)

    for row in table.get_children():
        table.delete(row)

    for book in results:
        table.insert("", tk.END, values=book)
    messagebox.showinfo("INFORMASI !","Buku yang anda cari sudah ditemukan")

# ================= MAIN WINDOW =================
init_db()

root = tk.Tk()
root.title("PROJEK UAS ALPRO ")
root.geometry("700x500")
root.configure(bg ="#079bfd")

#==================TITLE========================
tk.Label(
    root,
    text = "MINI PERPUSTAKAAN",
    font=("Segoe UI", 20,"bold"),
    bg= "#079bfd",
    fg= "#f2f2f2"
).pack(pady= 10)

# ================= FORM INPUT =================
frame_form = tk.Frame(root, bg= "#f2f2f2", bd=2, relief="groove")
frame_form.pack(padx=10 , pady=10)

tk.Label(frame_form, text="JUDUL BUKU :", bg="#f2f2f2", fg="#010101",font=("Arial",10,"bold")).grid(row=0, column=0, sticky="w")
entry_title = tk.Entry(frame_form, width=30)
entry_title.grid(row=0, column=1, padx=5)

tk.Label(frame_form, text="PENULIS :", bg = "#f2f2f2", fg= "#010101", font = ("Arial", 10 ,"bold")).grid(row=1, column=0, sticky="w")
entry_author = tk.Entry(frame_form, width=30)
entry_author.grid(row=1, column=1, padx=5)

tk.Label(frame_form, text="TAHUN TERBIT :", bg= "#f2f2f2", fg= "#010101", font= ("Arial", 10, "bold")).grid(row=2, column=0, sticky="w")
entry_year = tk.Entry(frame_form, width=30)
entry_year.grid(row=2, column=1, padx=5)

# ================= BUTTON =================
frame_btn = tk.Frame(root, bg="#079bfd")
frame_btn.pack(pady=10)

tk.Button(frame_btn, text="Tambah Buku", command=add_book_gui).grid(row=0, column=0, padx=5)
tk.Button(frame_btn, text="Hapus Buku", command=delete_gui).grid(row=0, column=1, padx=5)

# ================= SEARCH =================
frame_search = tk.Frame(root, bg="#f2f2f2")
frame_search.pack(pady=5)

tk.Label(frame_search, text="Cari Buku:", bg="#f2f2f2").pack(side=tk.LEFT)

entry_search = tk.Entry(frame_search, width=30)
entry_search.pack(side=tk.LEFT, padx=5)

frame_bttn2 = tk.Frame( bg= "#079bfd")
frame_bttn2.pack(pady=5, side = tk.TOP)

tk.Button(
    frame_bttn2, text="Cari",
    bg="#f2f2f2", fg="#080808",
    command=search_gui
).pack(side=tk.LEFT, padx=5)

tk.Button(
    frame_bttn2, text="Reset",
    command=refresh_table
).pack(side=tk.LEFT)

# ================= TABLE =================
columns =("ID", "Judul", "Penulis", "Tahun")
table = ttk.Treeview(root, columns=columns, show="headings")

for col in columns:
    table.heading(col, text=col)
    table.column(col, width=150)

table.pack(expand=True, fill="both", padx=10, pady=10)

refresh_table()
root.mainloop()