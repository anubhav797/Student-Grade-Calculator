def calculate_grade(marks):
    average = sum(marks) / len(marks)

    if average >= 90:
        return "A"
    elif average >= 75:
        return "B"
    elif average >= 60:
        return "C"
    elif average >= 40:
        return "D"
    else:
        return "Needs Improvement"


marks = [85, 90, 78, 92]

print("Average:", sum(marks) / len(marks))
print("Grade:", calculate_grade(marks))