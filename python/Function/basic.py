def student_result(name, marks, bonus=0):
    total = sum(marks) + bonus
    percentage = total / len(marks)

    if percentage >= 90:
        grade = "A+"
    elif percentage >= 75:
        grade = "A"
    elif percentage >= 60:
        grade = "B"
    elif percentage >= 40:
        grade = "C"
    else:
        grade = "Fail"

    return name, total, percentage, grade


# Function ko call karna
result = student_result(
    "Gouarv",
    [80, 75, 90, 85, 70],
    5
)

name, total, percentage, grade = result

print("Name:", name)
print("Total:", total)
print("Percentage:", percentage)
print("Grade:", grade)

