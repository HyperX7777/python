from typing import Any

# How to get help in Python.

#* help(object)
#* object?
#* object??
#* ?object
#* ??object

# Initializing Lists

names = ["Qasim", "Junaid", "Zia"]

# Benefits of Lists:
# Dyanmic Length
# Heterogeneous data types (Multiple types)
# Index:
#       Positive: 1 to maxiumum length
#       Negative: -1 to maxiumum - (minus) length

# Positive
names1 = ["Qasim", "Junaid", "Zia"]
#            0         1       2

print(names1[0])

# Negative
names2 = ["Qasim", "Junaid", "Zia"]
#           -3        -2      -1

print(names2[-1])

# Type any

names3: list[Any] = ["Sir Qasim", "Sir Zia", "Sir Junaid"]

print(f'Founder of PIAIC: {names3[-2]}')

# Slicing:
#       Start : int = include
#       End : int = n-1 (Meaning minus from last number)
#       Step : int = sequence

characters: list[str] = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")

# Using list function in it to get the elements in list form

print(characters)

# Default slicing goes from left to right.

#                          0    1    2    3    4    5    6    7    8    9    10   11   12   13   14   15   16   17   18   19   20   21   22   23   24   25
characters1: list[str] = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
#                         -26  -25  -24  -23  -22  -21  -20  -19  -18  -17  -16  -15  -14  -13  -12  -11  -10  -9   -8   -7   -6   -5   -4   -3   -2   -1

# Start

print(characters1[0:2]) # 0 = Included : Index 2 - 1 = 1
# The Last Index will not be included like 2 in this case

print(characters1[:2]) # Not passing any number = all
# If you omit the start index, Python will start from the beginning of the list.

# End

print(characters1[-26:-23]) # -26 = Included : Index -23 - 1 = -24

# Step (Sequence)

print(characters1[0:4:1]) # 0 = Included : Index 4-1 = 3 : 1 = Sequence (How many steps to leave)

print(characters1[-26:-14:1]) # -26 = Included : Index -26-14 = -12 : 1 = Sequence (How many steps to leave)

# Python is Mutable meaning that the list can be changed after it has been created.

names4: list[Any] = ["Qasim", "Sir Zia", "Sir Junaid", "Extra 1", "Extra 2"]

names4[0] = "Sir Qasim"

print(names4)

# Deleting using del (Method 1)

del names4[4] # Non return function

print(names4) # Deleted

# List Methods

listmethods = [i for i in dir(list) if "__" not in i]

print(listmethods)

# Deleting using pop method (Method 2)

rvaluecheck : str = names4.pop() # Return function

print(names4) # Deleted

print(rvaluecheck) # Return value received.

# Adding using append method

names5: list[Any] = ["Sir Ameen Alam"]

# Append adds element in last

names5.append("Sir Qasim") 
names5.append("Sir Junaid")
names5.append("Sir Zia")

print(names5)

# Adding using insert method

names6: list[Any] = ['Sir Qasim', 'Sir Junaid', 'Sir Zia']

# Insert adds element at desired position

names6.insert(1 ,"Sir Hassan") 

print(names6)

# Remove value but keep the object

names7: list[Any] = ['Sir Qasim', 'Sir Junaid', 'Sir Zia']

names7.clear() # Removes all elements

print(names7)

# Count elements

data : list[str] = ['a', 'a', 'a', 'b', 'c', 'c', 'c', 'c']

print(data.count("a"))
print(data.count("c"))

# Appending list (Problem: Adding whole list in list not elements in list)

founding_members: list[Any] = ['Sir Qasim', 'Sir Ameen Alam', 'Sir Zia']

new_members: list[Any] = ['Sir Junaid', 'Sir Hassan']

founding_members.append(new_members)

print(founding_members)

# Extend (Adds elements one by one and solves the problem)

founding_members1: list[Any] = ['Sir Qasim', 'Sir Ameen Alam', 'Sir Zia']

new_members1: list[Any] = ['Sir Junaid', 'Sir Hassan']

founding_members1.extend(new_members1)

print(founding_members1)

# Remove using value

names8: list[str] = ['Sir Qasim', 'Sir Ameen Alam', 'Sir Zia']

names8.remove("Sir Zia")

print(names8)

# Check Index number

names9: list[str] = ['Sir Qasim', 'Sir Ameen Alam', 'Sir Zia']

print(names9.index("Sir Ameen Alam"))

# Reverse Method (Changes real data in memory)

names10: list[str] = ['Sir Qasim', 'Sir Ameen Alam', 'Sir Zia', 'Sir Junaid']

print(names10)

names10.reverse()

print(names10)

# Sort Method (Sorting in ascending order)

names11: list[str] = ['Sir Qasim', 'Sir Ameen Alam', 'Sir Zia', 'Sir Junaid']

print(names11)

names11.sort()

print(names11)

# Sort Method (Sorting in descending order)

names12: list[str] = ['Sir Qasim', 'Sir Ameen Alam', 'Sir Zia', 'Sir Junaid']

print(names12)

names12.sort(reverse=True)

print(names12)