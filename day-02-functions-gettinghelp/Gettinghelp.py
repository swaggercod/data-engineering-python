"""
Day 2: Getting Help in Python
Kaggle Python Tutorial - Getting Help Section
"""

print("=== GETTING HELP IN PYTHON ===\n")

# 1. USING help() FUNCTION
# ------------------------
print("1. Using help() function:")
print("-" * 30)

# Get help on built-in functions
print("Help on print function:")
# Uncomment to see: help(print)

# Get help on modules
print("\nHelp on math module:")
# Uncomment to see: help('math')

# 2. USING dir() FUNCTION
# -----------------------
print("\n2. Using dir() function:")
print("-" * 30)

# See all attributes of an object
my_list = [1, 2, 3]
print("Methods available for lists:")
list_methods = [method for method in dir(my_list) if not method.startswith('_')]
print(list_methods[:10])  # First 10 non-private methods

# 3. DOCSTRINGS
# -------------
print("\n3. Docstrings:")
print("-" * 30)

def example_function():
    """
    This is a docstring.
    It explains what the function does.
    
    Example:
    >>> example_function()
    'This function returns a greeting'
    """
    return "This function returns a greeting"

# Access docstring
print("Function docstring:")
print(example_function.__doc__)

# 4. TYPE() AND ISINSTANCE()
# --------------------------
print("\n4. Type Checking:")
print("-" * 30)

value = 42
print(f"Type of {value}: {type(value)}")
print(f"Is {value} an integer? {isinstance(value, int)}")
print(f"Is {value} a string? {isinstance(value, str)}")

# 5. COMMON BUILT-IN FUNCTIONS FOR HELP
# -------------------------------------
print("\n5. Common Built-in Help Functions:")
print("-" * 30)

# len() - get length
my_string = "Python"
print(f"Length of '{my_string}': {len(my_string)}")

# id() - get memory address
x = 10
print(f"Memory address of x: {id(x)}")

# hasattr() - check if object has attribute
print(f"Does list have 'append' method? {hasattr([], 'append')}")
print(f"Does list have 'fly' method? {hasattr([], 'fly')}")

# 6. USING ? IN IPYTHON/JUPYTER
# -----------------------------
print("\n6. IPython/Jupyter Help Features:")
print("-" * 30)
print("""In IPython or Jupyter, you can use:
- `function?` - Show docstring
- `function??` - Show source code
- `object.` + Tab - Auto-completion
- `object._` + Tab - Show private methods""")

# 7. READING ERROR MESSAGES
# -------------------------
print("\n7. Understanding Error Messages:")
print("-" * 30)

print("Example error and how to read it:")
try:
    result = 10 / 0
except ZeroDivisionError as e:
    print(f"Error type: {type(e).__name__}")
    print(f"Error message: {e}")
    print("\nThe traceback shows:")
    print("1. File and line where error occurred")
    print("2. Function call chain")
    print("3. Error type and message")

# 8. ONLINE RESOURCES
# -------------------
print("\n8. Useful Online Resources:")
print("-" * 30)
resources = {
    "Official Python Docs": "https://docs.python.org/3/",
    "Stack Overflow": "https://stackoverflow.com/",
    "Python Weekly": "https://www.pythonweekly.com/",
    "Real Python": "https://realpython.com/",
    "Python Discord": "https://discord.gg/python",
}

for name, url in resources.items():
    print(f"{name}: {url}")

# 9. PRACTICAL EXAMPLES
# ---------------------
print("\n9. Practical Help Examples:")
print("-" * 30)

# Example 1: Exploring a string
text = "Hello Python"
print(f"\nExploring string: '{text}'")
print(f"Available methods: {[m for m in dir(text) if 'upper' in m]}")

# Example 2: Understanding a module
import math
print(f"\nMath module constants: pi={math.pi}, e={math.e}")
print(f"Math functions containing 'log': {[f for f in dir(math) if 'log' in f]}")

# 10. CUSTOM HELP SYSTEM
# ----------------------
print("\n10. Creating Custom Help:")
print("-" * 30)

def my_calculator():
    """A simple calculator with help."""
    
    def show_help():
        print("\nCalculator Help:")
        print("add(x, y) - Add two numbers")
        print("subtract(x, y) - Subtract y from x")
        print("Type 'help' for this message")
        print("Type 'quit' to exit")
    
    def add(a, b):
        return a + b
    
    def subtract(a, b):
        return a - b
    
    print("Welcome to Calculator (type 'help' for assistance)")
    
    while True:
        command = input("\nEnter command: ").strip().lower()
        
        if command == 'quit':
            print("Goodbye!")
            break
        elif command == 'help':
            show_help()
        elif command == 'add':
            try:
                x = float(input("Enter first number: "))
                y = float(input("Enter second number: "))
                print(f"Result: {add(x, y)}")
            except ValueError:
                print("Please enter valid numbers!")
        elif command == 'subtract':
            try:
                x = float(input("Enter first number: "))
                y = float(input("Enter second number: "))
                print(f"Result: {subtract(x, y)}")
            except ValueError:
                print("Please enter valid numbers!")
        else:
            print(f"Unknown command: {command}")
            print("Type 'help' for available commands")

# Uncomment to run the calculator
# my_calculator()
