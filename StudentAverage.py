# Read to grades of a student exam and tell its average and if his grade is equal or higher than 6 he has passed the exam

examOne = float(input("1º Exam: "))
examTwo = float(input("2º Exam: "))
print()

# Calculation

averageGrade = (examOne + examTwo) / 2


if averageGrade >= 6:
    print("Well done!, You've passed the exam")
else:
    print("Sorry, you've failed the exam")

# Output

print("Average:", averageGrade)


