import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
from receipt_page import show_receipt_window

def show_payment_page(name, phone, movie_info, tickets, total_amount):
    root = tk.Toplevel()
    root.title("Payment")
    root.geometry("500x350")

    # Background Image
    try:
        bg_img = Image.open("login.jpg.jpg")  # Use correct filename
        bg_img = bg_img.resize((500, 350), Image.Resampling.LANCZOS)
        bg_photo = ImageTk.PhotoImage(bg_img)

        bg_label = tk.Label(root, image=bg_photo)
        bg_label.image = bg_photo
        bg_label.place(x=0, y=0, relwidth=1, relheight=1)
    except Exception as e:
        print("Background not loaded:", e)
        root.configure(bg="white")

    container = tk.Frame(root, bg="white", bd=2)
    container.place(relx=0.5, rely=0.15, anchor="n")

    tk.Label(container, text="💳 Payment Page", font=("Arial", 16, "bold"), bg="white", fg="green").pack(pady=10)

    tk.Label(container, text=f"Total Amount: ₹{total_amount}", font=("Arial", 14), bg="white").pack(pady=10)

    option = tk.StringVar(value="Pay at Counter")
    tk.Radiobutton(container, text="Pay at Counter", variable=option, value="Pay at Counter", bg="white").pack()

    def submit_payment():
        messagebox.showinfo("Success", "Proceed to reciept")
        root.destroy()
        show_receipt_window(name)  # Only name is needed for receipt

    tk.Button(container, text="Submit", font=("Arial", 12), bg="#007bff", fg="white", command=submit_payment).pack(pady=10)
    tk.Button(container, text="Clear", font=("Arial", 12), bg="#dc3545", fg="white", command=root.destroy).pack(pady=5)

# Optional standalone test
if __name__ == "__main__":
    root = tk.Tk()
    root.withdraw()
    show_payment_page("Srushti", "9999999999", "Inception", 2, 300)
    root.mainloop()

