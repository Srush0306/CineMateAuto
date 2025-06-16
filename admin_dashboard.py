import tkinter as tk
from tkinter import ttk, Scrollbar
from PIL import Image, ImageTk
import mysql.connector

def show_admin_panel(parent=None):
    try:
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="root123",
            database="cinemate"
        )
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM bookings")
        bookings = cursor.fetchall()
        columns = [desc[0] for desc in cursor.description]
        conn.close()
    except Exception as e:
        print("Database error:", e)
        bookings = []
        columns = []

    panel = tk.Toplevel(parent)  # ✅ child of main app
    panel.title("Admin Dashboard - Bookings Overview")
    panel.geometry("850x550")
    panel.resizable(False, False)

    # Background image
    try:
        bg = Image.open("background.jpg.jpg")
        bg = bg.resize((850, 550), Image.Resampling.LANCZOS)
        bg_img = ImageTk.PhotoImage(bg)
        bg_label = tk.Label(panel, image=bg_img)
        bg_label.place(x=0, y=0, relwidth=1, relheight=1)
        panel.bg_img = bg_img  # prevent garbage collection
    except:
        panel.configure(bg="lightgray")

    # Frame for table
    frame = tk.Frame(panel, bg="white")
    frame.place(relx=0.5, rely=0.45, anchor="center", relwidth=0.9, relheight=0.7)

    tree = ttk.Treeview(frame, columns=columns, show="headings")
    tree.pack(side="left", fill="both", expand=True)

    scroll = Scrollbar(frame, orient="vertical", command=tree.yview)
    scroll.pack(side="right", fill="y")
    tree.configure(yscrollcommand=scroll.set)

    for col in columns:
        tree.heading(col, text=col)
        tree.column(col, width=100)

    for row in bookings:
        tree.insert("", "end", values=row)

    # Buttons
    tk.Button(panel, text="🔁 Return to Login", bg="#007bff", fg="white", font=("Arial", 12),
              command=panel.destroy).place(x=250, y=500)
    tk.Button(panel, text="❌ Exit", bg="red", fg="white", font=("Arial", 12),
              command=panel.quit).place(x=550, y=500)
