# gui_app.py

import tkinter as tk
from tkinter import messagebox
import database

def main_window():
    root = tk.Tk()
    root.title("🎬 CineMate Auto – Movie Booking App")
    root.geometry("600x400")
    root.config(bg="#f0f0f0")

    heading = tk.Label(root, text="Welcome to CineMate Auto", font=("Helvetica", 18, "bold"), bg="#f0f0f0")
    heading.pack(pady=20)

    info_label = tk.Label(root, text="Start booking your movie tickets!", font=("Arial", 12), bg="#f0f0f0")
    info_label.pack(pady=10)

    root.mainloop()

if __name__ == "__main__":
    main_window()
