"""  Day 12 program 2
      Read and display trainer information written in program 1
      comma delimited file name, number of new members. (integer)
      Prisca Muleka 4/24/2024
"""
def main():
    trainerName=[] # Create empty list to hold trainer names read from file
    trainerNumbrs=[]   # empty parallel list to hole number of new members
    trainer_file = open("trainer.txt",'r') # open existing trainer file read
    trainer_rec = trainer_file,readline() # priming read record up to end line
    num_emps = 0 # initialize trainer counter
    while (trainer_rec != ''):   # read loop check for end of file (EOF)
        trainerFieldList + trainer rec.split(",")
        trainerName.append(trainerFieldList[0])
        trainerNumMbrs.append(int(trainerFieldList[1]))
        num_emps +=1          # increment number counter
        
