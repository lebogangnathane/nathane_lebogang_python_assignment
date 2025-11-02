# Defining   the subjects, USING LIST
subjects = ["Math", "English", "Science", "Setswana", "Agriculture"]

# Get the number of students from user
num_students = int(input("Enter the number of students in the class: "))

# LIST to store student data as TUPLES (name, grades_list)
students = []

#Multiple Subjects - Loop to get each student's data
for i in range(num_students):
    print(f"\nStudent {i+1}")
    
    # Get student name
    name = input("Enter student name: ")
    
    # LIST to store grades for this student
    grades = []
    
    # Get grades for each subject
    for subject in subjects:
        while True:
            grade = float(input(f"Enter {name}'s {subject} grade (0-100): "))
            if 0 <= grade <= 100:
                grades.append(grade)  # Adding to LIST
                break
            else:
                print("Grade must be between 0 and 100. Please try again.")
    
    # Store as TUPLE (name, grades list) in students LIST
    students.append((name, grades))

#Enhanced Output - Calculate subject statistics
print("\nSUBJECT STATISTICS")

# Find highest and lowest for each subject
for j, subject in enumerate(subjects):
    subject_grades = []  # LIST for current subject's grades
    for name, grades in students:
        subject_grades.append(grades[j])  # Get grade for this subject
    
    highest = max(subject_grades)
    lowest = min(subject_grades)
    print(f"{subject}: Highest = {highest}, Lowest = {lowest}")

 #Data Display - Student Summary
print("\nSTUDENT DETAILS")
for name, grades in students:
    average = sum(grades) / len(grades)
    print(f"\n{name}:")
    for i, subject in enumerate(subjects):
        print(f"  {subject}: {grades[i]}")
    print(f"  Overall Average: {average:.2f}")

# Calculate class overview
print("\nCLASS OVERVIEW")

# Calculate overall class average
all_grades = []  # LIST to collect all grades from all students
for name, grades in students:
    all_grades.extend(grades)  # Add all grades to the list

total_grade = sum(all_grades)
average_grade = total_grade / len(all_grades)

print(f"Total Grade: {total_grade}")
print(f"Average Grade: {average_grade:.1f}")