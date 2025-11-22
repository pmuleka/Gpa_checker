""" Day 13 Spilt string characters that make it up display
      individual character as well as the ASII valur assigned to it.
      Prisca Muleka
"""
data = input("Enter a string of characters (enter to exit): ") # priming input
while data != "":
    for i in range(len(data)):   # loop fo examine each character of inpt string
        print(i," ",data[i]," ",ord(data[i])) # show counter, char, & ASCII
    data = input("Enter the next string (enter to exit): ")
print("End Program")
