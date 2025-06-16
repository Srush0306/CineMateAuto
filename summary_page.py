import tkinter as tk
from PIL import Image, ImageTk
from payment_page import show_payment_page  # Import from payment module
import random

def show_summary_window(name, phone, movie_info, tickets):
    summary = tk.Toplevel()
    summary.title("Booking Summary & Payment")
    summary.geometry("600x450")  # Larger size for better UI

    # Background Image
    try:
        bg_img = Image.open("login.jpg.jpg")  # Make sure this exists
        bg_img = bg_img.resize((600, 450), Image.Resampling.LANCZOS)
        bg_photo = ImageTk.PhotoImage(bg_img)

        bg_label = tk.Label(summary, image=bg_photo)
        bg_label.image = bg_photo
        bg_label.place(x=0, y=0, relwidth=1, relheight=1)
    except Exception as e:
        print("Background image not loaded:", e)
        summary.configure(bg="white")

    # Container Frame
    container = tk.Frame(summary, bg="#ffffe0", bd=2, relief="groove")
    container.place(relx=0.5, rely=0.15, anchor="n")

    tk.Label(container, text="Booking Summary", font=("Arial", 16, "bold"), bg="#ffffe0").pack(pady=10)

    # Info Section
    info_frame = tk.Frame(summary, bg="#ffffe0")
    info_frame.place(relx=0.5, rely=0.35, anchor="center")

    tk.Label(info_frame, text=f"Name: {name}", font=("Arial", 12), bg="#ffffe0").pack(pady=2)
    tk.Label(info_frame, text=f"Phone: {phone}", font=("Arial", 12), bg="#ffffe0").pack(pady=2)
    tk.Label(info_frame, text=f"Movie: {movie_info}", font=("Arial", 12), bg="#ffffe0", wraplength=500).pack(pady=2)
    tk.Label(info_frame, text=f"Tickets: {tickets}", font=("Arial", 12), bg="#ffffe0").pack(pady=2)

    # Button Section
    button_frame = tk.Frame(summary, bg="#ffffe0")
    button_frame.place(relx=0.5, rely=0.75, anchor="center")

    def submit_and_proceed():
        try:
            # Generate random price per ticket for fun variation
            price_per_ticket = random.choice([120, 130, 150])
            total_amount = int(tickets) * price_per_ticket
        except:
            total_amount = 0

        summary.destroy()  # Close current window
        show_payment_page(name, phone, movie_info, tickets, total_amount)  # Pass to payment window with all info

    tk.Button(button_frame, text="✅ Submit", font=("Arial", 12), bg="#28a745", fg="white",
              command=submit_and_proceed).grid(row=0, column=0, padx=20, pady=10)

    tk.Button(button_frame, text="🧹 Clear", font=("Arial", 12), bg="#dc3545", fg="white",
              command=summary.destroy).grid(row=0, column=1, padx=20, pady=10)

# Optional standalone test
if __name__ == "__main__":
    root = tk.Tk()
    root.withdraw()
    show_summary_window("Srushti", "9999999999", "CineVerse: The Rise", 2)
    root.mainloop()
