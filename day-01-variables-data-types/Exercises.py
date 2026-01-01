Day 1: Variables & Data Types - Exercises & Solutions
Question 1: Basic Variables
Task: Create three variables:

name storing your name as a string

age storing your age as an integer

height storing your height in meters as a float
Print them in a sentence like: "My name is [name], I am [age] years old and [height] meters tall."

Answer:

python
name = "Alex"
age = 28
height = 1.75
print(f"My name is {name}, I am {age} years old and {height} meters tall.")
Question 2: Type Conversion Practice
Task: Convert the string "25.5" to a float, add 10.5 to it, then convert the result to an integer and string.

Answer:

python
# Convert string to float
num_float = float("25.5")  # 25.5

# Add 10.5
result = num_float + 10.5  # 36.0

# Convert to integer and string
result_int = int(result)    # 36
result_str = str(result)    # "36.0"

print(f"Float: {result}, Integer: {result_int}, String: '{result_str}'")
Question 3: Multiple Assignment
Task: Use one line to assign values 10, 20, and 30 to variables x, y, and z. Then swap the values of x and y.

Answer:

python
# Multiple assignment in one line
x, y, z = 10, 20, 30
print(f"Original: x={x}, y={y}, z={z}")

# Swap x and y
x, y = y, x
print(f"After swap: x={x}, y={y}, z={z}")
Question 4: Data Type Identification
Task: Given the list data = ["100", 200, 300.0, False], print the type of each element and convert all to integers.

Answer:

python
data = ["100", 200, 300.0, False]

print("Original types:")
for item in data:
    print(f"{item}: {type(item)}")

print("\nConverted to integers:")
for item in data:
    converted = int(item)
    print(f"{item} -> {converted} (type: {type(converted)})")
Question 5: Boolean Operations
Task: Create variables a = True, b = False, c = 10, d = 0. Perform and print:

a and b

a or b

not a

bool(c)

bool(d)

Answer:

python
a = True
b = False
c = 10
d = 0

print(f"a and b: {a and b}")    # False
print(f"a or b: {a or b}")      # True
print(f"not a: {not a}")        # False
print(f"bool(c): {bool(c)}")    # True (non-zero is truthy)
print(f"bool(d): {bool(d)}")    # False (zero is falsy)
Question 6: String to Number Operations
Task: Take two number strings "15" and "20", convert them to integers, perform addition and multiplication, then convert results back to strings.

Answer:

python
num1_str = "15"
num2_str = "20"

# Convert to integers
num1_int = int(num1_str)
num2_int = int(num2_str)

# Perform operations
addition = num1_int + num2_int      # 35
multiplication = num1_int * num2_int  # 300

# Convert back to strings
addition_str = str(addition)          # "35"
multiplication_str = str(multiplication)  # "300"

print(f"Addition: {addition} -> '{addition_str}'")
print(f"Multiplication: {multiplication} -> '{multiplication_str}'")
