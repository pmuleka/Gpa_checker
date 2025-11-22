"""
   Day 5 hands on simulate two dice rolling.  Doa apecified number of times
     with and without a "seed" number.  Encase in a while loop to allow
     multiple iterations of our code in run of the progress.
     Prisca Muleka 4/1/2024
"""
def main():
    import random # built in pseudorandom number generator in Python
    another = 'y' # while loop terminator value.  initialize to run once
    while (another== 'y'):
        numRoll = int(input("Enter number of rolls as an integer: "))
        seedNo  = int(input("Enter optional seed number (0 not to declare): "))
        if (seedNo > 0):
            random.seed(seedNo)  # numbers predictable with seed number known
        for x in range(numRoll):
            result = random.randint(1,6) + random.randint(1,6)
            print(result)
        another = input('Another run?(y):  ') # continue our loop
    print("End program")
#call main ()function/method here
main()
