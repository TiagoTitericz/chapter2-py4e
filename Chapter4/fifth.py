'''Exercise 7: Rewrite the grade program from the previous chapter using
a function called computegrade that takes a score as its parameter and
returns a grade as a string.'''

def grade_score(score):
    try:
        grade = float(score)
        if grade >= 1.0 or grade < 0:
            return "Bad score"
        elif grade >= 0.9:
            return "A"
        elif grade >= 0.8:
            return "B"
        elif grade >= 0.7:
            return "C"
        elif grade >= 0.6:
            return "D"
        else:
            return "F"
    except:
        return 'Bad score'

score = input("Enter a score: ")

print(grade_score(score))