"""
# Author: Prisca Muleka
# Date:12/01/2025
# Description:
# This program will ask the user to enter numbers one by one. When the user presses Enter without typing a number, the program will stop taking inputs.
# It then will calculate and display the sum of all entered numbers and their average.
"""

# Input:
# The user will be asked to enter numbers one by one. 
# When the user presses Enter without typing anything, the program stops taking inputs.

# Initialize sum and count to 0
total_sum = 0  # This will add up all the numbers
count = 0       # This will count how many numbers we enter

# Process:
# The program will keep asking the user to enter numbers until the user presses Enter without typing anything.
number = input("Enter a number or press Enter to stop: ")

while number != "":
    try:
        # Add the number to the total sum
        total_sum += float(number)
        # Increase the count by 1
        count += 1
    except ValueError:
        # If the user enters something that's not a number, show an error
        print("Enter a valid number.")
    
    # Ask for another number
    number = input("Enter another number or press Enter to stop: ")

# Output:
# The program will show the total sum and the average of the numbers entered.
print(f"\nThe total sum is: {total_sum}")

# If the user entered at least one number, calculate the average
if count > 0:
    average = total_sum / count
    print(f"The average is: {average}")
else:4
    # If no number was entered, say so
    
#print("You didn't enter any numbers.")

