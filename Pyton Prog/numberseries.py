""" 
PRISCA MULEKA
02/02/2025
# Description: This program has two parts:
  1. Calculating the sum of digits from a string of numbers entered by the user.
  2. Writing a series of random numbers to a file and displaying them to the console.
"""

# Part 1: Sum of Digits

# Function to add up the digits of a number entered as a string

def sum_of_digits():
    # Ask the user to enter a series of digits
    numbers = input("Enter a series of single-digit numbers (no spaces): ")

    # Initialize the sum to 0
    total_sum = 0
    
    # Loop through each character in the string and add its value to the sum
    for digit in numbers:
        if digit.isdigit():  # Check if it's a digit
            total_sum += int(digit)

    # Print the total sum of the digits

    print(f"The sum of the digits is {total_sum}.")

# Part 2: Write Random Numbers to a File

# Function to create and save random numbers to a file

def write_random_numbers_to_file():

    # Ask the user how many random numbers they want
    num_of_random_numbers = int(input("How many random numbers do you want to generate? "))

    # Open the file to write random numbers
    
    with open("random_numbers.txt", "w") as file:
        for _ in range(num_of_random_numbers):
            # Create a random number between 1 and 500
            random_number = randint(1, 500)
            # Write the random number to the file
            file.write(str(random_number) + "/n")

    # Open the file again to read and display the random numbers

    print("Here are the random numbers from the file:")
    with open("random_numbers.txt", "r") as file:
        for line in file:
            print(line.strip())

# Import the randint function to create random numbers
from random import randint

# Run the functions
sum_of_digits()
write_random_numbers_to_file()




