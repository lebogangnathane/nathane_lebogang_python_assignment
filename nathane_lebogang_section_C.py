# This is the main dictionary that will store ALL student data(names,grades)
students_dict = {}

# These are the subjects we used for every student
subjects = ["Math", "English", "Science"]

# ADD STORED STUDENTS DATA
students_dict["John"] = {
    "Math": 85,
    "English": 78,
    "Science": 92
}

students_dict["Sarah"] = {
    "Math": 95,
    "English": 88,
    "Science": 85
}
students_dict["David"] = {
    "Math": 78,
    "English": 80,
    "Science": 92
}

print("WELCOME TO SIMPLE GRADING SYSTEM")
print(f"System initialized with {len(students_dict)} students")

# MAIN PROGRAM LOOP(keeps running until user chooses to exit)
while True:
    # This shows the menu options to the user
    print("\nWhat would you like to do?")
    print("1. Add a new student")
    print("2. Update a student's grades")
    print("3. Remove a student")
    print("4. View all students")
    print("5. Search for a student")
    print("6. View grades for one subject")
    print("7. Exit program")

    # Get the user's choice
    user_choice = input("\nEnter your choice (1-7): ")

#1 ADDING A NEW STUDENT
    if user_choice == '1':
        print("\n--- Add a new student ---")

        # Ask for the student's name
        student_name = input("Enter the student's name: ")

        # Check if this student already exists in our dictionary
        if student_name in students_dict:
            print(f"{student_name} is already in the system.")
        else:
            # Create a new dictionary to store this student's grades
            student_grades = {}

            # Ask for grades in each subject
            for subject in subjects:
                # Loop to keep asking until we get a valid grade (0-100)
                while True:
                    try:
                        # Ask for the grade
                        grade = float(input(f"Enter {student_name}'s grade for {subject}: "))

                        # Check if grade is between 0 and 100
                        if 0 <= grade <= 100:
                            # Add the grade to this student's subject
                            student_grades[subject] = grade
                            break  # Exit the while loop since we got a valid grade
                        else:
                            print("Please enter a grade between 0 and 100.")
                    except ValueError:
                        # This happens if user enters text instead of a number
                        print("Please enter a valid number (like 85 or 92.5).")

            # Add the student to our main dictionary
            students_dict[student_name] = student_grades
            print(f"Great! {student_name} has been added to the system.")

#2 UPDATING STUDENTS GRADE
    elif user_choice == '2':
        print("\n--- UPDATING STUDENT GRADES ---")

        # Ask which student to update
        student_name = input("Enter the student's name: ")

        # Check if student exists
        if student_name not in students_dict:
            print(f"{student_name} is not in the system.")
        else:
            print(f"Updating grades for {student_name}:")

            # Get the student's current grade dictionary
            current_grades = students_dict[student_name]

            # Ask for new grades for each subject
            for subject in subjects:
                while True:
                    try:
                        # Show the current grade (if it exists)
                        current_grade = current_grades.get(subject, "No grade")
                        print(f"Current {subject} grade: {current_grade}")

                        # Ask for new grade
                        new_grade = float(input(f"Enter new grade for {subject}: "))

                        if 0 <= new_grade <= 100:
                            # Update the grade
                            current_grades[subject] = new_grade
                            break
                        else:
                            print("Please enter a grade between 0 and 100.")
                    except ValueError:
                        print("Please enter a valid number.")

            print(f"Grades for {student_name} have been updated!")

   #3 REMOVING A STUDENT
    elif user_choice == '3':
        print("\n--- REMOVING A STUDENT ---")

        # Ask which student to remove
        student_name = input("Enter the student's name to remove: ")

        # Check if student exists
        if student_name in students_dict:
            # Remove the student from the dictionary
            del students_dict[student_name]
            print(f"{student_name} has been removed from the system.")
        else:
            print(f"Sorry, {student_name} is not in the system.")

    #4 VIEWING ALL STUDENTS
    elif user_choice == '4':
        print("\n--- VIEWING ALL STUDENTS ---")

        # Check if there are any students in the system
        if len(students_dict) == 0:
            print("There are no students in the system yet.")
        else:
            # Loop through each student in the dictionary
            for student_name, grades_dict in students_dict.items():
                print(f"\nStudent: {student_name}")

                # Calculate total and average for this student
                total_grade = 0
                count = 0

                # Print each subject and grade
                for subject, grade in grades_dict.items():
                    print(f"  {subject}: {grade}")
                    total_grade += grade
                    count += 1

                # Calculate and display average
                if count > 0:
                    average = total_grade / count
                    print(f"  AVERAGE: {average:.2f}")

   #5 SEARCHING FOR A STUDENT
    elif user_choice == '5':
        print("\n--- SEARCHING FOR A STUDENT ---")

        # Ask which student to search for
        student_name = input("Enter the student's name to search: ")

        # Check if student exists
        if student_name in students_dict:
            print(f"\nFOUND: {student_name}")

            # Get the student's grades
            grades_dict = students_dict[student_name]

            total_grade = 0
            count = 0

            # Display all grades
            for subject, grade in grades_dict.items():
                print(f"  {subject}: {grade}")
                total_grade += grade
                count += 1

            # Calculate and display average
            if count > 0:
                average = total_grade / count
                print(f"  OVERALL AVERAGE: {average:.2f}")
        else:
            print(f"Sorry, {student_name} is not in the system.")

   #6 VIEW GRADES FOR 1 SUBJECT
    elif user_choice == '6':
        print("\n--- VIEWING GRADES FOR ONE SUBJECT ---")

        # Show available subjects
        print("Available subjects:", ", ".join(subjects))

        # Ask which subject to view
        subject_name = input("Enter the subject name: ")

        # Check if it's a valid subject
        if subject_name not in subjects:
            print("That's not a valid subject.")
        else:
            print(f"\n--- {subject_name.upper()} GRADES ---")

            # List to store all grades for this subject (for calculating statistics)
            all_grades = []

            # Loop through all students
            for student_name, grades_dict in students_dict.items():
                # Check if this student has a grade for the subject
                if subject_name in grades_dict:
                    grade = grades_dict[subject_name]
                    print(f"{student_name}: {grade}")
                    all_grades.append(grade)

            # Calculate and display statistics if we have grades
            if len(all_grades) > 0:
                average = sum(all_grades) / len(all_grades)
                highest = max(all_grades)
                lowest = min(all_grades)

                print(f"\nSUBJECT STATISTICS:")
                print(f"  Class Average: {average:.2f}")
                print(f"  Highest Grade: {highest}")
                print(f"  Lowest Grade: {lowest}")
            else:
                print("No grades available for this subject.")

   #7 EXIT THE PROGRAM
    elif user_choice == '7':
        print("\nGoodbye!")
        break  # This stops the while loop and ends the program

  #if invalid choice is entered
    else:
        print("Invalid choice! Please enter a number from 1 to 7.")