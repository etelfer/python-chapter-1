# Initialize an empty dictionary of student grades
student_grades = {}

# Function to add a student and grade
def add_student(name,grade):
    student_grades[name] = grade
    print(f"Student '{name}' added with grade of {grade}.")
    pass

# Function to remove a student
def remove_student(name):
    if name in student_grades:
        del student_grades[name]
        print(f"Student '{name}' removed.")
    elif name not in student_grades:
        print(f"Student '{name}' not found.")
        pass

# Function to display all students and their grades
def display_students():
    print("Student Grades:")
    for name, grade in student_grades.items():
        print(f"{name}: {grade}")
        pass

# Function to update a student's grade
def update_grade(name, grade):
    if name in student_grades:
        student_grades[name] = grade
        print(f"Student '{name}' grade updated to grade {grade}.")
    elif name not in student_grades:
        print(f"Student '{name}' not found.")
        pass

# Add some students

add_student("Erin", 99)
add_student("Justin", 85)
add_student("Marcus", 87)


# Display students and their grades

display_students()

# Update a student's grade

update_grade("Erin", 98.5)

# Remove a student

remove_student("Erin")

# Display students and their grades again

display_students()