"Main.py- Order Now"

import tkinter as tk
from PIL import Image, ImageTk
from order import open_order_window

def main_window():
    root = tk.Tk()
    root.title("Pizza Delivery App")
    root.geometry("500x400")

    # Load an image
    img = Image.open("images/pizza.jpg")  #dont forget to download image
    img = img.resize((200,200))
    pizza_img = ImageTk.PhotoImage(img)

    # Display image
    label = tk.Button(root, text="Welcome to pizza Express", font==("Arial", 14, "bold"))
    label.pack(pady=10)

    
    #Order Button
    order_btn = tk.Button(root,text=)