from typing import Union

# Simple if-else structure example

if True:  # Condition is True
    print("Pakistan")  # Executes if condition is True
else:
    print("Other")  # Executes if condition is False

# Another if-else example with condition as False

if False:  # Condition is False
    print("Pakistan")
else:
    print("Other")  # Executes since condition is False

# Ternary operator for concise if-else statements

print("HyperX") if True else print("Razer")  # One-liner conditional logic

# Example of if, elif, else chain

if True:  # First condition is True, so this block runs
    print("True_block")
elif False:  # Skipped, as previous condition was True
    print("elif logic 1")
elif False:  # Skipped
    print("elif logic 2")
elif False:  # Skipped
    print("elif logic 3")
else:  # Skipped, no conditions triggered this block
    print("Final else block")

print("If else logic completed")  # Code execution reaches here after conditions

# Grading system based on percentage

percentage: Union[int, float] = float(input("Enter your percentage: "))  # Accepts percentage input
grade: Union[str, None] = None  # Variable to store grade

# Determine grade based on percentage ranges
if (percentage >= 90) and (percentage <= 100):
    grade = "A* Grade"
elif (percentage >= 80) and (percentage < 90):
    grade = "A Grade"
elif (percentage >= 70) and (percentage < 80):
    grade = "B Grade"
elif (percentage >= 60) and (percentage < 70):
    grade = "C Grade"
elif (percentage >= 50) and (percentage < 60):
    grade = "D Grade"
elif (percentage >= 40) and (percentage < 50):
    grade = "E Grade"
else:
    grade = "U Grade"  # Grade U for anything below 40%

print(f"Dear Student, your percentage is {percentage} and your calculated grade is {grade}.")

# List of student percentages

PerType = Union[float, int]  # Custom type for percentage (int or float)
percentages: list[PerType] = [39, 40, 49, 55, 59.5, 60, 65, 73, 85, 95, 100]  # Sample percentage data

grades: list[str] = []  # Empty list to store grades

# Loop through percentages and assign grades based on the same logic
for per in percentages:
    s_grades: str = ""  # Temporary variable for storing grade
    
    # Determine grade based on percentage ranges
    if (per >= 90) and (per <= 100):
        s_grades = "A*"
    elif (per >= 80) and (per < 90):
        s_grades = "A"
    elif (per >= 70) and (per < 80):
        s_grades = "B"
    elif (per >= 60) and (per < 70):
        s_grades = "C"
    elif (per >= 50) and (per < 60):
        s_grades = "D"
    elif (per >= 40) and (per < 50):
        s_grades = "E"
    else:
        s_grades = "U"  # Below 40% gets a U grade

    grades.append(s_grades)  # Append each grade to the list

# Display the percentage and corresponding grades
print(percentages)
print(grades)

# Use zip to combine percentages and grades into pairs
print(list(zip(percentages, grades)))

# Assign roll numbers to students (0 to len(percentages)-1)
roll_no: list[int] = list(range(len(percentages)))

# Display the roll number, percentage, and grade for each student
print(list(zip(roll_no, percentages, grades)))

# Combine roll numbers, percentages, and grades into a database (list of tuples)
database = list(zip(roll_no, percentages, grades))

# Sort the database by percentage in descending order
print(sorted(database, key=lambda x: x[1], reverse=True))

# Another example: Working with a list of cars

cars: list[str] = ["audi", "bmw", "subaru", "toyota"]  # List of car names
for car in cars:
    if car == 'bmw':  # Check for specific condition
        print(car.upper())  # Print 'bmw' in uppercase
    else:
        print(car.title())  # Print other car names with title case

# Check if an item is in the list
print('changan' in cars)  # Returns False since 'changan' is not in the list

# Example with a list of banned users

banned_users: list[str] = ['andrew', 'carolina', 'david']  # List of banned users
user: str = 'marie'

# Check if user is not banned
if user not in banned_users:
    print(f"{user.title()}, you can post a response if you wish.")

# Login system example

user_name: str = input("Enter User ID: ")  # User input for ID
user_password: str = input("Enter Password: ")  # User input for password

# Check if credentials are correct
if user_name == 'admin' and user_password == '7896':  # Fixed login credentials
    print("Sent OTP")
    otp: str = input("Please Enter OTP: ")  # User input for OTP
    if otp == '1234':  # Check if OTP matches
        print("Login Success")  # Successful login message
else:
    print("Invalid User ID or Password")  # Error message for invalid login
