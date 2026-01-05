# 📘 Day 3: Booleans & Conditionals
## 🎯 Today I Learned About BOOLEANS AND CONDITIONALS
1. Boolean Values - The Foundation
```python
# Two boolean values: True and False (capitalized!)
print(True)   # Output: True
print(False)  # Output: False
type(True)    # <class 'bool'>
```
2. Comparison Operators
```python
x = 10
y = 5

x > y      # True  - greater than
x < y      # False - less than
x >= 10    # True  - greater than or equal
y <= 5     # True  - less than or equal
x == 10    # True  - equal to
x != y     # True  - not equal to
```
3. Logical Operators
```python
# AND (both must be True)
True and True    # True
True and False   # False

# OR (at least one True)
True or False    # True
False or False   # False

# NOT (negation)
not True         # False
not False        # True
```
4. Truthy and Falsy Values
```python
# Falsy values (evaluate to False)
False, None, 0, 0.0, "", [], (), {}, set()

# Truthy values (evaluate to True)
True, 1, -1, 3.14, "hello", [1, 2], {"a": 1}

# Examples in conditionals
if "hello":        # Truthy - executes
    print("This runs")
    
if "":            # Falsy - doesn't execute
    print("This doesn't run")
```
5. Short-Circuit Evaluation
```python
# AND short-circuits on first False
def expensive_operation():
    print("Expensive operation!")
    return True

False and expensive_operation()  # expensive_operation() never called
True and expensive_operation()   # expensive_operation() gets called

# OR short-circuits on first True
True or expensive_operation()    # expensive_operation() never called
False or expensive_operation()   # expensive_operation() gets called
6. String Comparison
python
# Lexicographical (dictionary) order
"apple" == "apple"    # True
"apple" < "banana"    # True ('a' comes before 'b')
"apple" < "Apple"     # False (uppercase comes first in ASCII)
"10" < "2"           # True (strings compare character by character)
```
7. Identity Operators (is vs ==)
```python
list1 = [1, 2, 3]
list2 = [1, 2, 3]
list3 = list1

list1 == list2   # True (same values)
list1 is list2   # False (different objects in memory)
list1 is list3   # True (same object)

# Integer caching (-5 to 256)
a = 100
b = 100
a is b          # True (cached integers)

a = 1000
b = 1000
a is b          # False (not cached)
```
8. Membership Operators
```python
# Check if item is in collection
fruits = ["apple", "banana", "cherry"]
"apple" in fruits      # True
"orange" in fruits     # False
"orange" not in fruits # True

# With strings
"Hello" in "Hello, World!"    # True
"Python" in "Hello, World!"   # False

# With dictionaries (checks keys only)
person = {"name": "Alice", "age": 30}
"name" in person          # True (checks keys)
"Alice" in person        # False (doesn't check values)
"Alice" in person.values() # True (checks values)
```
9. Boolean Algebra & De Morgan's Laws
```python
# Chained comparisons
age = 25
13 <= age <= 19      # False (not a teenager)

# De Morgan's Laws
# not (A and B) == (not A) or (not B)
# not (A or B) == (not A) and (not B)

A = True
B = False
not (A and B) == (not A) or (not B)  # True
not (A or B) == (not A) and (not B)  # True
```
10. Practical Data Engineering Examples
```python
# 1. Data validation
def validate_data(record):
    has_required_fields = "id" in record and "timestamp" in record
    has_valid_types = isinstance(record.get("value"), (int, float))
    is_complete = record.get("status") != "partial"
    return has_required_fields and has_valid_types and is_complete

# 2. Log filtering
logs = ["ERROR: Disk full", "INFO: Backup started", "WARNING: Memory low"]
error_logs = [log for log in logs if log.startswith("ERROR")]

# 3. Data quality checks
def check_data_quality(df):
    has_no_nulls = df.isnull().sum().sum() == 0
    has_positive_values = (df["price"] > 0).all()
    has_valid_dates = (df["date"] <= pd.Timestamp.now()).all()
    return has_no_nulls and has_positive_values and has_valid_dates

# 4. Pipeline control flags
is_production = True
debug_mode = not is_production
should_log = debug_mode or is_production

# 5. Config-based feature toggles
features = {
    "enable_caching": True,
    "use_new_algorithm": False,
    "log_verbose": debug_mode
}

# Only cache in production with feature flag
if is_production and features["enable_caching"]:
    enable_cache()
```
11. Common Patterns
```python
# Default values with or operator
value = user_input or default_value

# Conditional assignment
status = "active" if user_count > 0 else "inactive"

# Guard clauses
if not data:
    return None
    
if not isinstance(data, list):
    raise TypeError("Expected list")

# Multiple condition checking
is_valid = (
    data is not None and
    len(data) > 0 and
    all(item is not None for item in data)
)
```
## 🔑 Key Takeaways for Data Engineering
Use == for value comparison, is for identity checks

Leverage short-circuiting for performance optimization

Truthy/Falsy values simplify conditional logic

Membership operators are fast for lookups in collections

Boolean logic is essential for data validation and filtering

## 🎯 Best Practices
```python
 ✅ DO
if not data:  # Checks for empty/None
    handle_empty_data()
    
 ✅ DO use explicit comparisons for clarity
if value is None:
    handle_none()
    
 ✅ DO use parentheses for complex expressions
if (condition1 or condition2) and condition3:
    do_something()

 ❌ DON'T compare boolean to True/False explicitly
if is_valid == True:  # Bad
if is_valid:          # Good
```
