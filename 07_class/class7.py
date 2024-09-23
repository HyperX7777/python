from typing import Dict, Union, Optional
import pprint

# List - Index
data1: list[str] = ["Muhammad Qasim", "Muhammad Junaid", "Zia Khan"]

# Dictionary with key-value pairs
data2: Dict[str, str] = {
    "Father Name": "Abdullah Sheikh",
    "Name": "Abubakr Sheikh",
    "Education": "College"
}
pprint.pprint(data2["Name"])  # Accessing value by key

# Dictionary with multiple data types
Key = Union[int, str]
Value = Union[int, str, list, dict, tuple, set]

data3: Dict[Key, Value] = {1: "Games", 2: "Music", 3: "Study"}
pprint.pprint(data3[1])  # Access value by key

# Get method - safe key access
print(data3.get(4, 'NA'))  # Returns 'NA' if key not found
print(data3.get(1))  # Returns value for key 1

# Adding and updating values in dictionary
data4: Dict[Key, Value] = {}  # Empty dictionary
data4[1] = "Sleeping"
data4[2] = "Coding"
data4[3] = "Eating"
pprint.pprint(data4)

data4[1] = "Gaming"  # Update key 1
pprint.pprint(data4)

# Print keys, values, and items
for d in data4.keys():
    print(d)

for v in data4.values():
    print(v)

for k, v in data4.items():
    print(k, v)

# Variable swap
a: int = 7
b: int = 10
a, b = b, a
print(a, b)  # Now a=10, b=7

# Auto add keys to dictionary
keys: list[str] = ['id', 'name', 'fname', 'course']
data5: dict[Key, Value] = {}
print(data5.fromkeys(keys))  # Create dict with default None values
