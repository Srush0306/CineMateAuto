import tkinter as tk
from PIL import Image, ImageTk
from user_login import launch_user_login
from admin_panel import launch_admin_login

def open_user_portal():
    root.destroy()
    launch_user_login()

def open_admin_portal():
    root.destroy()
    launch_admin_login()

root = tk.Tk()
root.title("CineMate Auto – Homepage")
root.geometry("800x600")
root.resizable(False, False)

# Background image
try:
    bg_image = Image.open("background.jpg.jpg")
    bg_image = bg_image.resize((800, 600), Image.Resampling.LANCZOS)
    bg_photo = ImageTk.PhotoImage(bg_image)
    bg_label = tk.Label(root, image=bg_photo)
    bg_label.place(x=0, y=0, relwidth=1, relheight=1)
except:
    root.configure(bg="gray")

# Overlay frame for title and buttons
overlay = tk.Frame(root, bg="black")
overlay.place(relx=0.5, rely=0.5, anchor="center")

tk.Label(
    overlay,
    text="🎬 Welcome to CineMate Auto",
    font=("Arial", 20, "bold"),
    bg="black",
    fg="white"
).pack(pady=20)

tk.Button(
    overlay,
    text="🎫 User Login",
    font=("Arial", 14),
    bg="#007bff",
    fg="white",
    width=20,
    command=open_user_portal
).pack(pady=10)

tk.Button(
    overlay,
    text="🛠 Admin Login",
    font=("Arial", 14),
    bg="#28a745",
    fg="white",
    width=20,
    command=open_admin_portal
).pack(pady=10)

tk.Label(
    root,
    text="© 2025 CineMate Technologies",
    font=("Arial", 10),
    bg="black",
    fg="white"
).pack(side="bottom", pady=5)

root.mainloop()
