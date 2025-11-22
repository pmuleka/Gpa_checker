""" Day 14 program 2 - read numbers.txt file create in program 1
      Accumulate total number sum of all random numbers.
      at end of file (EOF) display total number, sum as well as average
      Prisca Muleka 5/1/2024
"""
def main():
    counter = 0    # initialize counter and sum of numbers
    total = 0
    inFile = open("numbers.txt",'r')  # open existing file (created program 1)
    curNumberStr = inFile.readline()  # priming read.
    while (curNumberStr != ''):       # read all numbers check for EOF 
        curNumber = int(curNumberStr) # convert string to integer numeric
        counter += 1                  # increment counter
        total += curNumber            # Accumulate sum total
        curNumberStr = inFile.readline()    # read next number
    average = total/counter                 # compute average
    print("Total of ", counter, " numbers is ", total)
    print("Average of numbers is ", average)
    inFile.close()                    # close input file
main()                                # execute main() method
