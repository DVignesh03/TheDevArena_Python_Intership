# Personal Information Manger

## Project Description

This is a simple script used to perform basic operations like asking user input and displaying it. It has already some information stored.

## What I learned

1. **Variables**: How to store different types of data.
2. **Input/Output**: Getting user input and displaying it.
3. **String Formatting**: Using f-strings to create a nice output.
4. **Error Handling**: Basic validation of user input.

## How To Run This Program

1. Make sure you have Python installed
2. Open command prompt/terminal
3. Navigate to project folder
4. Run: `python personal_info.py`
5. Follow the prompts to enter your information

## Features

- Stores static information (name, age, city, profession)
- Gets dynamic information from the user (favorite hobby, color)
- Displays all information in a formatted way
- Basic input validation
- Age calculation in months

## Sample Output

========================================
    PERSONAL INFORMATION MANAGER
========================================

Please tell me about yourself:
------------------------------
What is your favorite hobby? gaming
What is your favorite color? red

========================================
        YOUR INFORMATION
========================================

Name: D. Vignesh
Age: 22 (264 months old)
City: Hyderabad
Profession: Student

Favorite Hobby: Gaming
Favorite Color: Red

========================================
Thanks for using this program!
========================================

## Challenges & Solutions

**Challenge**: User might enter empty input
**Solution**: Added an if statement to check for empty input

**Challenge**: Formatting the output nicely
**Solution**: Used f-strings with proper spacing