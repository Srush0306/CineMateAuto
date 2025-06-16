import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import mysql.connector

def authenticate_user(username, password):
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="root123",
        database="cinemate"
    )
    cursor = conn.cursor()
    query = "SELECT * FROM users WHERE username=%s AND password=%s"
    cursor.execute(query, (username, password))
    result = cursor.fetchone()
    conn.close()
    return result

def handle_login(root, username_entry, password_entry):
    username = username_entry.get()
    password = password_entry.get()
    
    if authenticate_user(username, password):
        messagebox.showinfo("Success", f"Welcome, {username}!")
        root.destroy()
        import gui_app
        gui_app.main_window()
    else:
        messagebox.showerror("Login Failed", "Invalid username or password.")

def open_signup(root):
    root.destroy()
    import signup

def forgot_password(root):
    root.destroy()
    import forgot_password

def launch_user_login():
    root = tk.Tk()
    root.title("User Login")
    root.geometry("800x500")
    root.resizable(False, False)

    bg_image = Image.open("background.jpg.jpg")
    bg_image = bg_image.resize((800, 500))
    bg_photo = ImageTk.PhotoImage(bg_image)
    tk.Label(root, image=bg_photo).place(x=0, y=0, relwidth=1, relheight=1)

    login_frame = tk.Frame(root, bg="white", bd=2)
    login_frame.place(x=250, y=120, width=300, height=250)

    tk.Label(login_frame, text="Username:", font=("Arial", 12), bg="white").place(x=20, y=30)
    username_entry = tk.Entry(login_frame, font=("Arial", 12))
    username_entry.place(x=110, y=30, width=160)

    tk.Label(login_frame, text="Password:", font=("Arial", 12), bg="white").place(x=20, y=80)
    password_entry = tk.Entry(login_frame, font=("Arial", 12), show="*")
    password_entry.place(x=110, y=80, width=160)

    tk.Button(login_frame, text="Login", bg="#4CAF50", fg="white", font=("Arial", 12),
              command=lambda: handle_login(root, username_entry, password_entry)).place(x=100, y=130, width=100)

    tk.Button(login_frame, text="Sign Up", command=lambda: open_signup(root), bg="blue", fg="white", font=("Arial", 10)).place(x=30, y=180, width=100)

    tk.Button(login_frame, text="Forgot Password?", command=lambda: forgot_password(root), bg="gray", fg="white", font=("Arial", 10)).place(x=150, y=180, width=120)

    root.mainloop()
