""" Day 10 hands on simulate rolling two 6-sided dice a specified number of
      times. Record results in list table. When complete distribution
      as well as theoretical probability.
      Prisca Muleka 4/17/2024
"""
def main():
    another = 'y'   # for multiple runs with different nummbers
    expectedProb=[0,0,1/36,2/36,3/36,4/36,5/36,6/36,5/36,4/36,3/36,2/36,1/36]
    import random  # invoke python randit method/function
    while (another == 'y'):
        result2Dice = [0] * 13  #table holds actual roll values conters
        #initialize actual counts table note ignore zero and 1
        numRoll = int(input("Enter number rolls desired as an integer:"))
        for x in range(numRoll):
            result=random.randint(1,6) + random.randint(1,6) # roll and store
            result2Dice[result] +=1   # bump list counter
            #print(result)     # diagnostics only
        print("Num----Total Act Actual Pct           Expected Pct") # heading
        for i in range(2,13,1): # roll through numbers 2 through 12
            resultPct = result2Dice[i]/numRoll  # compute percentage of total
            print(f'{i:3} - {result2Dice[i]:7}   {resultPct:^7.2%} \
                    {expectedProb[i]:^7.2%}')
        another = input('Another Run? (y): ')
main()  # call the main() module
            
