# Personal Information Manager
# Week 1 task by D. Vignesh
# A simple personal information display tool.

# Welcome message
print("=" * 40)
print("    PERSONAL INFORMATION MANAGER")
print("=" * 40)
print()

# Store static information
name = "D. Vignesh"
age = 22
city = "Hyderabad"
profession = "student"

# Get user input
print("Please tell me about yourself:")
print("-" * 30)

favorite_hobby = input("What is your favorite hobby? ")
while favorite_hobby == "":
    print("Please enter a valid hobby! \n If you don't have a favorite hobby please enter 'none'.")
    favorite_hobby = input("What is your favorite hobby? ")

favorite_color = input("What is your favorite color? ")
while favorite_color == "":
    print("Please enter a valid color! \n If you don't have a favorite color please enter 'none'.")
    favorite_color = input("What is your favorite color? ")

# Calculate age in months
age_in_months = age * 12

# String corrections
city = city.title()
profession = profession.title()
favorite_hobby = favorite_hobby.title()
favorite_color = favorite_color.title()

# Display all information
print()
print("=" * 40)
print("        YOUR INFORMATION")
print("=" * 40)
print()

print(f"Name: {name}")
print(f"Age: {age} ({age_in_months} months old)")
print(f"City: {city}")
print(f"Profession: {profession}")
print()
print(f"Favorite Hobby: {favorite_hobby}")
print(f"Favorite Color: {favorite_color}")
print()

# Goodbye message
print("=" * 40)
print("Thanks for using this program!")
print("=" * 40)