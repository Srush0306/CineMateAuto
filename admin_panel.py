import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
from admin_dashboard import show_admin_panel  # ✅ Import the correct dashboard function

# Dummy admin credentials
ADMIN_USERNAME = "admin"
ADMIN_PASSWORD = "admin123"

def launch_admin_login():
    def handle_login():
        username = username_entry.get()
        password = password_entry.get()

        if username == ADMIN_USERNAME and password == ADMIN_PASSWORD:
            messagebox.showinfo("Login Successful", "Welcome, Admin!")
            root.withdraw()  # ✅ Hide login window instead of destroying it
            show_admin_panel(root)  # ✅ Pass root as parent
        else:
            messagebox.showerror("Login Failed", "Invalid username or password")

    root = tk.Tk()
    root.title("CineMate Admin Login")
    root.geometry("800x600")
    root.resizable(False, False)

    # Background image
    try:
        bg_image = Image.open("view-3d-cinema-theatre-room.jpg")
        bg_image = bg_image.resize((800, 600), Image.Resampling.LANCZOS)
        bg_photo = ImageTk.PhotoImage(bg_image)
        tk.Label(root, image=bg_photo).place(x=0, y=0, relwidth=1, relheight=1)
        root.bg_photo = bg_photo  # prevent garbage collection
    except:
        root.configure(bg="white")

    # Login Frame (centered)
    login_frame = tk.Frame(root, bg="white", bd=2)
    login_frame.place(relx=0.5, rely=0.5, anchor="center", width=350, height=250)

    tk.Label(login_frame, text="Admin Login", font=("Arial", 16, "bold"), bg="white").pack(pady=(15, 10))

    tk.Label(login_frame, text="Username", bg="white", anchor="w", font=("Arial", 12)).pack(fill="x", padx=20)
    username_entry = tk.Entry(login_frame, font=("Arial", 12))
    username_entry.pack(padx=20, pady=5, fill="x")

    tk.Label(login_frame, text="Password", bg="white", anchor="w", font=("Arial", 12)).pack(fill="x", padx=20)
    password_entry = tk.Entry(login_frame, font=("Arial", 12), show="*")
    password_entry.pack(padx=20, pady=5, fill="x")

    tk.Button(login_frame, text="Login", font=("Arial", 12), bg="green", fg="white", width=10, command=handle_login).pack(pady=15)

    root.mainloop()
