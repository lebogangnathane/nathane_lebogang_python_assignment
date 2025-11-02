# Getting the number of students from user
num_students = int(input("Enter the number of students in the class: "))

# Variable to store total grades
total_grade = 0

# String to store all student results
all_students_results = ""

# Loop to get each student's data
for i in range(num_students):
    print(f"\nStudent {i + 1}")

    # Get student name
    name = input("Enter student name: ")

    # Getting and validating grades
    while True:
        grade = float(input(f"Enter {name}'s English grade (0-100): "))
        if 0 <= grade <= 100:
            total_grade += grade  # Add grade to total

            # Add student result to the string
            all_students_results += f"Student: {name} , Grade: {grade}\n"
            break
        else:
            print("Grade must be between 0 and 100. Please try again.")

# Display all student results
print("\n")
print("ALL STUDENT RESULTS:")
print(all_students_results)

# Calculating average grade
average_grade = total_grade / num_students

# Display results
print("CLASS SUMMARY:")
print(f"Total Class Grade: {total_grade}")
print(f"Average Class Grade: {average_grade:.1f}")