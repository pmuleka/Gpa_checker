"""
Prisca Muleka 
02/15/2025
Description: This program asks the user to input a number greater than 1 and finds all prime numbers up to that number.
             It creates a list of numbers starting from 2 and goes up to the number the user entered.
             Then, it checks each number using the is prime function to see if it's prime. 
             If a number is prime, it shows up in the output.
"""
# Part I: Find Prime Numbers

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

# Input
num = int(input("Enter an integer greater than 1: "))

# Create a list of numbers from 2 to user input
numbers = list(range(2, num + 1))

#Output

# Print prime numbers
print("Prime numbers up to", num, ":")
for n in numbers:
    if is_prime(n):
        print(n)

# Part II: Get Top Three Items Price

# Data
data = {'Apple': 0.50, 'Banana': 0.20, 'Mango': 0.99, 'Coconut': 2.99, 'Pineapple': 3.99}

# Sort items by price in order
sorted_items = sorted(data.items(), key=lambda item: item[1], reverse=True)

#Output15

# Print top three most expensive items
print("\nTop three most expensive items:")
for item, price in sorted_items[:3]:
    print(item, price)
