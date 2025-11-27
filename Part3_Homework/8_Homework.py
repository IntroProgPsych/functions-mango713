# 1.(Mandatory) Write a function called calculate_grade(score)
#    that RETURNS the correct letter grade:
#       90+ -> A
#       80-89 -> B
#       70-79 -> C
#       60-69 -> D
#       below 60 -> F
#
# 2. Write another function called display_report(score, grade)
#    that PRINTS something like:
#       Score: 85
#       Grade: B
#
# 3. In the main part of the program:
#       - ask the user for the score
#       - call calculate_grade(score)
#       - call display_report(score, grade)
#
# Keep input() outside the functions.

# Write your code here:

def calculate_grade(score):
    "Return a letter grade based on the numeric score."
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"


def display_report(score, grade):
    "Print the score and grade in a clean format."
    print(f"Score: {score}")
    print(f"Grade: {grade}")

score_input = int(input("Enter the score: "))

grade = calculate_grade(score_input)

display_report(score_input, grade)



