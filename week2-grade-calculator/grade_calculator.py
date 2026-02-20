# Student Grade Calculator
# Week 2 project

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
    
min_val = 0, max_val = 100

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