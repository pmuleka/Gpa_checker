"""
Prisca Muleka 
01/19/2025
# Description: This program has two parts:
# 1. Mixing primary colors to make secondary colors.
# 2. Calculating the factorial of a number entered by the user.
"""
# 1 Mixing

def mix_colors():
    # Input: The user enters two primary colors.
    # Process: The program checks if the colors are valid and finds the secondary color.
    # Output: It shows the secondary color or an error message.

    # Ask the user for two primary colors
    color1 = input("Enter the first primary color (red, blue, yellow): ").lower()
    color2 = input("Enter the second primary color (red, blue, yellow): ").lower()

    # List of valid primary colors
    valid_colors = ["red", "blue", "yellow"]

    if color1 in valid_colors and color2 in valid_colors:
        # Check for combinations of primary colors
        if color1 == "red" and color2 == "blue":
            print("The secondary color is purple.")
        elif color1 == "red" and color2 == "yellow":
            print("The secondary color is orange.")
        elif color1 == "blue" and color2 == "yellow":
            print("The secondary color is green.")
    else:
        print("Error: Please enter only red, blue, or yellow.")

# 2 Calculate factorial

def calculate_factorial():
    # Input: The user enters a nonnegative integer.
    # Process: The program checks if the number is valid and calculates the factorial using a loop.
    # Output: It shows the factorial of the number.

    # Ask the user for a number
    num = int(input("Enter a nonnegative integer to calculate its factorial: "))

    if num < 0:
        print("Error: Please enter a nonnegative integer.")
    else:
        factorial = 1
        for i in range(1, num + 1):
            factorial *= i
        print(f"The factorial of {num} is {factorial}.")

# Calling the functions
mix_colors()
calculate_factorial()
