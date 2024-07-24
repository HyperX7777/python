# String data type in python

# Boundaries for writing string in python
# 'string', "string", '''string''' & """string"""

name : str = 'Muhammad Qasim'
fname : str = "Muhammad Aslam"
education : str = '''Master in Computer Science'''
age : str = """27"""

# If we want to use a single quote in some text we have to use double quote to make it string
# It's the opposite for using double quotes in the text

# card_info1 : str = 'Student Card \n Father's name' # ERROR
card_info1 : str = "Student Card \n Father's name"

# card_info2 : str = "Student Card" \n Student name" # ERROR
card_info2 : str = '"Student Card" \n Student name'

# Convert any special character into simple character
# Place \ before character

# card_info3 : str = 'Student Card \n Father's name' # ERROR
card_info3 : str = 'Student Card \n Father\'s name'

# Student Card

name1 : str = "Furqan Ahmed"
fname1 : str = "Moshin Mughal"
education1 : str = "Master in Computer Science"
age1 : int = 19

# Concatenation using + and \n used to bring text to the next line

card_info4 : str = "Student Card\nName: " + name1 + "\nFather's Name: " + fname1

print(card_info4)

# String and Number cannot be concatenated so we have make them of same type to concatenate.
# We are using a function str() to make the value of age1 go through function and convert it into string.

card_info5 : str = "Student Card\nName: " + name1 + "\nAge: " + str(age1)

print(card_info5)

