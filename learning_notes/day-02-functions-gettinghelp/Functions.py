"""
Day 2: Functions and Getting Help
Kaggle Python Tutorial - Functions Section
"""

print("=== FUNCTIONS IN PYTHON ===\n")

# 1. BASIC FUNCTION DEFINITION
# ----------------------------
def greet():
    """Print a simple greeting message."""
    print("Hello, welcome to Python!")

# Calling the function
print("1. Basic Function:")
greet()

# 2. FUNCTIONS WITH PARAMETERS
# ----------------------------
def greet_person(name):
    """Greet a specific person."""
    print(f"Hello, {name}! Nice to meet you.")

print("\n2. Function with Parameters:")
greet_person("Alice")
greet_person("Bob")

# 3. FUNCTIONS WITH MULTIPLE PARAMETERS
# -------------------------------------
def introduce(name, age, city):
    """Introduce someone with multiple details."""
    print(f"My name is {name}, I'm {age} years old, and I live in {city}.")

print("\n3. Function with Multiple Parameters:")
introduce("Charlie", 25, "New York")

# 4. FUNCTIONS WITH DEFAULT PARAMETERS
# ------------------------------------
def greet_with_default(name="Guest"):
    """Greet with a default value."""
    print(f"Welcome, {name}!")

print("\n4. Function with Default Parameters:")
greet_with_default("David")
greet_with_default()  # Uses default

# 5. FUNCTIONS WITH RETURN VALUES
# -------------------------------
def add_numbers(a, b):
    """Return the sum of two numbers."""
    return a + b

def multiply_numbers(a, b):
    """Return the product of two numbers."""
    product = a * b
    return product

print("\n5. Functions with Return Values:")
result1 = add_numbers(5, 3)
result2 = multiply_numbers(4, 6)
print(f"5 + 3 = {result1}")
print(f"4 × 6 = {result2}")

# 6. RETURNING MULTIPLE VALUES
# ----------------------------
def get_min_max(numbers):
    """Return both minimum and maximum of a list."""
    if not numbers:
        return None, None
    return min(numbers), max(numbers)

print("\n6. Returning Multiple Values:")
nums = [3, 7, 2, 9, 1]
minimum, maximum = get_min_max(nums)
print(f"List: {nums}")
print(f"Minimum: {minimum}, Maximum: {maximum}")

# 7. FUNCTIONS WITH DOCSTRINGS
# ----------------------------
def calculate_area(length, width):
    """
    Calculate the area of a rectangle.
    
    Parameters:
    length (float): The length of the rectangle
    width (float): The width of the rectangle
    
    Returns:
    float: The area of the rectangle
    """
    area = length * width
    return area

print("\n7. Function with Docstring:")
area = calculate_area(5.5, 3.0)
print(f"Area of rectangle: {area}")

# 8. LAMBDA FUNCTIONS (ANONYMOUS)
# -------------------------------
# Lambda functions are small, anonymous functions
print("\n8. Lambda Functions:")

# Regular function
def square(x):
    return x ** 2

# Equivalent lambda function
square_lambda = lambda x: x ** 2

print(f"Square (regular): {square(5)}")
print(f"Square (lambda): {square_lambda(5)}")

# Using lambda directly
numbers = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x ** 2, numbers))
print(f"Squared numbers: {squared}")

# 9. HIGHER-ORDER FUNCTIONS
# -------------------------
def apply_operation(func, value):
    """Apply a function to a value."""
    return func(value)

def double(x):
    return x * 2

def triple(x):
    return x * 3

print("\n9. Higher-Order Functions:")
print(f"Apply double to 10: {apply_operation(double, 10)}")
print(f"Apply triple to 10: {apply_operation(triple, 10)}")

# 10. NESTED FUNCTIONS
# --------------------
def outer_function(text):
    """Example of nested functions."""
    message = text.upper()
    
    def inner_function():
        """Inner function that uses outer variable."""
        return f"Processed: {message}"
    
    return inner_function()

print("\n10. Nested Functions:")
print(outer_function("hello world"))

# 11. VARIABLE SCOPE
# ------------------
global_var = "I'm global"

def scope_demo():
    """Demonstrate variable scope."""
    local_var = "I'm local"
    print(f"Inside function: {local_var}")
    print(f"Global inside function: {global_var}")

print("\n11. Variable Scope:")
scope_demo()
print(f"Global outside function: {global_var}")
# print(local_var)  # This would cause an error!

# 12. *args AND **kwargs
# ----------------------
def sum_all(*args):
    """Sum all arguments (variable number)."""
    return sum(args)

def print_info(**kwargs):
    """Print all keyword arguments."""
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print("\n12. *args and **kwargs:")
print(f"Sum of 1,2,3,4,5: {sum_all(1, 2, 3, 4, 5)}")
print("Person info:")
print_info(name="Emma", age=30, city="London")
