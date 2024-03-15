# This is how we log or print in Python

print("Hello World!")

# With quotes its print statement otherwise without quotes its considered as a variable

# String:

name: str = "Muhammad Ali"

# name: str = 7777 # Will run it and not show errors but will create problems at later on stages in complex code.
# to manually check for errors use: mypy [filename.py]

print(name)

print(type(name)) # This is how we check type in python

print(id(name)) # This is how we check Psychical Address

# print(dir(name)) # Shows all the attributes of a variable

# Here's a breakdown of what each part of the below code does:
# 1. dir(name): This returns a list of all the attributes of the object name.
# 2. for i in dir(name): This iterates over each attribute in the list obtained from dir(name).
# 3. if "__" not in i: This condition checks if the attribute name does not contain the substring "__" (double underscore).
# 4. [i for i in dir(name) if "__" not in i]: This is a list comprehension that filters out the attributes that do not contain double underscores.
# 5. print(...): Finally, the filtered list of attributes is printed out.

print([i for i in dir(name) if "__" not in i])

# Number:

num: int = 7777

print(num)

print(type(num))

print(id(num))

print([i for i in dir(num) if "__" not in i])

# Decimal Number:

decnum: float = 7.0

print(decnum)

print(type(decnum))

print(id(decnum))

print([i for i in dir(decnum) if "__" not in i])

# Boolean:

booleanTest: bool = True

print(booleanTest)

print(type(booleanTest))

print(id(booleanTest))

print([i for i in dir(booleanTest) if "__" not in i])

# List: (somewhat like arrays)

listTest: list[str] = ['A', 'B', 'C', 'D']

print(listTest)

print(type(listTest))

print(id(listTest))

print([i for i in dir(listTest) if "__" not in i])

# Tuple:

tupleTest: tuple[str, int, float] = ('Testing', 1234, 0.1234)

print(tupleTest)

print(type(tupleTest))

print(id(tupleTest))

print([i for i in dir(tupleTest) if "__" not in i])