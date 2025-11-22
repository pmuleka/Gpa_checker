#Ordersum

import tkinter as tk

def open_order_window(root, pizza, drink, quantity):
    # Create a new window for the order summary
    order_window = tk.Toplevel(root)
    order_window.title("Order Summary")
    order_window.geometry("400x250")

    # Display order details
    summary_label = tk.Label(order_window, text=f"Pizza: {pizza}\nDrink: {drink}\nQuantity: {quantity}", font=("Arial", 12))
    summary_label.pack(pady=20)

    # Confirm Order button
    confirm_button = tk.Button(order_window, text="Confirm Order", command=order_window.destroy)
    confirm_button.pack(pady=10)

    # Close button
    close_button = tk.Button(order_window, text="Close", command=order_window.destroy)
    close_button.pack(pady=5)
