""" Day 14 program 1 generate a specified number of random numbers
      between 1 and 500. write to created text file number,txt
      Prisca Muleka 5/1/2024
"""
def main():
    import random   # access python built in randint(low,high) method.
    numRolls = int(input("Enter number of random numbers desired: "))
    outFile = open("numbers.txt",'w')   # open output file
    for i in range(numRolls):
        randomNum + random.randint (1,500)
        outFile.write(str(randomNum) +'\n')
    outFile.close() # write buffer contents and close file
main() # execute main() module 
