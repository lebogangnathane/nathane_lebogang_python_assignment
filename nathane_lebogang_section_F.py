# Define the subjects we'll use
subjects = ["Math", "English", "Science"]


class StudentNotFoundError(Exception):
    """Raised when a student is not found in the system"""
    pass


class InvalidGradeError(Exception):
    """Raised when a grade is not between 0-100"""
    pass


class InvalidSubjectError(Exception):
    """Raised when a subject is not valid"""
    pass


class EmptyNameError(Exception):
    """Raised when a student name is empty"""
    pass


class InvalidNameError(Exception):
    """Raised when a student name contains numbers"""
    pass


class Student:
    """
    This class represents one student in our system.
    It holds the student's name and grades, and can do calculations.
    """

    def __init__(self, name):
        """
        This is the constructor - it runs automatically when we create a new Student.
        It sets up the student with their name and empty grades.
        """
        # Validate name
        if not name or not name.strip():
            raise EmptyNameError("Student name cannot be empty")

        # Check if name contains numbers
        if any(char.isdigit() for char in name):
            raise InvalidNameError("Student name cannot contain numbers")

        self.name = name.strip()  # Store the student's name
        self.grades = {}  # Create empty dictionary for grades

    def add_grade(self, subject, grade):
        """
        Add or update a grade for a specific subject with validation.
        """
        try:
            # Validate subject
            if subject not in subjects:
                raise InvalidSubjectError(f"'{subject}' is not a valid subject")

            # Validate grade
            if not isinstance(grade, (int, float)):
                raise InvalidGradeError("Grade must be a number")
            if grade < 0 or grade > 100:
                raise InvalidGradeError("Grade must be between 0 and 100")

            self.grades[subject] = grade
            return True

        except (InvalidSubjectError, InvalidGradeError):
            raise  # Re-raise our custom exceptions
        except Exception as error:
            print(f"Unexpected error adding grade: {error}")
            return False

    def calculate_average(self):
        """
        Calculate the student's average grade across all subjects.
        """
        try:
            if not self.grades:
                return 0  # No grades yet

            total = sum(self.grades.values())
            count = len(self.grades)

            if count == 0:
                return 0

            return total / count

        except Exception as error:
            print(f"Error calculating average for {self.name}: {error}")
            return 0

    def print_details(self):
        """
        Print the student's name, all grades, and average.
        """
        try:
            print(f"\nStudent: {self.name}")
            print("Grades:")
            for subject in subjects:
                grade = self.grades.get(subject, "No grade yet")
                print(f"  {subject}: {grade}")

            # Only show average if student has at least one grade
            if self.grades:
                average = self.calculate_average()
                print(f"Average: {average:.1f}")
            else:
                print("Average: No grades yet")

        except Exception as error:
            print(f"Error printing student details: {error}")

    def get_grade(self, subject):
        """
        Get the grade for a specific subject.
        """
        try:
            return self.grades.get(subject, "No grade yet")
        except Exception as error:
            print(f"Error getting grade: {error}")
            return "Error"

    def has_grades(self):
        """
        Check if student has any grades.
        """
        return len(self.grades) > 0


class Gradebook:
    """
    This class manages a collection of Student objects.
    It can add, remove, search, and sort students.
    """

    def __init__(self):
        """
        Constructor - creates an empty gradebook.
        """
        self.students = {}  # Dictionary to store Student objects

    def add_student(self, name):
        """
        Add a new student to the gradebook with validation.
        """
        try:
            if not name or not name.strip():
                raise EmptyNameError("Student name cannot be empty")

            name = name.strip()

            # Check if name contains numbers
            if any(char.isdigit() for char in name):
                raise InvalidNameError("Student name cannot contain numbers")

            if name in self.students:
                raise ValueError(f"Student '{name}' already exists!")

            self.students[name] = Student(name)
            print(f"Added student: {name}")
            return True

        except (EmptyNameError, InvalidNameError, ValueError) as error:
            print(f"Error: {error}")
            return False
        except Exception as error:
            print(f"Unexpected error adding student: {error}")
            return False

    def remove_student(self, name):
        """
        Remove a student from the gradebook.
        """
        try:
            if not name or not name.strip():
                raise EmptyNameError("Student name cannot be empty")

            name = name.strip()

            if name not in self.students:
                raise StudentNotFoundError(f"Student '{name}' not found!")

            del self.students[name]
            print(f"Removed student: {name}")
            return True

        except (EmptyNameError, StudentNotFoundError) as error:
            print(f"Error: {error}")
            return False
        except Exception as error:
            print(f"Unexpected error removing student: {error}")
            return False

    def search_student(self, name):
        """
        Search for a student by name and return their object.
        """
        try:
            if not name or not name.strip():
                raise EmptyNameError("Student name cannot be empty")

            name = name.strip()

            if name not in self.students:
                raise StudentNotFoundError(f"Student '{name}' not found!")

            return self.students[name]

        except (EmptyNameError, StudentNotFoundError) as error:
            print(f"Error: {error}")
            return None
        except Exception as error:
            print(f"Unexpected error searching for student: {error}")
            return None

    def update_student_grade(self, name, subject, grade):
        """
        Update a grade for a specific student with full validation.
        """
        try:
            student = self.search_student(name)
            if not student:
                return False

            return student.add_grade(subject, grade)

        except (InvalidSubjectError, InvalidGradeError) as error:
            print(f"Error: {error}")
            return False
        except Exception as error:
            print(f"Unexpected error updating grade: {error}")
            return False

    def view_all_students(self):
        """
        Display all students with their details.
        """
        try:
            if not self.students:
                print("No students in the gradebook.")
                return

            print("\nALL STUDENTS")
            for student in self.students.values():
                student.print_details()

        except Exception as error:
            print(f"Error displaying students: {error}")

    def bubble_sort_students_by_average(self):
        """
        Sort students by average using bubble sort algorithm.
        Returns sorted list of (average, student) tuples.
        """
        try:
            # Get students with grades only
            students_with_grades = []
            for student in self.students.values():
                if student.has_grades():
                    average = student.calculate_average()
                    students_with_grades.append((average, student))

            if not students_with_grades:
                print("No students with grades to sort.")
                return []

            # Bubble sort implementation
            n = len(students_with_grades)
            for i in range(n):
                for j in range(0, n - i - 1):
                    # Compare averages and swap if needed
                    if students_with_grades[j][0] < students_with_grades[j + 1][0]:
                        # Swap the elements
                        students_with_grades[j], students_with_grades[j + 1] = students_with_grades[j + 1], \
                        students_with_grades[j]

            return students_with_grades

        except Exception as error:
            print(f"Error during sorting: {error}")
            return []

    def sort_by_average(self):
        """
        Sort students by their average grade (highest to lowest) using bubble sort.
        """
        try:
            sorted_students = self.bubble_sort_students_by_average()

            if sorted_students:
                print("\nSTUDENTS SORTED BY AVERAGE (Highest to Lowest)")
                print("Using Bubble Sort Algorithm")
                for average, student in sorted_students:
                    print(f"{student.name}: {average:.1f}")

            return sorted_students

        except Exception as error:
            print(f"Error sorting by average: {error}")
            return []

    def insertion_sort_students_by_subject(self, subject):
        """
        Sort students by subject grade using insertion sort algorithm.
        Returns sorted list of (grade, student) tuples.
        """
        try:
            if subject not in subjects:
                raise InvalidSubjectError(f"'{subject}' is not a valid subject")

            # Get students with grades for this subject
            students_with_grades = []
            for student in self.students.values():
                grade = student.grades.get(subject)
                if grade is not None:
                    students_with_grades.append((grade, student))

            if not students_with_grades:
                print(f"No students have grades for {subject} yet.")
                return []

            # Insertion sort implementation
            for i in range(1, len(students_with_grades)):
                key = students_with_grades[i]
                j = i - 1

                # Move elements that are smaller than key to one position ahead
                while j >= 0 and students_with_grades[j][0] < key[0]:
                    students_with_grades[j + 1] = students_with_grades[j]
                    j -= 1
                students_with_grades[j + 1] = key

            return students_with_grades

        except InvalidSubjectError as error:
            print(f"Error: {error}")
            return []
        except Exception as error:
            print(f"Error during sorting: {error}")
            return []

    def sort_by_subject(self, subject):
        """
        Sort students by grade in a specific subject (highest to lowest) using insertion sort.
        """
        try:
            sorted_students = self.insertion_sort_students_by_subject(subject)

            if sorted_students:
                print(f"\nSTUDENTS SORTED BY {subject.upper()} (Highest to Lowest)")
                print("Using Insertion Sort Algorithm")
                for grade, student in sorted_students:
                    print(f"{student.name}: {grade}")

            return sorted_students

        except Exception as error:
            print(f"Error sorting by subject: {error}")
            return []

    def sort_students_by_name(self):
        """
        NEW: Sort students by name alphabetically (A to Z) using bubble sort.
        """
        try:
            if not self.students:
                print("No students to sort.")
                return []

            # Convert dictionary to list for sorting
            student_list = list(self.students.values())

            # Bubble sort implementation for names
            n = len(student_list)
            for i in range(n):
                for j in range(0, n - i - 1):
                    # Compare names alphabetically
                    if student_list[j].name > student_list[j + 1].name:
                        # Swap the elements
                        student_list[j], student_list[j + 1] = student_list[j + 1], student_list[j]

            print("\nSTUDENTS SORTED BY NAME (A to Z)")
            print("Using Bubble Sort Algorithm")
            for student in student_list:
                print(f"{student.name}")

            return student_list

        except Exception as error:
            print(f"Error sorting by name: {error}")
            return []

    def view_subject_grades(self, subject):
        """
        View grades for a specific subject across all students.
        """
        try:
            if subject not in subjects:
                raise InvalidSubjectError(f"'{subject}' is not a valid subject")

            print(f"\n{subject.upper()} GRADES")
            all_grades = []

            for student in self.students.values():
                grade = student.grades.get(subject)
                if grade is not None:
                    print(f"{student.name}: {grade}")
                    all_grades.append(grade)
                else:
                    print(f"{student.name}: No grade yet")

            if all_grades:
                average = sum(all_grades) / len(all_grades)
                print(f"\nClass Statistics:")
                print(f"  Average: {average:.1f}")
                print(f"  Highest: {max(all_grades)}")
                print(f"  Lowest: {min(all_grades)}")
                print(f"  Total Students with Grades: {len(all_grades)}")
            else:
                print("No grades available for this subject yet.")

        except InvalidSubjectError as error:
            print(f"Error: {error}")
        except Exception as error:
            print(f"Error viewing subject grades: {error}")

    def search_students_by_name(self, search_term):
        """
        Search for students by name (partial match).
        """
        try:
            if not search_term or not search_term.strip():
                raise EmptyNameError("Search term cannot be empty")

            search_term = search_term.strip().lower()
            found_students = []

            for student in self.students.values():
                if search_term in student.name.lower():
                    found_students.append(student)

            return found_students

        except EmptyNameError as error:
            print(f"Error: {error}")
            return []
        except Exception as error:
            print(f"Error searching students: {error}")
            return []


def run_comprehensive_tests():
    """
    COMPREHENSIVE TESTING DOCUMENTATION:

    Tests Conducted:
    1. Student creation with valid and invalid names
    2. Grade validation (0-100 range, invalid subjects)
    3. Custom exception handling
    4. Sorting algorithms (bubble sort and insertion sort)
    5. Search functionality
    6. Edge cases (empty data, boundary values)

    Issues Found and Resolved:
    - Empty names now properly handled with EmptyNameError
    - Invalid grades rejected with clear error messages
    - Sorting algorithms handle empty data gracefully
    - All methods include try-except blocks for robustness
    """
    print("COMPREHENSIVE SYSTEM TESTING")

    gradebook = Gradebook()

    # Test 1: Student management with exception handling
    print("\n1. TESTING STUDENT MANAGEMENT WITH EXCEPTIONS")
    print("   Testing valid student creation")
    gradebook.add_student("John")
    gradebook.add_student("Sarah")

    print("   Testing invalid student creation")
    gradebook.add_student("")  # Should show EmptyNameError
    gradebook.add_student("John")  # Should show duplicate error
    gradebook.add_student("John123")  # Should show InvalidNameError

    # Test 2: Grade management with exception handling
    print("\n2. TESTING GRADE MANAGEMENT WITH EXCEPTIONS")
    print("   Testing valid grade updates")
    gradebook.update_student_grade("John", "Math", 85)
    gradebook.update_student_grade("John", "English", 78)
    gradebook.update_student_grade("Sarah", "Math", 95)

    print("   Testing invalid grade updates")
    gradebook.update_student_grade("John", "Math", 150)  # Should show InvalidGradeError
    gradebook.update_student_grade("John", "History", 90)  # Should show InvalidSubjectError
    gradebook.update_student_grade("Unknown", "Math", 90)  # Should show StudentNotFoundError

    # Test 3: Sorting algorithms
    print("\n3. TESTING SORTING ALGORITHMS")
    gradebook.add_student("David")
    gradebook.update_student_grade("David", "Math", 78)
    gradebook.update_student_grade("David", "English", 82)

    print("   Testing bubble sort by average")
    gradebook.sort_by_average()

    print("   Testing insertion sort by subject")
    gradebook.sort_by_subject("Math")

    print("   Testing name sorting")
    gradebook.sort_students_by_name()

    # Test 4: Search functionality
    print("\n4. TESTING SEARCH FUNCTIONALITY")
    print("   Testing name search")
    results = gradebook.search_students_by_name("a")  # Should find Sarah and David
    print(f"   Found {len(results)} students with 'a' in name")

    # Test 5: View all data
    print("\n5. TESTING DATA DISPLAY")
    gradebook.view_all_students()

    print("\nALL TESTS COMPLETED SUCCESSFULLY")
    return gradebook


def show_menu():
    """
    Display the main menu to the user.
    """
    print("\n")
    print("GRADEBOOK MANAGEMENT SYSTEM")
    print("1. Add student")
    print("2. Remove student")
    print("3. Update student grade")
    print("4. View all students")
    print("5. Search student by name")
    print("6. Sort students by average")
    print("7. Sort students by subject")
    print("8. Sort students by name")
    print("9. View subject grades")
    print("10. Run comprehensive tests")
    print("11. Exit")

    choice = input("Enter your choice (1-11): ")
    return choice


def get_valid_grade(prompt):
    """
    Get a valid grade from user (0-100) with exception handling.
    """
    while True:
        try:
            grade = float(input(prompt))
            if 0 <= grade <= 100:
                return int(grade)
            else:
                raise InvalidGradeError("Grade must be between 0 and 100")
        except ValueError:
            print("Please enter a valid number.")
        except InvalidGradeError as error:
            print(f"Error: {error}")


def main():
    """
    Main program that runs the enhanced gradebook system.
    """
    # Create a gradebook
    gradebook = Gradebook()

    # Add sample data for demonstration
    try:
        gradebook.add_student("John")
        gradebook.update_student_grade("John", "Math", 85)
        gradebook.update_student_grade("John", "English", 78)
        gradebook.update_student_grade("John", "Science", 92)

        gradebook.add_student("Sarah")
        gradebook.update_student_grade("Sarah", "Math", 95)
        gradebook.update_student_grade("Sarah", "English", 88)
        gradebook.update_student_grade("Sarah", "Science", 85)

        gradebook.add_student("David")
        gradebook.update_student_grade("David", "Math", 78)
        gradebook.update_student_grade("David", "English", 80)

        # One student with no grades to demonstrate the system
        gradebook.add_student("NewStudent")

    except Exception as error:
        print(f"Error setting up sample data: {error}")

    print("ENHANCED OOP GRADING SYSTEM")
    print("Now with comprehensive exception handling and sorting algorithms!")
    print(f"System loaded with {len(gradebook.students)} students")

    # Main program loop with enhanced error handling
    while True:
        try:
            choice = show_menu()

            if choice == '1':
                name = input("Enter student name: ")
                gradebook.add_student(name)

            elif choice == '2':
                name = input("Enter student name to remove: ")
                gradebook.remove_student(name)

            elif choice == '3':
                name = input("Enter student name: ")
                print("Available subjects:", ", ".join(subjects))
                subject = input("Enter subject: ")
                grade = get_valid_grade(f"Enter grade for {subject}: ")
                if gradebook.update_student_grade(name, subject, grade):
                    print("Grade updated successfully!")

            elif choice == '4':
                gradebook.view_all_students()

            elif choice == '5':
                search_term = input("Enter student name to search: ")
                found_students = gradebook.search_students_by_name(search_term)
                if found_students:
                    print(f"\nFound {len(found_students)} student(s):")
                    for student in found_students:
                        student.print_details()
                else:
                    print("No students found matching your search.")

            elif choice == '6':
                gradebook.sort_by_average()

            elif choice == '7':
                print("Available subjects:", ", ".join(subjects))
                subject = input("Enter subject to sort by: ")
                gradebook.sort_by_subject(subject)

            elif choice == '8':
                gradebook.sort_students_by_name()

            elif choice == '9':
                print("Available subjects:", ", ".join(subjects))
                subject = input("Enter subject: ")
                gradebook.view_subject_grades(subject)

            elif choice == '10':
                run_comprehensive_tests()

            elif choice == '11':
                print("Thank you for using the Enhanced Grading System!")
                print("Goodbye!")
                break

            else:
                print("Invalid choice! Please enter a number from 1 to 11.")

        except KeyboardInterrupt:
            print("\n\nProgram interrupted by user. Goodbye!")
            break
        except Exception as error:
            print(f"Unexpected error: {error}")


# Run the program
if __name__ == "__main__":
    main()