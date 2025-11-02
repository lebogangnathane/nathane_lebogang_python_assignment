students_dict = {}
subjects = ["Math", "English", "Science"]

# Initialize with some sample student data
students_dict.update({
    "John": {"Math": 85, "English": 78, "Science": 92},
    "Sarah": {"Math": 95, "English": 88, "Science": 85},
    "David": {"Math": 78, "English": 80, "Science": 92}
})

def get_grade(prompt):                   # function 1
    """
    Get a valid grade from user input with comprehensive validation.

    This function continuously prompts the user until a valid grade is entered.
    Valid grades must be numeric and between 0-100 inclusive.

    Args:
        prompt (str): The message to display when asking for input

    Returns:
        int: A valid grade between 0-100
    """
    while True:
        try:
            grade = float(input(prompt))
            if 0 <= grade <= 100:
                return int(grade)  # Convert to int for cleaner storage
            print("Grade must be 0-100")
        except ValueError:
            # Handle non-numeric input like letters or symbols
            print("Please enter a valid number")


def calculate_average(grades):                        # function 2
    """
    Calculate the average of grades with safety checks.

    This function handles empty grade dictionaries and prevents division by zero.
    It's designed to be robust and return 0 for invalid inputs.

    Args:
        grades (dict): A dictionary of subject:grade pairs

    Returns:
        float: The average grade, or 0 if no grades are available
    """
    return sum(grades.values()) / len(grades) if grades else 0


def get_student_name(prompt):                       # function 3
    """
    Get and validate a student name from user input.

    Ensures the name is not empty and returns the stripped version.
    Also handles the case where user enters only whitespace.

    Args:
        prompt (str): The message to display when asking for the name

    Returns:
        str: A non-empty student name, or empty string if invalid
    """
    name = input(prompt).strip()
    if not name:
        print("Student name cannot be empty")
        return ""
    return name


def add_student():                  # function 4
    """
    Add a new student to the grading system.

    This function:
    1. Gets and validates the student name
    2. Checks if the student already exists
    3. Collects grades for all subjects
    4. Adds the student to the main dictionary

    The function prevents duplicate entries and ensures all subjects have grades.
    """
    name = get_student_name("Enter student name: ")
    # Early return if name is invalid or student already exists
    if not name:
        return
    if name in students_dict:
        print(f"{name} already exists")
        return

    # Use dictionary comprehension to collect grades for all subjects
    students_dict[name] = {subject: get_grade(f"Enter {name}'s {subject} grade: ")
                           for subject in subjects}
    print(f"Added {name}")


def update_grades():                 # function 5
    """
    Update grades for an existing student.

    This function:
    1. Finds the student to update
    2. Shows current grades for reference
    3. Collects new grades for all subjects
    4. Updates the student record

    If the student doesn't exist, it informs the user and exits.
    """
    name = get_student_name("Enter student name: ")
    if not name or name not in students_dict:
        print(f"{name not in students_dict and f'{name} not found' or ''}")
        return

    # Loop through each subject, show current grade and get new one
    for subject in subjects:
        current = students_dict[name].get(subject, "No grade")
        print(f"Current {subject}: {current}")
        students_dict[name][subject] = get_grade(f"New {subject} grade: ")

    print(f"Updated {name}'s grades")


def remove_student():                        # function 6
    """
    Remove a student from the system entirely.

    This function:
    1. Gets the student name to remove
    2. Verifies the student exists
    3. Deletes the student record
    4. Confirms the deletion

    Uses safe deletion with existence check to prevent KeyError.
    """
    name = get_student_name("Enter student name to remove: ")
    if not name:
        return

    if name in students_dict:
        del students_dict[name]
        print(f"Removed {name}")
    else:
        print(f"{name} not found")


def display_student_grades(name, grades):                    # function 7
    """
    Display a formatted view of a single student's grades and average.

    This helper function creates a consistent display format used by
    both view_students() and search_student() functions.

    Args:
        name (str): The student's name
        grades (dict): The student's subject:grade pairs
    """
    print(f"\n{name}:")
    # Display each subject and grade with indentation
    for subject, grade in grades.items():
        print(f"  {subject}: {grade}")
    # Calculate and display the average with one decimal place
    avg = calculate_average(grades)
    print(f"  Average: {avg:.1f}")


def view_students():                     # function 8
    """
    Display all students in the system with their grades and averages.

    Shows a comprehensive overview of all student records.
    If no students exist, informs the user instead of showing empty data.
    """
    if not students_dict:
        print("No students in system")
        return

    # Use the helper function to display each student consistently
    for name, grades in students_dict.items():
        display_student_grades(name, grades)


def search_student():
    """
    Find a student and optionally update their grades.
    """
    name = get_student_name("Enter student name: ")
    if not name:
        return

    if name in students_dict:
        display_student_grades(name, students_dict[name])

        # ADD THIS PART FOR UPDATING:
        update = input("Update grades? (y/n): ").strip().lower()
        if update == 'y':
            for subject in subjects:
                current = students_dict[name].get(subject, "No grade")
                print(f"Current {subject}: {current}")
                students_dict[name][subject] = get_grade(f"New {subject} grade: ")
            print(f"Updated {name}'s grades")
    else:
        print(f"{name} not found")

def view_subject():                         # function 10
    """
    Display comprehensive statistics for a specific subject across all students.

    This function:
    1. Shows available subjects
    2. Gets the subject to analyze
    3. Displays all student grades for that subject
    4. Calculates class statistics (average, highest, lowest)

    Provides both individual grades and aggregate class performance.
    """
    print("Subjects:", ", ".join(subjects))
    subject = input("Enter subject: ").strip()

    if subject not in subjects:
        print("Invalid subject")
        return

    # Collect all grades for the specified subject using list comprehension
    grades = [student_grades[subject] for name, student_grades in students_dict.items()
              if subject in student_grades]

    # Display individual student grades for the subject
    print(f"\n{subject} Grades:")
    for name, student_grades in students_dict.items():
        if subject in student_grades:
            print(f"  {name}: {student_grades[subject]}")

    # Calculate and display class statistics if grades exist
    if grades:
        average = sum(grades) / len(grades)
        print(f"\nClass Average: {average:.1f}")
        print(f"Highest: {max(grades)}")
        print(f"Lowest: {min(grades)}")
    else:
        print("No grades available for this subject")


def show_menu():                     # function 11
    """
    Display the main menu and get user choice.

    Creates a numbered menu of all available operations.
    Uses enumeration for clean, maintainable menu display.

    Returns:
        str: The user's menu choice as a string
    """
    print("\nWhat would you like to do?")
    menu_options = [
        "Add student",
        "Update grades",
        "Remove student",
        "View all students",
        "Search student",
        "View subject grades",
        "Exit"
    ]

    # Display each menu option with its number
    for i, option in enumerate(menu_options, 1):
        print(f"{i}. {option}")

    return input("Choose 1-7: ").strip()


# MAIN PROGRAM LOOP
print("SIMPLE GRADING SYSTEM")
print(f"{len(students_dict)} students currently in the system.")

while True:
    choice = show_menu()

    # Dictionary mapping menu choices to function calls
    # This makes the menu handling clean and extensible
    actions = {
        '1': add_student,
        '2': update_grades,
        '3': remove_student,
        '4': view_students,
        '5': search_student,
        '6': view_subject
    }

    # Execute the corresponding function for valid choices
    if choice in actions:
        actions[choice]()
    elif choice == '7':
        print("Goodbye!")
        break
    else:
        print("Invalid choice")