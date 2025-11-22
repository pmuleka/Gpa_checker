from tkinter import *
from PIL import ImageTk, Image

pizza = Tk()
pizza.geometry("600x500")
pizza.title("Pizz-out")


name_label = Label(pizza, text="what is your name?")
name_label.grid(row=0, column=0)

name_entry = Entry(pizza,width= 30)
name_entry.grid(row=0, column=1)

address_label = Label(pizza, text="what is your address?")
address_label.grid(row=1, column=0)

address_entry = Entry(pizza,width= 30)
address_entry.grid(row=1, column=1)

phone_label = Label(pizza, text="what is your name?")
phone_label.grid(row=2, column=0)


phone_entry = Entry(pizza,width= 20)
phone_entry.grid(row=2, column=1)


#Create pizza list
my_pizza_list = ["pepperoni", "cheese", "Mushroom", "Steak", "Hawaienne"]


pizza_list = Listbox(pizza, selectmode= MULTIPLE, bg="pink", fg="black")
pizza_list.grid(row=4, column=1)

for item in my_pizza_list:
    pizza_list.insert(0, item)






def add_pizza():
    result = ""
    for item in pizza_list.curselection():
        result = result + str(pizza_list.get(item)) + "\n"

        add_lbl.config(text="Your Pizza Selection: " + "\n" + result)


add_lbl = Label(pizza, text="")
add_lbl.grid(row=5, column=1)        


add_button = Button(pizza, text="Add Pizza", command= add_pizza)
add_button.grid( row=5, column=0)


def check():
    text1 = name_entry.get()
    new_lbl = Label(pizza, text="Name: " + text1)
    new_lbl.grid(row=5,column=2)

text2 = address_entry.get()
new_lbl2 = Label(pizza, text=text2)
new_lbl2.grid(row=6,column=2)

text3 = phone_entry.get()
new_lbl3 = Label(pizza, text=text3) 
new_lbl3.grid(row=7,column=2)




check_button = Button(pizza, text="Checkout", command=check)
check_button.grid(row=6, column=0)


def deleteme():
    pizza_list.delete(0,5)


del_button = Button(pizza, text="Delete Pizza", command=deleteme)
del_button.grid(row=7, column=0)


drinks = StringVar()
drinks.set("Choose a drink")

drink = OptionMenu(pizza, drinks, "pinacolada", "Exotic", "fanta", "Root Beer")
drink.grid(row=8,column=0)
drink_pic = Image.open("pinacolada")


# Open and Resize image

pizza_pic = Image.open("beef.png")
new_width = int(pizza_pic.width / 8.8)
new_height = int(pizza_pic.height / 8.8)
new_size = (new_width, new_height)
beefpng = ImageTk.PhotoImage(pizza_pic.resize(new_size))



pic_lbl = Label(pizza, image= beefpng)
pic_lbl.grid(row=1, column=7)

def exitme():
    answer = messagebox.askyesno("Hi", "Are you sure to exit?")
if answer == 1:
   pizza.destroy()
else:
     return

exit_button = Button(pizza, text="Exit Me")
exit_button.grid(row=4, column=7)




pizza.mainloop()


