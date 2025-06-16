import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import re
import mysql.connector

# ---------- Validation Functions ----------
def validate_email(email):
    return re.match(r"[^@]+@[^@]+\.[^@]+", email)

def validate_phone(phone):
    return phone.isdigit() and len(phone) == 10

def validate_name(name):
    return name.replace(" ", "").isalpha()

def validate_password(password):
    return (
        len(password) >= 7 and
        re.search(r'[A-Z]', password) and
        re.search(r'[a-z]', password) and
        re.search(r'[0-9]', password) and
        re.search(r'[!@#$%^&*(),.?":{}|<>]', password)
    )

# ---------- Register Function ----------
def register_user():
    name = name_entry.get()
    email = email_entry.get()
    phone = phone_entry.get()
    username = username_entry.get()
    password = password_entry.get()
    security_q = security_question_entry.get()
    security_ans = security_answer_entry.get()

    if not validate_name(name):
        messagebox.showerror("Invalid Name", "Name must contain alphabets only.")
        return
    if not validate_email(email):
        messagebox.showerror("Invalid Email", "Please enter a valid email.")
        return
    if not validate_phone(phone):
        messagebox.showerror("Invalid Phone", "Phone number must be 10 digits.")
        return
    if not validate_password(password):
        messagebox.showerror("Invalid Password", "Password must have 7+ characters, uppercase, lowercase, number, special char.")
        return
    if not security_q.strip() or not security_ans.strip():
        messagebox.showerror("Incomplete", "Please provide both security question and answer.")
        return

    try:
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="root123",
            database="cinemate"
        )
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO users (name, email, phone, username, password, security_question, security_answer)
            VALUES (%s, %s, %s, %s, %s, %s, %s)
        """, (name, email, phone, username, password, security_q, security_ans))
        conn.commit()
        conn.close()
        messagebox.showinfo("Success", "Signup successful! Redirecting to login...")
        root.destroy()
        import user_login
    except mysql.connector.IntegrityError:
        messagebox.showerror("Error", "Username already exists.")
    except Exception as e:
        messagebox.showerror("Database Error", str(e))

# ---------- Tkinter GUI ----------
root = tk.Tk()
root.title("User Signup")
root.geometry("900x600")
root.resizable(False, False)

# Background Image
bg_img = Image.open("login.jpg.jpg")
bg_img = bg_img.resize((900, 600))
bg_photo = ImageTk.PhotoImage(bg_img)
tk.Label(root, image=bg_photo).place(x=0, y=0, relwidth=1, relheight=1)

# Signup Frame
frame = tk.Frame(root, bg="white", bd=2)
frame.place(x=250, y=50, width=400, height=500)

tk.Label(frame, text="User Signup", font=("Arial", 16, "bold"), bg="white").pack(pady=10)

# Input Fields
tk.Label(frame, text="Full Name", bg="white").pack(anchor='w', padx=20)
name_entry = tk.Entry(frame, font=("Arial", 12))
name_entry.pack(fill='x', padx=20, pady=5)

tk.Label(frame, text="Email", bg="white").pack(anchor='w', padx=20)
email_entry = tk.Entry(frame, font=("Arial", 12))
email_entry.pack(fill='x', padx=20, pady=5)

tk.Label(frame, text="Phone", bg="white").pack(anchor='w', padx=20)
phone_entry = tk.Entry(frame, font=("Arial", 12))
phone_entry.pack(fill='x', padx=20, pady=5)

tk.Label(frame, text="Username", bg="white").pack(anchor='w', padx=20)
username_entry = tk.Entry(frame, font=("Arial", 12))
username_entry.pack(fill='x', padx=20, pady=5)

tk.Label(frame, text="Password", bg="white").pack(anchor='w', padx=20)
password_entry = tk.Entry(frame, font=("Arial", 12), show="*")
password_entry.pack(fill='x', padx=20, pady=5)

tk.Label(frame, text="Security Question", bg="white").pack(anchor='w', padx=20)
security_question_entry = tk.Entry(frame, font=("Arial", 12))
security_question_entry.pack(fill='x', padx=20, pady=5)

tk.Label(frame, text="Answer", bg="white").pack(anchor='w', padx=20)
security_answer_entry = tk.Entry(frame, font=("Arial", 12))
security_answer_entry.pack(fill='x', padx=20, pady=5)

# Signup Button
tk.Button(frame, text="Sign Up", bg="green", fg="white", font=("Arial", 12),
          command=register_user).pack(pady=15)

# Back to Login
tk.Button(frame, text="Back to Login", bg="blue", fg="white", font=("Arial", 10),
          command=lambda: [root.destroy(), __import__("user_login")]).pack()

root.mainloop()
