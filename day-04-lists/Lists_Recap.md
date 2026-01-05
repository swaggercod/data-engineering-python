#  📘Day 4: Lists Recap
## 📚 Today I Learned About LISTS
1. What is a List?
```python
# A collection of ordered, mutable (changeable) elements
my_list = [1, 2, 3, "hello", 4.5, True]
```
2. Indexing - Accessing Elements
```python
fruits = ["apple", "banana", "cherry", "date"]

# Positive indexing (0-based)
first_fruit = fruits[0]      # "apple"
third_fruit = fruits[2]      # "cherry"

# Negative indexing (from the end)
last_fruit = fruits[-1]      # "date"
second_last = fruits[-2]     # "cherry"
```
3. Slicing - Getting Parts of Lists
```python
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# Basic slicing [start:stop:step]
first_three = numbers[0:3]      # [0, 1, 2]
middle = numbers[3:7]           # [3, 4, 5, 6]
every_other = numbers[::2]      # [0, 2, 4, 6, 8]
reverse = numbers[::-1]         # [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]

# Omitting start/stop
first_five = numbers[:5]        # [0, 1, 2, 3, 4]
from_third = numbers[2:]        # [2, 3, 4, 5, 6, 7, 8, 9]
```
4. Mutating Lists - Changing Elements
```python
# Lists are MUTABLE - we can change them!

# Changing single element
colors = ["red", "green", "blue"]
colors[1] = "yellow"          # ["red", "yellow", "blue"]

# Changing multiple elements with slicing
numbers = [1, 2, 3, 4, 5]
numbers[1:4] = [20, 30, 40]   # [1, 20, 30, 40, 5]

# Adding elements
colors.append("purple")       # Adds to the end
colors.insert(1, "orange")    # Insert at specific position

# Removing elements
colors.pop()                  # Remove last element
colors.pop(0)                 # Remove first element
colors.remove("yellow")       # Remove specific value
del colors[1:3]              # Remove slice
```
5. Common List Methods
```python
my_list = [1, 2, 3]

# Length
len(my_list)                  # 3

# Adding elements
my_list.append(4)             # [1, 2, 3, 4]
my_list.extend([5, 6])        # [1, 2, 3, 4, 5, 6]

# Finding elements
index = my_list.index(3)      # 2
count = my_list.count(2)      # 1
exists = 3 in my_list         # True

# Sorting and reversing
numbers = [3, 1, 4, 2]
numbers.sort()                # [1, 2, 3, 4]
numbers.reverse()             # [4, 3, 2, 1]
sorted_list = sorted(numbers) # Returns new sorted list

# Copying lists (important!)
original = [1, 2, 3]
shallow_copy = original.copy()     # Creates new list
list_copy = original[:]            # Another way to copy
```
6. Data Engineering Applications
```python
# Processing data batches
batch_data = []
for i in range(1000):
    batch_data.append(process_data(i))
    if len(batch_data) >= 100:  # Process in batches of 100
        save_to_database(batch_data)
        batch_data = []  # Reset for next batch

# Transforming data
raw_logs = ["ERROR: Disk full", "INFO: Backup started", "WARNING: Memory low"]
error_logs = [log for log in raw_logs if "ERROR" in log]  # List comprehension

# Data windowing for streaming
stream_window = []
new_data = get_stream_data()
stream_window.append(new_data)
stream_window = stream_window[-100:]  # Keep only last 100 items
