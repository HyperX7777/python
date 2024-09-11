# List Operations
# Iterating over a list using different types of loops and applying operations on elements.

# While Loop
names1: list[str] = ['Sir Zia', 'Sir Qasim', 'Sir Ameen', 'Sir Junaid']

i: int = 0  # Initialize counter = 0

# Loop through 'names1' using a while loop
while i < len(names1):  # Loop until i is less than the length of the list
    print(names1[i])  # Print the current name
    i += 1  # Increment counter


# For Loop
names2: list[str] = ['Sir Zia', 'Sir Qasim', 'Sir Ameen']

# Loop through 'names2' using a for loop
for name1 in names2:
    print(name1)  # Print each name


# Using the Enumerate Function
# 'enumerate()' allows you to loop over a list and keep track of the index
print(list(enumerate(names2)))  # Prints list of tuples (index, value)


# For Loop with a Welcome Message and List Method
names3: list[str] = ['Sir Zia', 'Sir Qasim', 'Sir Ameen', 'Extras']

print("PIAIC Gen AI Team:")

# Loop through the first three names in 'names3' using list slicing
for name2 in names3[:3]:  # Accessing only the first 3 elements
    print(f'Welcome {name2.title()}')  # Welcoming each name with title case


# Authentication Check Using a For Loop

# A list of tuples representing username and password
data_base: list[tuple[str, str]] = [
    ("HyperX", '7777'),
    ("Razer", '1234'),
    ("Logitech", '9999')
]

# Taking user input for username and password
input_user: str = input("Enter username: ")
input_password: str = input("Enter password: ")

# Checking if the entered credentials match any in the database
for row in data_base:
    user, password = row  # Unpacking tuple into 'user' and 'password'
    if input_user == user and input_password == password:
        print("Valid User")  # If credentials match, print valid user
        break  # Exit the loop once a match is found
else:
    print("Invalid User")  # If no match is found, print invalid user


# Working with Numbers in Loops

# Print even numbers from 2 to 20 using range with step
print(list(range(2, 21, 2)))  # Creates a list of even numbers


# Printing a multiplication table for 2
for n in range(1, 11):
    print(f"{2} X {n} = {n * 2}")  # Prints 2 multiplied by numbers from 1 to 10


# Calculating Squares of Values

squares: list[int] = []  # Create an empty list to store squares

# Loop through numbers from 1 to 10 and append their squares to the list
for value in range(1, 11):
    square = value ** 2  # Calculate the square of the current value
    squares.append(square)  # Add the square to the 'squares' list
print(squares)  # Print the list of squares


# List Comprehension Example

# A more concise way to generate the list of squares using list comprehension
print([i**2 for i in range(1, 11)])  # Prints squares of numbers from 1 to 10


# Tuple Example and Definition

# A tuple is a collection which is ordered and immutable (cannot be changed).
# Tuples are defined by using parentheses () and can hold elements of different types.

# Example of a tuple:
my_tuple: tuple[str, int] = ("PIAIC Student", 100)

# Accessing elements in a tuple
name, score = my_tuple  # Unpacking the tuple into variables
print(f"Name: {name}, Score: {score}")  # Output the values

# Tuples can also be used in lists, as seen earlier in the database example.
# They are useful when you want to store a collection of related data that shouldn't change.
