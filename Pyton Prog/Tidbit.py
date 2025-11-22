"""
Author: Prisca Muleka
Date: 01/16/2025
Description: This program calculates a monthly payment plan, displaying interest, principal, and remaining balance until the loan is paid off. 
             It takes the purchase price as input and applies a 10% down payment.
"""
ANNUAL_RATE = 0.12  # Annual interest rate
MONTHLY_RATE = ANNUAL_RATE / 12  # Monthly interest rate
DOWNPAYMENT_RATE = 0.10  # Down payment rate
TABLEFORMATSTRING = "%2d%15.2f%15.2f%17.2f%17.2f%17.2f"  # Format for displaying the table

# Input: Get purchase price from the user
purchase_price = float(input("Enter the purchase price: "))

# Initialize variables
monthly_payment = 0.05 * purchase_price  # Monthly payment
downpayment = purchase_price * DOWNPAYMENT_RATE  # Down payment
balance = purchase_price - downpayment  # Balance after down payment
month = 1  # Start from month 1

# Display the table header
print("\nMonth  Starting Balance  Interest to Pay  Principal to Pay  Payment  Ending Balance")

# Process: Loop until the balance is paid off
while balance > 0:
    if monthly_payment > balance:
        # If the payment is more than the balance, set payment to the balance
        monthly_payment = balance
        interest = 0  # No interest if paying off the final balance
    else:
        # Calculate interest for the month
        interest = balance * MONTHLY_RATE

    # Calculate principal paid in this month
    principal = monthly_payment - interest
    # Calculate the remaining balance after payment
    remaining_balance = balance - monthly_payment

# Output
    # Display the payment details
    print(TABLEFORMATSTRING % (month, balance, interest, principal, monthly_payment, remaining_balance))

    # Update the balance for the next month
    balance = remaining_balance
    month += 1
