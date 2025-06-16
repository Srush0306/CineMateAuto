import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk

def show_receipt_window(name, email=None):
    receipt = tk.Toplevel()
    receipt.title("Receipt Confirmation")
    receipt.geometry("500x350")

    # Load background image
    try:
        bg = Image.open("background.jpg.jpg")  # Make sure the image name and path is correct
        bg = bg.resize((500, 350), Image.Resampling.LANCZOS)
        bg_img = ImageTk.PhotoImage(bg)
        bg_label = tk.Label(receipt, image=bg_img)
        bg_label.image = bg_img
        bg_label.place(x=0, y=0, relwidth=1, relheight=1)
    except:
        receipt.configure(bg="white")

    container = tk.Frame(receipt, bg="white")
    container.place(relx=0.5, rely=0.2, anchor="n")

    # Heading
    tk.Label(container, text=f"\u2705 Payment Successful, {name}!", font=("Arial", 16, "bold"), fg="green", bg="white").pack(pady=10)
    tk.Label(container, text="Would you like us to email your receipt?", font=("Arial", 12), bg="white").pack(pady=10)

    choice = tk.StringVar(value="No")

    # Radio buttons for choice
    radio_frame = tk.Frame(container, bg="white")
    radio_frame.pack()

    tk.Radiobutton(radio_frame, text="Yes", variable=choice, value="Yes", bg="white", font=("Arial", 11)).pack(side="left", padx=20)
    tk.Radiobutton(radio_frame, text="No", variable=choice, value="No", bg="white", font=("Arial", 11)).pack(side="left", padx=20)

    # Email input (initially hidden)
    email_entry = tk.Entry(container, font=("Arial", 11))
    email_label = tk.Label(container, text="Enter Email:", font=("Arial", 11), bg="white")

    def handle_choice():
        if choice.get() == "Yes":
            email_label.pack(pady=5)
            email_entry.pack(pady=5)
        else:
            email_label.pack_forget()
            email_entry.pack_forget()

    choice.trace("w", lambda *args: handle_choice())

    def send_receipt():
        if choice.get() == "Yes":
            email_address = email_entry.get()
            if not email_address or "@" not in email_address:
                messagebox.showwarning("Input Error", "Please enter a valid email.")
                return
            messagebox.showinfo("Receipt Sent", f"Receipt sent to {email_address}")
        else:
            messagebox.showinfo("Done", f"Thank you for booking, {name}!")
        receipt.destroy()

    tk.Button(container, text="Submit", font=("Arial", 12), bg="#007bff", fg="white", command=send_receipt).pack(pady=15)

# For independent testing
if __name__ == "__main__":
    root = tk.Tk()
    root.withdraw()  # Hide root if testing separately
    show_receipt_window("Ashish")

    def check_closed():
        if not any(isinstance(w, tk.Toplevel) for w in root.winfo_children()):
            root.destroy()
        else:
            root.after(100, check_closed)

    check_closed()
    root.mainloop()
