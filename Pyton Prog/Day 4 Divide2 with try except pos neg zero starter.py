""" Day 4 Divide2 with try except pos neg zero starter.py - hands on
   Day 2b - Multiple two numbers, convert to Floating point,
            Process - multiply the two values and
            Output - display results along with echo of input.
            Prisca Muleka - 3/20/2024

   Day 4. Revise program.
          - multiply to divide. operation * to / as well as promprts
          - test result positive, negative, or zero and display
          - add try/except blocks to gracefully catch non-numeri errors
            as well as divide by zero.
            Prisca Muleka -3/27/2024

"""
try:
    num1s = input ("Enter first number to divide into: ") # get first numner
    num2s = input ("Enter second number to divide by : ") # and the second
    num1 = float(num1s)                       # Convert string to floating point    
    num2 = float(num2s)                       #    prepare to do arithmetic
    result = num1 / num2                   #process - multiply the two inputs to
    print("Result of ", num1s,  "divided by ", num2s, "is " + str(result), \
          end=" - ")# output.   Output includes echo of input.
    if result > 0:
        print("Positive")
    elif result < 0:
        print("Negative")
    else:
        print("Zero")
except ValueError:
    print("Input must be floating point number")
except ZeroDivisionError:
    print("Zero division - second operand can not be zero")
   
