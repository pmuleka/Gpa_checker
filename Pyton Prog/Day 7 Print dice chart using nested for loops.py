""" Day 7 print diece chart using for loops.py
      Do a couple of nested for loops to print out results of rolling 2 dice,
      Makes use of Python print to allow professional looking lined
      up report.
      Prisca Muleka 4/10/2024
"""
def main():
    print("    |    1   2   3   4   5  6  die 1") #print top heading
    print("----------------------------")
    for i in range(1,7,1):  # outer loop
        print("%3s" % str(i),"|",end=' ') # print left column label
        for j in range(1,7,1):    # inner loop print detail of line
            print("%3s" % str(i + j),end=' ')
        print(end='\n')      #back to outer loop print end of row
    print("die 2\n\n")       #print bottom column heading
    print (" **End Program**")
main()  # execute main() method
