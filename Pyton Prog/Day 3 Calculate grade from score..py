"""
    Day 3 calculate grade using nexted if/else and if/elif/else.  Two ways to acocomplish the same task. from an input score calculate on a common 10 point scale.
    Prisca Muleka 3/25/2024
"""
score = int(input("Enter interger score from 1 to 100 for grade: ")) # input score # first part run if?else statements only - be ware of indentation
if score >= 90:
    grade = "A'"
else:
    if score >= 80:
        grade = "B"
    else:
        if score >= 70:
            grade = "C"
        else:
            if score >= 60 :
                grade = "D"
            else:
                    grade = "F"
print ("Score ", score, " earns grade ", grade)                    
# second part if/elif/else statements accomplish same as above
if (score >= 90) :
    grade = 'a'
elif (score >= 80) :
    grade = 'b'
elif (score >= 70) :
    grade = 'c'
elif (score >= 60) :
    grade = 'd'
else:
    grade = 'f'
print ('Score ', score , 'earns grade ', grade)
