"""
Day 1: Variables and Data Types
Kaggle Python Tutorial - Variables Section
"""

# 1. VARIABLES
# ------------
# Variables are containers for storing data values
name = "Ahmet"
age = 25
height = 1.75
is_student = True

print("=== VARIABLES ===")
print(f"Name: {name}")
print(f"Age: {age}")
print(f"Height: {height}m")
print(f"Is student: {is_student}")

# Variable reassignment
age = 26
print(f"\nAfter birthday: {age}")

# Multiple assignment
x, y, z = 10, 20, 30
print(f"\nMultiple variables: x={x}, y={y}, z={z}")

# 2. DATA TYPES
# -------------
print("\n=== DATA TYPES ===")

# String
text = "Hello Python"
print(f"String: {text} (type: {type(text)})")

# Integer
number = 42
print(f"Integer: {number} (type: {type(number)})")

# Float
pi = 3.14159
print(f"Float: {pi} (type: {type(pi)})")

# Boolean
is_true = True
print(f"Boolean: {is_true} (type: {type(is_true)})")

# List
my_list = [1, 2, 3, "Python"]
print(f"List: {my_list} (type: {type(my_list)})")

# Dictionary
person = {"name": "Ali", "age": 30}
print(f"Dictionary: {person} (type: {type(person)})")

# Tuple
coordinates = (10.5, 20.3)
print(f"Tuple: {coordinates} (type: {type(coordinates)})")

# Set
unique_numbers = {1, 2, 3, 3, 2}
print(f"Set: {unique_numbers} (type: {type(unique_numbers)})")

# 3. TYPE CONVERSION
# ------------------
print("\n=== TYPE CONVERSION ===")

# String to integer
num_str = "123"
num_int = int(num_str)
print(f"String '123' to integer: {num_int}")

# Integer to string
int_to_str = str(456)
print(f"Integer 456 to string: '{int_to_str}'")

# Float to integer
float_num = 9.99
int_num = int(float_num)  # Truncates decimal part
print(f"Float 9.99 to integer: {int_num}")

# Check types
print(f"\nType checking:")
print(f"Is 'text' a string? {isinstance(text, str)}")
print(f"Is 'number' an integer? {isinstance(number, int)}")
