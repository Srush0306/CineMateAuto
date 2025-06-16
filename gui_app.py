import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import mysql.connector
import re
from summary_page import show_summary_window  # External import

def connect_db():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="root123",
        database="cinemate"
    )

def show_movies():
    db = None
    try:
        db = connect_db()
        cursor = db.cursor()
        cursor.execute("SELECT * FROM movies")
        movies = cursor.fetchall()
        movie_list.delete(0, tk.END)

        if not movies:
            movie_list.insert(tk.END, "No movies available.")
        else:
            for idx, movie in enumerate(movies, start=1):
                movie_info = f"{idx}. {movie[1]} ({movie[2]}) — {movie[3]} | Screen: {movie[4]}"
                movie_list.insert(tk.END, movie_info)

    except Exception as e:
        messagebox.showerror("Error", f"Could not fetch movies.\n{e}")
    finally:
        if db:
            db.close()

def clear_fields():
    name_entry.delete(0, tk.END)
    phone_entry.delete(0, tk.END)
    tickets_entry.delete(0, tk.END)
    movie_list.selection_clear(0, tk.END)

def book_ticket():
    customer_name = name_entry.get().strip()
    phone = phone_entry.get().strip()
    num_tickets = tickets_entry.get().strip()
    selected_index = movie_list.curselection()

    if not customer_name or not phone or not num_tickets:
        messagebox.showwarning("Input Error", "Please fill all fields.")
        return
    if not customer_name.replace(" ", "").isalpha():
        messagebox.showwarning("Name Error", "Name must contain only alphabets.")
        return
    if not re.fullmatch(r'\d{10}', phone):
        messagebox.showwarning("Phone Error", "Phone number must be exactly 10 digits.")
        return
    if not num_tickets.isdigit() or int(num_tickets) < 1:
        messagebox.showwarning("Ticket Error", "Enter a valid number of tickets (1 or more).")
        return
    if not selected_index:
        messagebox.showwarning("Selection Error", "Please select a movie to book.")
        return

    show_details = movie_list.get(selected_index)
    try:
        movie_id = int(show_details.split('.')[0])
    except:
        messagebox.showerror("Error", "Invalid movie selection format.")
        return

    match = re.search(r'— (.*?) \| Screen: (.+)', show_details)
    if match:
        show_time = match.group(1).strip()
        screen = match.group(2).strip()
    else:
        show_time = ''
        screen = ''

    db = None
    try:
        db = connect_db()
        cursor = db.cursor()
        cursor.execute(
            "INSERT INTO bookings (customer_name, phone, movie_id, show_time, screen, num_tickets) VALUES (%s, %s, %s, %s, %s, %s)",
            (customer_name, phone, movie_id, show_time, screen, int(num_tickets))
        )
        db.commit()
        show_summary_window(customer_name, phone, show_details, num_tickets)
    except Exception as e:
        messagebox.showerror("Booking Error", f"Failed to book ticket.\n{e}")
    finally:
        if db:
            db.close()

def main_window():
    global movie_list, name_entry, phone_entry, tickets_entry

    root = tk.Tk()
    root.title("CineMate Auto – Movie Booking App")
    root.geometry("800x700")

    # Background Image Layer
    try:
        bg_img = Image.open("login.jpg.jpg")
        bg_img = bg_img.resize((800, 700), Image.Resampling.LANCZOS)
        bg_photo = ImageTk.PhotoImage(bg_img)
        bg_label = tk.Label(root, image=bg_photo)
        bg_label.image = bg_photo  # Prevent garbage collection
        bg_label.place(x=0, y=0, relwidth=1, relheight=1)
    except:
        root.configure(bg="white")

    # Main container on top of background
    container = tk.Frame(root, bg="white")
    container.place(relwidth=1, relheight=1)

    tk.Label(container, text="Welcome to CineMate Auto", font=("Arial", 20, "bold"),
             bg="lightgray", pady=10).pack(fill=tk.X)

    tk.Label(container, text="🎬 Available Movies & Shows:", font=("Arial", 14, "underline"),
             fg="black", bg="white", pady=10).pack()

    movie_list = tk.Listbox(container, width=100, height=12, font=("Arial", 11))
    movie_list.pack(pady=10)

    form_frame = tk.Frame(container, bg="white")
    form_frame.pack(pady=10)

    tk.Label(form_frame, text="Your Name:", bg="white", font=("Arial", 12)).grid(row=0, column=0, padx=5, pady=5, sticky="e")
    name_entry = tk.Entry(form_frame, width=30, font=("Arial", 12))
    name_entry.grid(row=0, column=1, padx=5, pady=5)

    tk.Label(form_frame, text="Phone Number:", bg="white", font=("Arial", 12)).grid(row=1, column=0, padx=5, pady=5, sticky="e")
    phone_entry = tk.Entry(form_frame, width=30, font=("Arial", 12))
    phone_entry.grid(row=1, column=1, padx=5, pady=5)

    tk.Label(form_frame, text="No. of Tickets:", bg="white", font=("Arial", 12)).grid(row=2, column=0, padx=5, pady=5, sticky="e")
    tickets_entry = tk.Entry(form_frame, width=30, font=("Arial", 12))
    tickets_entry.grid(row=2, column=1, padx=5, pady=5)

    action_frame = tk.Frame(container, bg="white")
    action_frame.pack(pady=20)

    tk.Button(action_frame, text="🎟 Book Ticket", font=("Arial", 12, "bold"),
              bg="#28a745", fg="white", width=15, command=book_ticket).grid(row=0, column=0, padx=20)

    tk.Button(action_frame, text="🧹 Clear", font=("Arial", 12, "bold"),
              bg="#dc3545", fg="white", width=15, command=clear_fields).grid(row=0, column=1, padx=20)

    show_movies()
    root.mainloop()

if __name__ == "__main__":
    main_window()
