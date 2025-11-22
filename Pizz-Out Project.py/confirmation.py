#Confirmation

import tkinter as tk

def show_confirmation_window(root):
    # Create a new window for the confirmation
    confirm_window = tk.Toplevel(root)
    confirm_window.title("Order Confirmation")
    confirm_window.geometry("300x150")

    # Display the confirmation message
    confirm_label = tk.Label(confirm_window, text="Your order has been confirmed!\nThank you for ordering.", font=("Arial", 12))
    confirm_label.pack(pady=30)

    # Close button
    close_button = tk.Button(confirm_window, text="Close", command=confirm_window.destroy)
    close_button.pack(pady=10)
