class Student:
    """
    A class to represent a student with their name and grades.

    Attributes:
        name (str): The student's name
        grades (dict): Dictionary storing subject:grade pairs
    """

    def __init__(self, name):
        """
        Initialize a new Student with their name and empty grades.

        Args:
            name (str): The student's name
        """
        self.name = name
        self.grades = {}  # Start with no grades

    def add_grade(self, subject, grade):
        """
        Add a grade for a specific subject.

        Args:
            subject (str): The subject name (e.g., "Math")
            grade (int): The grade value (0-100)
        """
        self.grades[subject] = grade

    def calculate_average(self):
        """
        Calculate the student's average grade across all subjects.

        Returns:
            float: The average grade, or 0 if no grades exist
        """
        if not self.grades:  # Check if grades dictionary is empty
            return 0
        return sum(self.grades.values()) / len(self.grades)

    def print_details(self):
        """
        Print the student's name, all grades, and average.
        """
        print(f"\n{self.name}:")
        for subject, grade in self.grades.items():
            print(f"  {subject}: {grade}")

        avg = self.calculate_average()
        print(f"  Average: {avg:.1f}")


class Gradebook:
    """
    A class to manage a collection of Student objects.

    Attributes:
        students (dict): Dictionary storing name:Student object pairs
        subjects (list): List of available subjects
    """

    def __init__(self, subjects):
        """
        Initialize an empty Gradebook with the specified subjects.

        Args:
            subjects (list): List of subject names
        """
        self.students = {}
        self.subjects = subjects

    def add_student(self, name):
        """
        Add a new student to the gradebook.

        Args:
            name (str): The student's name

        Returns:
            bool: True if student was added, False if already exists
        """
        if name in self.students:
            print(f"{name} already exists in the gradebook.")
            return False

        # Create a new Student object and add to our dictionary
        self.students[name] = Student(name)
        print(f"Added {name} to the gradebook.")
        return True

    def remove_student(self, name):
        """
        Remove a student from the gradebook.

        Args:
            name (str): The student's name

        Returns:
            bool: True if student was removed, False if not found
        """
        if name in self.students:
            del self.students[name]
            print(f"Removed {name} from the gradebook.")
            return True
        else:
            print(f"{name} not found in the gradebook.")
            return False

    def search_student(self, name):
        """
        Find and return a student by name.

        Args:
            name (str): The student's name

        Returns:
            Student: The Student object if found, None otherwise
        """
        return self.students.get(name)

    def get_all_students(self):
        """
        Get a list of all student names in the gradebook.

        Returns:
            list: List of all student names
        """
        return list(self.students.keys())

    def view_all_students(self):
        """
        Display all students with their grades and averages.
        """
        if not self.students:
            print("No students in the gradebook.")
            return

        print("\n--- ALL STUDENTS ---")
        for student in self.students.values():
            student.print_details()

    def sort_by_average(self):
        """
        Sort students by their average grade (highest to lowest).

        Returns:
            list: List of Student objects sorted by average
        """
        # Create a list of (average, student) tuples and sort by average
        students_with_avg = [(student.calculate_average(), student)
                             for student in self.students.values()]

        # Sort by average (highest first) and return just the student objects
        students_with_avg.sort(reverse=True, key=lambda x: x[0])
        return [student for avg, student in students_with_avg]

    def get_class_average(self):
        """
        Calculate the average grade across all students and all subjects.

        Returns:
            float: The class average, or 0 if no grades exist
        """
        all_grades = []
        for student in self.students.values():
            all_grades.extend(student.grades.values())

        if not all_grades:
            return 0
        return sum(all_grades) / len(all_grades)


# Helper functions for input validation
def get_grade(prompt):
    """
    Get a valid grade from user input (0-100).

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
            print("Grade must be between 0 and 100.")
        except ValueError:
            print("Please enter a valid number.")


def get_student_name(prompt):
    """
    Get and validate a student name from user input.

    Args:
        prompt (str): The message to display when asking for the name

    Returns:
        str: A non-empty student name
    """
    while True:
        name = input(prompt).strip()
        if name:
            return name
        print("Student name cannot be empty.")


# Main program functions that use the Gradebook class
def add_student(gradebook):
    """
    Add a new student to the system and collect their grades.
    """
    name = get_student_name("Enter student name: ")

    if gradebook.add_student(name):
        # If student was added successfully, collect their grades
        student = gradebook.search_student(name)
        print(f"Enter grades for {name}:")
        for subject in gradebook.subjects:
            grade = get_grade(f"  {subject} grade: ")
            student.add_grade(subject, grade)
        print(f"Completed adding {name}'s grades.")


def update_grades(gradebook):
    """
    Update grades for an existing student.
    """
    name = get_student_name("Enter student name: ")
    student = gradebook.search_student(name)

    if student:
        print(f"Updating grades for {name}:")
        for subject in gradebook.subjects:
            current_grade = student.grades.get(subject, "No grade")
            print(f"  Current {subject}: {current_grade}")
            new_grade = get_grade(f"  New {subject} grade: ")
            student.add_grade(subject, new_grade)
        print(f"Updated {name}'s grades.")
    else:
        print(f"{name} not found.")


def remove_student(gradebook):
    """
    Remove a student from the system.
    """
    name = get_student_name("Enter student name to remove: ")
    gradebook.remove_student(name)


def search_student(gradebook):
    """
    Find a student and optionally update their grades.
    """
    name = get_student_name("Enter student name: ")
    student = gradebook.search_student(name)

    if student:
        student.print_details()

        # Ask if user wants to update grades
        update = input("Update grades? (y/n): ").strip().lower()
        if update == 'y':
            for subject in gradebook.subjects:
                current_grade = student.grades.get(subject, "No grade")
                print(f"Current {subject}: {current_grade}")
                new_grade = get_grade(f"New {subject} grade: ")
                student.add_grade(subject, new_grade)
            print(f"Updated {name}'s grades.")
    else:
        print(f"{name} not found.")


def view_subject_grades(gradebook):
    """
    Display statistics for a specific subject across all students.
    """
    print("Subjects:", ", ".join(gradebook.subjects))
    subject = input("Enter subject: ").strip()

    if subject not in gradebook.subjects:
        print("Invalid subject.")
        return

    # Collect grades for the specified subject
    grades = []
    print(f"\n{subject} Grades:")

    for student in gradebook.students.values():
        if subject in student.grades:
            grade = student.grades[subject]
            print(f"  {student.name}: {grade}")
            grades.append(grade)

    # Calculate and display statistics
    if grades:
        average = sum(grades) / len(grades)
        print(f"\nClass Statistics for {subject}:")
        print(f"  Average: {average:.1f}")
        print(f"  Highest: {max(grades)}")
        print(f"  Lowest: {min(grades)}")
    else:
        print("No grades available for this subject.")


def view_sorted_students(gradebook):
    """
    Display students sorted by their average grade.
    """
    sorted_students = gradebook.sort_by_average()

    if not sorted_students:
        print("No students in the gradebook.")
        return

    print("\n--- STUDENTS SORTED BY AVERAGE (HIGHEST FIRST) ---")
    for student in sorted_students:
        avg = student.calculate_average()
        print(f"{student.name}: {avg:.1f}")


def show_menu():
    """
    Display the main menu and get user choice.

    Returns:
        str: The user's menu choice
    """
    print("\nWhat would you like to do?")
    menu_options = [
        "Add student",
        "Update grades",
        "Remove student",
        "View all students",
        "Search student",
        "View subject grades",
        "View students sorted by average",
        "Run Tests",  # New option for testing
        "Exit"
    ]

    for i, option in enumerate(menu_options, 1):
        print(f"{i}. {option}")

    return input("Choose 1-9: ").strip()


# COMPREHENSIVE TESTING FUNCTIONS
def run_unit_tests():
    """
    Run unit tests for individual classes and methods.
    """
    print("\n" + "=" * 50)
    print("RUNNING UNIT TESTS")
    print("=" * 50)

    # Test 1: Student class initialization
    print("\n1. Testing Student class initialization...")
    student1 = Student("Alice")
    assert student1.name == "Alice", "Student name not set correctly"
    assert student1.grades == {}, "Grades should be empty initially"
    print("✓ Student initialization test passed")

    # Test 2: Adding grades
    print("\n2. Testing grade addition...")
    student1.add_grade("Math", 85)
    student1.add_grade("English", 92)
    assert student1.grades["Math"] == 85, "Math grade not stored correctly"
    assert student1.grades["English"] == 92, "English grade not stored correctly"
    print("✓ Grade addition test passed")

    # Test 3: Average calculation
    print("\n3. Testing average calculation...")
    avg = student1.calculate_average()
    expected_avg = (85 + 92) / 2
    assert avg == expected_avg, f"Average calculation incorrect: {avg} vs {expected_avg}"
    print("✓ Average calculation test passed")

    # Test 4: Empty student average
    print("\n4. Testing empty student average...")
    empty_student = Student("Empty")
    assert empty_student.calculate_average() == 0, "Empty student should have average 0"
    print("✓ Empty student average test passed")

    # Test 5: Gradebook initialization
    print("\n5. Testing Gradebook initialization...")
    subjects = ["Math", "Science"]
    gradebook = Gradebook(subjects)
    assert gradebook.subjects == subjects, "Subjects not set correctly"
    assert gradebook.students == {}, "Students should be empty initially"
    print("✓ Gradebook initialization test passed")

    # Test 6: Adding students to gradebook
    print("\n6. Testing student addition to gradebook...")
    result1 = gradebook.add_student("Bob")
    result2 = gradebook.add_student("Bob")  # Duplicate
    assert result1 == True, "First addition should succeed"
    assert result2 == False, "Duplicate addition should fail"
    assert "Bob" in gradebook.students, "Student not found in gradebook"
    print("✓ Student addition test passed")

    # Test 7: Removing students
    print("\n7. Testing student removal...")
    result1 = gradebook.remove_student("Bob")
    result2 = gradebook.remove_student("Nonexistent")
    assert result1 == True, "Existing student removal should succeed"
    assert result2 == False, "Non-existent student removal should fail"
    assert "Bob" not in gradebook.students, "Student not removed properly"
    print("✓ Student removal test passed")

    # Test 8: Searching students
    print("\n8. Testing student search...")
    gradebook.add_student("Charlie")
    found_student = gradebook.search_student("Charlie")
    not_found = gradebook.search_student("Nobody")
    assert found_student is not None, "Existing student should be found"
    assert found_student.name == "Charlie", "Found student name incorrect"
    assert not_found is None, "Non-existent student should return None"
    print("✓ Student search test passed")

    # Test 9: Sorting by average
    print("\n9. Testing sorting by average...")
    # Create test students with different averages
    gradebook.add_student("HighAchiever")
    gradebook.add_student("LowAchiever")

    high_student = gradebook.search_student("HighAchiever")
    low_student = gradebook.search_student("LowAchiever")

    high_student.add_grade("Math", 95)
    high_student.add_grade("Science", 90)  # Average: 92.5
    low_student.add_grade("Math", 70)
    low_student.add_grade("Science", 65)  # Average: 67.5

    sorted_students = gradebook.sort_by_average()
    assert sorted_students[0].name == "HighAchiever", "Highest average should be first"
    assert sorted_students[1].name == "LowAchiever", "Lowest average should be last"
    print("✓ Sorting test passed")

    # Test 10: Class average calculation
    print("\n10. Testing class average calculation...")
    class_avg = gradebook.get_class_average()
    expected_class_avg = (95 + 90 + 70 + 65) / 4
    assert abs(class_avg - expected_class_avg) < 0.01, f"Class average incorrect: {class_avg} vs {expected_class_avg}"
    print("✓ Class average test passed")

    print("\n")
    print("ALL UNIT TESTS PASSED! ✓")

def run_integration_tests():
    """
    Run integration tests to verify the system works as a whole.
    """
    print("\n")
    print("RUNNING INTEGRATION TESTS")

    # Create a fresh gradebook for integration testing
    test_subjects = ["Math", "English", "Science"]
    test_gradebook = Gradebook(test_subjects)

    # Test 1: Complete student lifecycle
    print("\n1. Testing complete student lifecycle...")

    # Add students
    test_gradebook.add_student("IntegrationTest1")
    test_gradebook.add_student("IntegrationTest2")

    # Add grades
    student1 = test_gradebook.search_student("IntegrationTest1")
    student2 = test_gradebook.search_student("IntegrationTest2")

    student1.add_grade("Math", 80)
    student1.add_grade("English", 85)
    student1.add_grade("Science", 90)

    student2.add_grade("Math", 70)
    student2.add_grade("English", 75)
    student2.add_grade("Science", 80)

    # Verify data integrity
    assert len(test_gradebook.get_all_students()) == 2, "Should have 2 students"
    assert student1.calculate_average() == 85.0, "Student1 average incorrect"
    assert student2.calculate_average() == 75.0, "Student2 average incorrect"
    print("✓ Student lifecycle test passed")

    # Test 2: View all students functionality
    print("\n2. Testing view all students...")
    # This should run without errors
    test_gradebook.view_all_students()
    print("✓ View all students test passed")

    # Test 3: Sorting functionality
    print("\n3. Testing sorting integration...")
    sorted_list = test_gradebook.sort_by_average()
    assert sorted_list[0].name == "IntegrationTest1", "Sorting order incorrect"
    assert sorted_list[1].name == "IntegrationTest2", "Sorting order incorrect"
    print("✓ Sorting integration test passed")

    # Test 4: Remove and verify
    print("\n4. Testing removal integration...")
    test_gradebook.remove_student("IntegrationTest1")
    assert test_gradebook.search_student("IntegrationTest1") is None, "Student not properly removed"
    assert len(test_gradebook.get_all_students()) == 1, "Student count incorrect after removal"
    print("✓ Removal integration test passed")

    print("\n")
    print("ALL INTEGRATION TESTS PASSED! ✓")

def run_comprehensive_testing():
    """
    Run all comprehensive tests including edge cases.
    """
    print("\n")
    print("COMPREHENSIVE TESTING SUITE")

    # Run unit tests
    run_unit_tests()

    # Run integration tests
    run_integration_tests()

    # Test edge cases
    print("\n")
    print("RUNNING EDGE CASE TESTS")

    # Edge case 1: Empty gradebook operations
    empty_gradebook = Gradebook(["Math"])
    empty_gradebook.view_all_students()  # Should handle gracefully
    empty_list = empty_gradebook.sort_by_average()
    assert empty_list == [], "Empty gradebook should return empty list"
    print("✓ Empty gradebook operations test passed")

    # Edge case 2: Student with no grades
    no_grades_student = Student("NoGrades")
    assert no_grades_student.calculate_average() == 0, "Student with no grades should have average 0"
    print("✓ No grades student test passed")

    # Edge case 3: Grade boundary values
    boundary_student = Student("Boundary")
    boundary_student.add_grade("Math", 0)  # Minimum
    boundary_student.add_grade("English", 100)  # Maximum
    assert boundary_student.calculate_average() == 50.0, "Boundary grade average incorrect"
    print("✓ Grade boundary test passed")

    print("\n")
    print("ALL COMPREHENSIVE TESTS COMPLETED SUCCESSFULLY! ✓")

# MAIN PROGRAM
def main():
    """
    Main function that runs the grading system.
    """
    print("SIMPLE GRADING SYSTEM (OOP VERSION WITH TESTING)")

    # Create a gradebook with predefined subjects
    subjects = ["Math", "English", "Science"]
    gradebook = Gradebook(subjects)

    # Add some sample students to start with
    sample_students = {
        "stux": {"Math": 85, "English": 78, "Science": 92},
        "dudu": {"Math": 95, "English": 88, "Science": 85},
        "lala": {"Math": 78, "English": 80, "Science": 92}
    }

    for name, grades_dict in sample_students.items():
        gradebook.add_student(name)
        student = gradebook.search_student(name)
        for subject, grade in grades_dict.items():
            student.add_grade(subject, grade)

    print(f"{len(gradebook.students)} sample students added to the system.")

    # Main program loop
    while True:
        choice = show_menu()

        # Dictionary mapping menu choices to functions
        actions = {
            '1': lambda: add_student(gradebook),
            '2': lambda: update_grades(gradebook),
            '3': lambda: remove_student(gradebook),
            '4': lambda: gradebook.view_all_students(),
            '5': lambda: search_student(gradebook),
            '6': lambda: view_subject_grades(gradebook),
            '7': lambda: view_sorted_students(gradebook),
            '8': lambda: run_comprehensive_testing()  # Testing option
        }

        if choice in actions:
            actions[choice]()
        elif choice == '9':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please enter 1-9.")


# Run the program
if __name__ == "__main__":
    main()