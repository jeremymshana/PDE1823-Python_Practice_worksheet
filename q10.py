# Function to show grade
def get_grade(mark):
    if mark >= 80:
        return "A"
    elif mark >= 70:
        return "B"
    elif mark >= 60:
        return "C"
    elif mark >= 50:
        return "D"
    else:
        return "F"


names = []
marks = []

# Asking number of students
num_students = int(input("How many students are in the class? "))

# Input names and marks
for i in range(num_students):
    name = input(f"\nEnter student {i + 1} name: ")
    mark = int(input(f"Enter mark for {name}: "))

    names.append(name)
    marks.append(mark)

# showing results
print("Student Results:")

total = 0

for i in range(num_students):
    grade = get_grade(marks[i])
    print("{names[i]} - Mark: {marks[i]} - Grade: {grade}")
    total += marks[i]

# Calculate class average
average = total / num_students

print("Class average:", round(average, 2))