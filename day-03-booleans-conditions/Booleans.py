"""
Day 3: Booleans and Conditionals
Kaggle Python Tutorial - Booleans Section
"""

print("=== BOOLEANS IN PYTHON ===\n")

# 1. BOOLEAN VALUES
# -----------------
print("1. Boolean Values:")
print(f"True: {True}")
print(f"False: {False}")
print(f"Type of True: {type(True)}")
print(f"Type of False: {type(False)}")

# 2. BOOLEAN OPERATORS
# --------------------
print("\n2. Boolean Operators:")

# Comparison Operators
a = 10
b = 5
print(f"\nComparison Operators (a={a}, b={b}):")
print(f"a > b: {a > b}")      # Greater than
print(f"a < b: {a < b}")      # Less than
print(f"a >= 10: {a >= 10}")  # Greater than or equal
print(f"b <= 5: {b <= 5}")    # Less than or equal
print(f"a == 10: {a == 10}")  # Equal to
print(f"a != b: {a != b}")    # Not equal to

# 3. LOGICAL OPERATORS
# --------------------
print("\n3. Logical Operators:")

x = True
y = False

print(f"\nx = {x}, y = {y}")
print(f"x and y: {x and y}")    # AND - Both must be True
print(f"x or y: {x or y}")      # OR - At least one True
print(f"not x: {not x}")        # NOT - Negation
print(f"not y: {not y}")

# 4. TRUTHY AND FALSY VALUES
# --------------------------
print("\n4. Truthy and Falsy Values:")

# Falsy values in Python
falsy_values = [False, None, 0, 0.0, "", [], (), {}, set()]

print("Falsy values (evaluate to False):")
for value in falsy_values:
    print(f"  bool({repr(value)}) = {bool(value)}")

print("\nTruthy values (evaluate to True):")
truthy_values = [True, 1, 3.14, "hello", [1, 2], {"key": "value"}]
for value in truthy_values:
    print(f"  bool({repr(value)}) = {bool(value)}")

# 5. SHORT-CIRCUIT EVALUATION
# ---------------------------
print("\n5. Short-Circuit Evaluation:")

def return_true():
    print("  return_true() called")
    return True

def return_false():
    print("  return_false() called")
    return False

print("\nAND operator (short-circuits on False):")
result = return_false() and return_true()  # Only first function called
print(f"Result: {result}")

print("\nOR operator (short-circuits on True):")
result = return_true() or return_false()  # Only first function called
print(f"Result: {result}")

# 6. COMPARISON WITH DIFFERENT TYPES
# ----------------------------------
print("\n6. Comparison with Different Types:")

print("String comparison:")
print(f"'apple' == 'apple': {'apple' == 'apple'}")
print(f"'apple' == 'banana': {'apple' == 'banana'}")
print(f"'a' < 'b': {'a' < 'b'}")  # Lexicographical order
print(f"'apple' < 'banana': {'apple' < 'banana'}")

print("\nType-sensitive comparison:")
print(f"5 == '5': {5 == '5'}")  # Different types are not equal
print(f"5 == 5.0: {5 == 5.0}")  # But int and float can be equal

# 7. IDENTITY OPERATORS
# ---------------------
print("\n7. Identity Operators (is, is not):")

list1 = [1, 2, 3]
list2 = [1, 2, 3]
list3 = list1  # Same reference

print(f"list1 = {list1}")
print(f"list2 = {list2}")
print(f"list3 = list1")

print(f"\nlist1 == list2: {list1 == list2}")   # Same values
print(f"list1 is list2: {list1 is list2}")     # Different objects
print(f"list1 is list3: {list1 is list3}")     # Same object

# For small integers (Python caches -5 to 256)
a = 100
b = 100
print(f"\na = 100, b = 100")
print(f"a == b: {a == b}")
print(f"a is b: {a is b}")  # True due to integer caching

a = 1000
b = 1000
print(f"\na = 1000, b = 1000")
print(f"a == b: {a == b}")
print(f"a is b: {a is b}")  # False (not in cache range)

# 8. MEMBERSHIP OPERATORS
# -----------------------
print("\n8. Membership Operators (in, not in):")

fruits = ["apple", "banana", "cherry"]
print(f"fruits = {fruits}")

print(f"'apple' in fruits: {'apple' in fruits}")
print(f"'orange' in fruits: {'orange' in fruits}")
print(f"'orange' not in fruits: {'orange' not in fruits}")

# With strings
text = "Hello, World!"
print(f"\ntext = '{text}'")
print(f"'Hello' in text: {'Hello' in text}")
print(f"'Python' in text: {'Python' in text}")

# With dictionaries (checks keys)
person = {"name": "Alice", "age": 30}
print(f"\nperson = {person}")
print(f"'name' in person: {'name' in person}")
print(f"'Alice' in person: {'Alice' in person}")  # False, checks keys not values
print(f"'Alice' in person.values(): {'Alice' in person.values()}")  # True

# 9. BOOLEAN ALGEBRA EXAMPLES
# ---------------------------
print("\n9. Boolean Algebra Examples:")

age = 25
has_license = True
has_car = False

print(f"age = {age}, has_license = {has_license}, has_car = {has_car}")

# Complex boolean expressions
can_drive = age >= 18 and has_license
print(f"Can drive: {can_drive}")

can_rent_car = age >= 21 and has_license and not has_car
print(f"Can rent car: {can_rent_car}")

is_teenager = 13 <= age <= 19
print(f"Is teenager: {is_teenager}")

# De Morgan's Laws
print("\nDe Morgan's Laws:")
print(f"not (A and B) == (not A) or (not B)")
print(f"not (A or B) == (not A) and (not B)")

A = True
B = False
print(f"\nFor A={A}, B={B}:")
print(f"not (A and B): {not (A and B)}")
print(f"(not A) or (not B): {(not A) or (not B)}")
print(f"Are they equal? {not (A and B) == ((not A) or (not B))}")

# 10. PRACTICAL EXAMPLES
# ----------------------
print("\n10. Practical Boolean Examples:")

# Email validation example
email = "user@example.com"
print(f"\nEmail validation for: {email}")
is_valid_format = "@" in email and "." in email
print(f"Valid format: {is_valid_format}")

# Password strength checker
password = "SecurePass123"
print(f"\nPassword strength for: {password}")
has_upper = any(c.isupper() for c in password)
has_lower = any(c.islower() for c in password)
has_digit = any(c.isdigit() for c in password)
is_strong = len(password) >= 8 and has_upper and has_lower and has_digit

print(f"Length >= 8: {len(password) >= 8}")
print(f"Has uppercase: {has_upper}")
print(f"Has lowercase: {has_lower}")
print(f"Has digit: {has_digit}")
print(f"Is strong password: {is_strong}")

# Age category checker
ages = [15, 25, 35, 65, 75]
print("\nAge categories:")
for age in ages:
    is_child = age < 18
    is_adult = 18 <= age < 65
    is_senior = age >= 65
    
    if is_child:
        category = "Child"
    elif is_adult:
        category = "Adult"
    else:
        category = "Senior"
    
    print(f"  {age} years: {category}")
