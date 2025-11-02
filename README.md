SECTION A - INITIAL SETUP, SCALAR OBJECTS AND LOOPS
This part uses loops and scalar variables to introduce the fundamental grading scheme. 
The program lets the user enter the number of pupils in a class, followed by the name and grade of each student for a specific topic.
It presents all student results and the class summary, computes the total and average grades, and verifies that grades are between 0 and 100.

Key Features
- Accepts the number of students as input.
- Uses a for loop to collect student names and grades.
- Validates that grades are between 0 and 100.
- Calculates and displays:
- Each student’s name and grade.
- The total of all grades
- The average class grade

CONCEPTS USED
- Input and output (input(), print())
- Loops (for, while)
- Scalar variables (int, float, str)
- Basic arithmetic operations
- Conditional validation (if and else)

How to Use:
Run the program and follow prompts to enter student data.

Sample Input:
Enter number of students: 2
Enter student name: John
Enter grade: 85
Enter student name: Sarah  
Enter grade: 92

Sample Output:
John: 85.0
Sarah: 92.0
Class Average: 88.5

SECTION B
In order to manage several subjects for each student, this part introduces compound data structures, such as lists and tuples, which improve the grading system.
The grades for math, science, English, Setswana, and agriculture are now listed for each student and are kept in a tuple with their name.
Additionally, the program shows comprehensive summaries for each student and calculates per-subject statistics (highest and lowest grade).

KEY FEATURES
- Stores subjects in a list.
- Stores student records as tuples → (name, [grades]) inside a main list.
- Validates each subject grade (0 – 100).
- Calculates and displays:
 - Highest and lowest grade for each subject.
 - Each student’s grades per subject and overall average.
 - The overall class averages

CONCEPTS USED
- Lists ([]) to hold subjects and grades.
- Tuples (()) to pair each student’s name with their grades list.
- Nested loops for students × subjects.
- Aggregate functions max() and min() for per-subject stats.
- Arithmetic to compute per-student and overall averages

How to Use:
Run the program and enter grades for all three subjects for each student.

Sample Input/Output:
Student: John
Math: 85, English: 78, Science: 92
Average: 85.0

Math Statistics:
Average: 87.5, Highest: 95, Lowest: 85

SECTION C
To enable more adaptable and effective data storage and retrieval, this section substitutes dictionaries for the list and tuple structures.
The value is a different dictionary that contains the students' grades for every topic, and each student's name becomes a key in the main dictionary (students_dict).
To enable users to carry out different tasks interactively, a menu-driven interface was developed.

Key Features
- Stores all student data in a nested dictionary structure:
{ student_name: { subject_name: grade } }
- Allows users to:
 - Add new students and their grades.
 - Update existing grades for any subject.
- Remove students from the system.
- View all students with their grades and averages.
- Search for a student by name to view their details.
- View all grades for a specific subject and calculate its statistics (average, highest, lowest).
- Validates grade input (0–100) and provides clear messages for invalid entries.
- Implements a continuous menu loop until the user chooses to exit.

Concepts Used
- Dictionaries: to map student names to their grades.
- Nested dictionaries: to represent each subject–grade pair inside a student record.
- Loops and Conditionals: for menu navigation and repeated data entry.
- Exception Handling: using try / except to manage invalid input.
- Modular thinking: preparing the structure for later conversion to functions and classes.

How to Use:
Use the menu system to navigate between different operations.

Sample Input/Output:
1. Add student
2. Update grades
Choose: 1
Enter name: Alice
Enter Math grade: 88
Enter English grade: 92
Added Alice successfully

SECTION D
In order to increase readability, maintenance, and scalability, this section focuses on reorganizing the grading system into separate, reusable functions.
Smaller helper functions for tasks like grade validation, name input, and average computation support the larger functions that handle each major operation:
- adding, updating, removing, viewing, and searching for students.
These functions are now called by the main program loop in response to the user's menu option.

Key Features
- Functional design: breaks the program into logical, self-contained functions.
- Helper functions:
  - get_grade() – validates numeric input between 0 and 100.
  - get_student_name() – checks for non-empty names.
  - calculate_average() – safely computes averages.
- Core functions:
  - add_student(), update_grades(), remove_student(), view_students(), search_student(), view_subject().
- Display helpers: standardize the layout of student details and subject summaries.
- Menu handling: handled by a dedicated show_menu() function that uses a mapping dictionary to connect menu options to
their corresponding actions.
- Improved validation: prevents duplicate entries, invalid grades, and empty names.

Concepts Used
- Functions with clear input/output design.
- Docstrings for internal documentation and clarity.
- Mapping dictionary for clean function calls.
- Exception handling (try / except) for safe user input.
- Modular programming principles promoting code reuse and readability.

How to Use:
Functions are called based on menu selections, providing clean separation of concerns.

Sample Input/Output:
def add_student(): - Handles complete student addition process
def validate_grade(): - Ensures grade is valid number 0-100
def search_student(): - Finds student and allows grade updates

SECTION E
Description:
This section converts the procedural system to object-oriented programming using classes and methods. 
The Student class encapsulates student data and behaviors, while the Gradebook class manages the 
collection of students and provides advanced operations.

Key Features:
- Student class with attributes for name and grades dictionary
- Methods for adding grades, calculating averages, and printing details
- Gradebook class managing collection of Student objects
- Advanced operations: add, remove, search, and sort students
- Comprehensive testing suite with unit and integration tests
- Sorting students by average grade or specific subjects
- Input validation helper functions

Concepts Used:
- Class definition and object instantiation
- Encapsulation of data and methods
- Object composition (Gradebook contains Students)
- Method invocation on objects
- List comprehensions for data processing
- Lambda functions for sorting
- Unit testing and integration testing

How to Use:
Create Student objects and manage them through Gradebook class methods.

Sample Input/Output:
student = Student("John")
student.add_grade("Math", 85)
average = student.calculate_average()

gradebook = Gradebook(["Math", "English"])
gradebook.add_student("John")
sorted_students = gradebook.sort_by_average()

SECTION F
Description:
This final section adds robust exception handling and advanced features to create a production-ready system. 
Custom exceptions provide specific error handling, and manual sorting algorithms demonstrate algorithm implementation.

Key Features:
- Custom exception classes (StudentNotFoundError, InvalidGradeError, etc.)
- Comprehensive try-except blocks throughout all methods
- Manual implementation of bubble sort and insertion sort algorithms
- Enhanced search with partial name matching
- Professional error messages and user feedback
- Input validation preventing numbers in student names
- Alphabetical sorting of student names
- Edge case handling and boundary testing

Concepts Used:
- Custom exception classes inheritance
- Try-except-finally error handling
- Manual sorting algorithm implementation
- String validation and manipulation
- Professional user interface design
- Comprehensive test automation
- Algorithm analysis and implementation

How to Use:
The system now gracefully handles errors and provides professional user experience.

Sample Input/Output:
Enter student name: John123
Error: Student name cannot contain numbers

STUDENTS SORTED BY NAME (A to Z)
Using Bubble Sort Algorithm
Alice
David
John

COMPREHENSIVE TESTING
Description:
The system includes automated testing functions that verify all functionality including unit tests, 
integration tests, and edge case testing.

Key Features:
- Unit tests for individual class methods
- Integration tests for system workflow
- Edge case testing (empty data, boundary values)
- Automated test execution via menu option
- Detailed test documentation in code comments

Testing Coverage:
- Student class initialization and methods
- Gradebook management operations
- Sorting algorithm correctness
- Error handling scenarios
- Input validation boundaries

How to Run Tests:
Choose "Run Tests" option from main menu to execute comprehensive test suite.

INSTALLATION AND USAGE
Sample Workflow:
1. Add students with grades
2. View all students and their averages
3. Sort students by average or name
4. Search for specific students
5. Update grades as needed
6. View subject-specific statistics

Assumptions and Limitations:
- Three fixed subjects: Math, English, Science
- Grades range from 0-100
- Student names cannot contain numbers
- No persistent data storage between sessions
- Single grade per subject per student

This grading system demonstrates progressive enhancement from basic programming concepts to advanced 
object-oriented design with comprehensive error handling and testing.

SYSTEM REQUIREMENTS:
- Python Version: 3.6 or higher

INSTALLATION INSTRUCTIONS:
1. VERIFY PYTHON INSTALLATION:
   - Open command prompt/terminal
   - Type: python --version
   - If Python is not installed, download from python.org

2. DOWNLOAD PROJECT FILES:
   - Ensure all section files are in one folder:
     SectionA.py, SectionB.py, SectionC.py, SectionD.py, SectionE.py, SectionF.py

RUNNING THE SYSTEM:
BASIC EXECUTION:
1. Open command prompt/terminal
2. Navigate to project folder: cd path/to/your/project/folder
3. Run desired section: python SectionF.py

RECOMMENDED STARTUP:
- Start with SectionF.py for the complete system
- This includes all features from previous sections

MENU NAVIGATION GUIDE:
MAIN MENU OPTIONS:
1. Add Student      - Create new student and enter all grades
2. Update Grades    - Modify existing student's grades
3. Remove Student   - Delete student from system
4. View All Students- Display all students with details
5. Search Student   - Find student by name (partial match)
6. Sort by Average  - Show students sorted by average (high to low)
7. Sort by Subject  - Show students sorted by specific subject grade
8. Sort by Name     - Show students sorted alphabetically (A-Z)
9. View Subject Grades - See all grades for one subject with statistics
10. Run Tests       - Execute comprehensive test suite
11. Exit            - Close the program

STEP-BY-STEP USAGE EXAMPLES:
EXAMPLE 1: ADDING A NEW STUDENT
1. Choose option 1 from menu
2. Enter student name: "Emily"
3. Enter Math grade: 88
4. Enter English grade: 92
5. Enter Science grade: 85
6. System confirms addition and shows average

EXAMPLE 2: UPDATING GRADES
1. Choose option 2 from menu
2. Enter existing student name: "John"
3. View current grades displayed
4. Enter new Math grade: 95
5. Enter new English grade: 88
6. Enter new Science grade: 90
7. System confirms update

EXAMPLE 3: VIEWING STATISTICS
1. Choose option 9 from menu
2. Select subject: "Math"
3. System shows:
   - All student grades for Math
   - Class average
   - Highest and lowest grades
   - Number of students with grades

EXAMPLE 4: RUNNING COMPREHENSIVE TESTS
1. Choose option 10 from menu
2. System automatically runs:
   - Unit tests for all classes and methods
   - Integration tests for system workflow
   - Edge case testing
   - Performance verification
3. View test results and confirmation messages

INPUT REQUIREMENTS AND VALIDATION:
STUDENT NAMES:
- Cannot be empty
- Cannot contain numbers
- Case insensitive for searching
- Spaces are automatically trimmed

GRADES:
- Must be numbers between 0-100
- Decimal grades are converted to integers
- Invalid inputs prompt for re-entry

SUBJECTS:
- Fixed set: Math, English, Science
- Case insensitive for input
- Invalid subjects show error message

TROUBLESHOOTING:
COMMON ISSUES:
1. "Python not found" error:
   - Solution: Install Python or add to PATH

2. "File not found" error:
   - Solution: Ensure all .py files are in same folder

3. Program crashes on invalid input:
   - Solution: Use Section F which has comprehensive error handling

4. Menu not displaying properly:
   - Solution: Ensure terminal supports UTF-8 encoding

TESTING THE SYSTEM:
COMPREHENSIVE TESTING:
- Use Option 10 to run automated tests
- Tests verify:
  * Student creation and management
  * Grade calculations and averages
  * Sorting algorithms correctness
  * Error handling scenarios
  * Edge case performance

MANUAL TESTING SCENARIOS:
1. Test with empty student name
2. Test with grades outside 0-100 range
3. Test searching for non-existent student
4. Test sorting with various grade combinations
5. Test subject selection with invalid names

DATA PERSISTENCE NOTE:
- Data is stored only during program execution
- All data is lost when program closes
- For permanent storage, consider database integration in future versions

SUPPORTED PLATFORMS:
- Windows: Tested on Windows 10/11 with Python 3.8+


# nathane_lebogang_python_assignment
