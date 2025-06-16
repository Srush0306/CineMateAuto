import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import mysql.connector

def verify_and_reset():
    username = username_entry.get()
    security_answer = security_entry.get()
    new_password = new_password_entry.get()

    try:
        conn = mysql.connector.connect(host="localhost", user="root", password="root123", database="cinemate")
        cursor = conn.cursor()
        cursor.execute("SELECT security_question FROM users WHERE username=%s", (username,))
        result = cursor.fetchone()
        if result and result[0].lower().strip() == security_answer.lower().strip():
            cursor.execute("UPDATE users SET password=%s WHERE username=%s", (new_password, username))
            conn.commit()
            conn.close()
            messagebox.showinfo("Success", "Password reset successful! Redirecting to login...")
            root.destroy()
            import user_login
        else:
            messagebox.showerror("Error", "Incorrect security answer or username.")
    except Exception as e:
        messagebox.showerror("Database Error", str(e))

def go_back_to_login():
    root.destroy()
    import user_login

# -------- Tkinter GUI Setup --------
root = tk.Tk()
root.title("Forgot Password")
root.geometry("800x400")
root.resizable(False, False)

# Background Image
bg_img = Image.open("background.jpg.jpg")
bg_img = bg_img.resize((800, 400))
bg_photo = ImageTk.PhotoImage(bg_img)
tk.Label(root, image=bg_photo).place(x=0, y=0, relwidth=1, relheight=1)

# Reset Frame
frame = tk.Frame(root, bg="white", bd=2)
frame.place(x=200, y=100, width=400, height=260)

tk.Label(frame, text="Reset Password", font=("Arial", 14, "bold"), bg="white").pack(pady=10)

# Username
tk.Label(frame, text="Username", bg="white").pack(anchor='w', padx=20)
username_entry = tk.Entry(frame)
username_entry.pack(fill='x', padx=20, pady=5)

# Security Answer
tk.Label(frame, text="Answer to Security Question", bg="white").pack(anchor='w', padx=20)
security_entry = tk.Entry(frame)
security_entry.pack(fill='x', padx=20, pady=5)

# New Password
tk.Label(frame, text="New Password", bg="white").pack(anchor='w', padx=20)
new_password_entry = tk.Entry(frame, show="*")
new_password_entry.pack(fill='x', padx=20, pady=5)

# Buttons
btn_frame = tk.Frame(frame, bg="white")
btn_frame.pack(pady=10)

tk.Button(btn_frame, text="Submit", bg="green", fg="white", width=12, command=verify_and_reset).grid(row=0, column=0, padx=5)
tk.Button(btn_frame, text="Back to Login", bg="blue", fg="white", width=12, command=go_back_to_login).grid(row=0, column=1, padx=5)

root.mainloop()
