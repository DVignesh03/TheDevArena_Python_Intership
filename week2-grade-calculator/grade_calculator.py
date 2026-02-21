# Student Grade Calculator
# Week 2 project

# Grading system function
def calculate_grade(avg):
    if avg >= 90:
        return 'A', 'Excellent'
    elif avg >= 80:
        return 'B', 'Very good'
    elif avg >= 70:
        return 'C', 'Room for improvement'
    elif avg >= 60:
        return 'D', 'Needs improvement'
    else:
        return 'F', 'Failed'

# Input validation for numbers    
min_val = 0
max_val = 100
def get_valid_number(prompt, min_val, max_val):
    """Get a valid number within specified range"""
    while True:
        try:
            value = float(input(prompt))
            if min_val <= value <= max_val:
                return value
            else:
                print(f"Please enter a number between {min_val} and {max_val}")
        except ValueError:
            print("Invalid input! Please enter a number.")

# Initializing lists for storing data
# Store names, marks and results (average, grade, comment)    
st_names = []
st_marks = []
st_results = []
def get_student_info():
    # Get student info and calculate results
    while True:
        try:
            st_count = int(input("Enter number of students: "))
            if st_count > 0:
                break
            else:
                print("Enter a positive numebr")
        except ValueError:
            print("Invalid input! Whole number needed.")

    # Collect data
    for i in range(st_count):
        print(f"\n=== STUDENT {i+1} ===")
        # Ask for student info
        name = input("Student name: ")
        while name.strip() == "":
            print("Name cannot be empty!")
            name = input("Student name: ")
        st_names.append(name)

        # Collect marks and generate result
        print("Enter the marks obtained (0-100)")
        math = get_valid_number("Math: ", min_val, max_val)
        science = get_valid_number("Science: ", min_val, max_val)
        english = get_valid_number("English: ", min_val, max_val)

        st_marks.append([math, science, english])
        avg = (math + science + english) / 3
        grade, comment = calculate_grade(avg)
        st_results.append({
            'average': avg,
            'grade': grade,
            'comment': comment
        })
    return st_count # Return the student count. Modular approach taken.

# Print all data    
def publish_info(st_count):
    print("\n" + "=" * 50)
    print("            RESULTS SUMMARY")
    print("=" * 50)
    print(f"{'Name':<20} | {'Avg':>5} | {'Grade':^5} | Comment")
    print("-" * 60)

    for i in range(st_count): # Fetch student info
        name = st_names[i]
        avg = st_results[i]['average']
        grade = st_results[i]['grade']
        comment = st_results[i]['comment']

        print(f"{name:<20} | {avg:>5.1f} | {grade:^5} | {comment}")

    if st_count > 0:
        avgs = [result['average'] for result in st_results]
        class_avg = sum(avgs) / len(avgs)
        max_avg = max(avgs)
        min_avg = min(avgs)
        max_index = avgs.index(max_avg)
        min_index = avgs.index(min_avg)

        print("\n" + "=" * 50)
        print("          CLASS STATISTICS")
        print("=" * 50)
        print(f"Total Students: {st_count}")
        print(f"Class Average: {class_avg:.1f}")
        print(f"Highest Average: {max_avg:.1f} ({st_names[max_index]})")
        print(f"Lowest Average: {min_avg:.1f} ({st_names[min_index]})")

def main():
    print("=" * 50)
    print("      STUDENT GRADE CALCULATOR")
    print("=" * 50)
    print()

    student_count = get_student_info() # Modular approach in action
    publish_info(student_count)

    print("\n" + "=" * 50)
    print("Thank you for using the Grade Calculator!")
    print("=" * 50)

if __name__ == "__main__":
    main()