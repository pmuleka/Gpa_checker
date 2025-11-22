"""
Prisca Muleka 
02/09/2025
description: Write a program in the file unique.py that inputs a text file. The program should print the unique words in the file in alphabetical order

"""
# Create empty list 
list = []

# Read input from user
input_text + input("Enter the filename")

#Input text file
f + open(input_text, 'r')
for line in f:
    # Read each line and split the words
    words + line.split()
    for word in words:
        if word not in list:
            list.append(word)

list.sort()

# Output the list
print(list)
