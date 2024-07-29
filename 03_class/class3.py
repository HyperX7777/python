# Initializing variables
a: int = 7
b: int = 3

# Arithmetic Operators

# Addition Arithmetic
print(f"The sum of {a} and {b} is {a + b}")

# Subtraction Arithmetic
print(f"The difference when {b} is subtracted from {a} is {a - b}")

# Multiplication Arithmetic
print(f"The product of {a} and {b} is {a * b}")

# Division Arithmetic
print(f"The quotient when {a} is divided by {b} is {a / b}")

# Modulus Arithmetic
print(f"The remainder when {a} is divided by {b} is {a % b}")

# Exponentiation Arithmetic
print(f"{a} raised to the power of {b} is {a ** b}")

# Floor Division Arithmetic
print(f"The result of floor division of {a} by {b} is {a // b}")

# Initializing variables
c: int = 15
d: int = 3

# Assignment Operators

# Standard Assignment
c = 15  # Reset value of c
c = d
print(f"Standard Assignment: c = d results in c = {c}")

# Addition Assignment
c = 15  # Reset value of c
c += d
print(f"Addition Assignment: c += d results in c = {c}")

# Subtraction Assignment
c = 15  # Reset value of c
c -= d
print(f"Subtraction Assignment: c -= d results in c = {c}")

# Multiplication Assignment
c = 15  # Reset value of c
c *= d
print(f"Multiplication Assignment: c *= d results in c = {c}")

# Division Assignment
c = 15  # Reset value of c
c = int(c / d)  # Casting to int to maintain type consistency
print(f"Division Assignment: c /= d results in c = {c}")

# Modulus Assignment
c = 15  # Reset value of c
c %= d
print(f"Modulus Assignment: c %= d results in c = {c}")

# Floor Division Assignment
c = 15  # Reset value of c
c = c // d  # Floor division result is an int, so no need to cast
print(f"Floor Division Assignment: c //= d results in c = {c}")

# Initializing variables
x: int = 15
y: int = 10

# Comparison Operators

# Equal
result = x == y
print(f"Equal: {x} == {y} results in {result}")

# Not Equal
result = x != y
print(f"Not Equal: {x} != {y} results in {result}")

# Greater Than
result = x > y
print(f"Greater Than: {x} > {y} results in {result}")

# Less Than
result = x < y
print(f"Less Than: {x} < {y} results in {result}")

# Greater Than or Equal To
result = x >= y
print(f"Greater Than or Equal To: {x} >= {y} results in {result}")

# Less Than or Equal To
result = x <= y
print(f"Less Than or Equal To: {x} <= {y} results in {result}")

# Initializing variables
e: int = 7
f: int = 12

# Logical Operators

# and: Returns True if both statements are true
result = (e < 10) and (f > 5)
print(f"Logical AND: (e < 10) and (f > 5) results in {result}")

# or: Returns True if one of the statements is true
result = (e < 10) or (f < 5)
print(f"Logical OR: (e < 10) or (f < 5) results in {result}")

# not: Reverse the result, returns False if the result is true
result = not ((e < 10) and (f < 15))
print(f"Logical NOT: not((e < 10) and (f < 15)) results in {result}")

# Initializing variables
g: int = 5
h: int = 5

# Identity Operators

# is: Returns True if both variables point to the same object
result = (g is h)
print(f"Identity IS: g is h results in {result}")

# is not: Returns True if both variables point to different objects
result = (g is not h)
print(f"Identity IS NOT: g is not h results in {result}")

# Additional demonstration with mutable types
# Note: For mutable types (like lists), `is` checks if they refer to the same object in memory
g_list: list = [1, 2, 3]
h_list: list = [1, 2, 3]

# Checking identity for mutable types
result = (g_list is h_list)
print(f"Identity IS with lists: g_list is h_list results in {result}")

# Checking identity for mutable types with same reference
g_list = h_list  # Now g_list and h_list refer to the same object
result = (g_list is h_list)
print(f"Identity IS after reassignment: g_list is h_list results in {result}")

# Initializing variables
i: int = 3
j: list = [1, 2, 3, 4, 5]

# Membership Operators

# in: Returns True if the value is present in the sequence
result = (i in j)
print(f"Membership IN: {i} in {j} results in {result}")

# not in: Returns True if the value is not present in the sequence
result = (i not in j)
print(f"Membership NOT IN: {i} not in {j} results in {result}")

# Additional examples with strings and other sequences

# String example
string: str = "hello world"
char: str = 'w'

# Checking membership in a string
result = (char in string)
print(f"Membership IN with string: '{char}' in '{string}' results in {result}")

# Checking membership not in a string
result = (char not in string)
print(f"Membership NOT IN with string: '{char}' not in '{string}' results in {result}")
