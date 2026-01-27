# NumPy Complete Tutorial 🐍

A comprehensive guide to NumPy based on Bro Code's tutorial. This markdown file covers everything from basics to advanced topics.

---

## Table of Contents
1. [Introduction](#introduction)
2. [Installation](#installation)
3. [Basic Arrays](#basic-arrays)
4. [Multi-dimensional Arrays](#multi-dimensional-arrays)
5. [Slicing](#slicing)
6. [Arithmetic Operations](#arithmetic-operations)
7. [Broadcasting](#broadcasting)
8. [Aggregate Functions](#aggregate-functions)
9. [Filtering](#filtering)
10. [Random Numbers](#random-numbers)

---

## Introduction

### What is NumPy?
**NumPy** (Numerical Python) is a Python library used for numerical computing. It's widely used in:
- 📊 Data Science
- 🔧 Engineering
- 🤖 Artificial Intelligence
- 🧠 Machine Learning

### Why NumPy?
Python is slow, but NumPy is **fast** because:
- ⚡ Written in **C** under the hood
- 🚀 **Magnitudes faster** than regular Python
- 💪 Provides **vectorized operations**

**Example comparison:**
```python
# Python list
my_list = [1, 2, 3, 4]
my_list * 2  # [1, 2, 3, 4, 1, 2, 3, 4] - duplicates!

# NumPy array
array = np.array([1, 2, 3, 4])
array * 2  # [2, 4, 6, 8] - multiplies each element!
```

---

## Installation

### Install NumPy
```bash
pip install numpy
```

### Import NumPy
```python
import numpy as np

# Check version
print(np.__version__)  # Example: 2.3.1
```

---

## Basic Arrays

### Creating Arrays
```python
# Python list
my_list = [1, 2, 3, 4]

# NumPy array
array = np.array([1, 2, 3, 4])
print(array)  # [1 2 3 4]

# Check type
print(type(array))  # <class 'numpy.ndarray'>
```

### Array Operations
```python
array = np.array([1, 2, 3, 4])

# Multiply all elements by 2
array = array * 2
print(array)  # [2 4 6 8]
```

---

## Multi-dimensional Arrays

### Dimensions Overview
| Dimension | Description | Example |
|-----------|-------------|---------|
| **0D** | Single point | `np.array('A')` |
| **1D** | Single row | `np.array(['A', 'B', 'C'])` |
| **2D** | Matrix (rows × columns) | `np.array([['A', 'B'], ['C', 'D']])` |
| **3D** | Layers of matrices | Multiple 2D arrays stacked |

### Creating Multi-dimensional Arrays

#### 0D Array (Scalar)
```python
array = np.array('A')
print(array.ndim)  # 0
```

#### 1D Array (Vector)
```python
array = np.array(['A', 'B', 'C'])
print(array.ndim)  # 1
```

#### 2D Array (Matrix)
```python
array = np.array([
    ['A', 'B', 'C'],
    ['D', 'E', 'F'],
    ['G', 'H', 'I']
])
print(array.ndim)  # 2
print(array.shape)  # (3, 3) - 3 rows, 3 columns
```

#### 3D Array (Tensor)
```python
array = np.array([
    [['A', 'B', 'C'],
     ['D', 'E', 'F'],
     ['G', 'H', 'I']],
    
    [['J', 'K', 'L'],
     ['M', 'N', 'O'],
     ['P', 'Q', 'R']],
    
    [['S', 'T', 'U'],
     ['V', 'W', 'X'],
     ['Y', 'Z', '_']]
])

print(array.ndim)   # 3
print(array.shape)  # (3, 3, 3) - 3 layers, 3 rows, 3 columns
```

**⚠️ Important:** All nested lists must have the **same number of elements**!

### Accessing Elements

#### Chain Indexing (Old Way)
```python
array[0][0][0]  # 'A'
```

#### Multi-dimensional Indexing (Better Way)
```python
array[0, 0, 0]  # 'A' - Faster!
array[0, 0, 1]  # 'B'
array[1, 1, 1]  # 'N'
array[2, 0, 0]  # 'S'
```

**Format:** `array[layer, row, column]`

### 🏋️ Exercise: Spell a Word
```python
array = np.array([
    [['A', 'B', 'C'],
     ['D', 'E', 'F'],
     ['G', 'H', 'I']],
    
    [['J', 'K', 'L'],
     ['M', 'N', 'O'],
     ['P', 'Q', 'R']],
    
    [['S', 'T', 'U'],
     ['V', 'W', 'X'],
     ['Y', 'Z', '_']]
])

# Spell "ASS"
word = array[0,0,0] + array[2,0,0] + array[2,0,0]
print(word)  # "ASS"
```

---

## Slicing

### Basic Slicing Syntax
```python
array[start:end:step]
```
- **start:** Starting index (inclusive)
- **end:** Ending index (exclusive)
- **step:** Skip elements

### Creating Test Array
```python
array = np.array([
    [1,  2,  3,  4],
    [5,  6,  7,  8],
    [9,  10, 11, 12],
    [13, 14, 15, 16]
])
```

### Row Selection
```python
# Single row
array[0]     # [1 2 3 4]
array[1]     # [5 6 7 8]
array[-1]    # [13 14 15 16] - Last row
array[-2]    # [9 10 11 12]  - Second to last

# Range of rows
array[0:3]   # First 3 rows (indices 0, 1, 2)
array[1:4]   # Rows 1, 2, 3
array[1:]    # From row 1 to end

# Step in rows
array[0:4:2] # Every 2nd row (rows 0, 2)
array[::2]   # Every 2nd row (all rows)
array[::-1]  # All rows reversed
array[::-2]  # Every 2nd row reversed
```

### Column Selection
```python
# Single column
array[:, 0]   # [1 5 9 13]  - First column
array[:, 1]   # [2 6 10 14] - Second column
array[:, -1]  # [4 8 12 16] - Last column
array[:, -2]  # [3 7 11 15] - Second to last

# Range of columns
array[:, 0:3]  # First 3 columns
array[:, 1:4]  # Columns 1, 2, 3
array[:, 1:]   # From column 1 to end

# Step in columns
array[:, 0:4:2]  # Every 2nd column
array[:, ::2]    # Every 2nd column (all)
array[:, ::-1]   # All columns reversed
array[:, ::-2]   # Every 2nd column reversed
```

### Combined Row and Column Slicing
```python
# First 2 rows, first 2 columns (top-left quadrant)
array[0:2, 0:2]  # [[1 2], [5 6]]

# First 2 rows, last 2 columns (top-right quadrant)
array[0:2, 2:]   # [[3 4], [7 8]]

# Last 2 rows, first 2 columns (bottom-left quadrant)
array[2:, 0:2]   # [[9 10], [13 14]]

# Last 2 rows, last 2 columns (bottom-right quadrant)
array[2:, 2:]    # [[11 12], [15 16]]
```

---

## Arithmetic Operations

### Scalar Arithmetic
Apply a single value to all elements in an array.
```python
array = np.array([1, 2, 3])

# Addition
array + 1      # [2 3 4]

# Subtraction
array - 2      # [-1 0 1]

# Multiplication
array * 3      # [3 6 9]

# Division
array / 4      # [0.25 0.5 0.75]

# Power
array ** 5     # [1 32 243]
```

### Vectorized Math Functions
Apply functions to entire arrays without loops.
```python
array = np.array([1, 2, 3])

# Square root
np.sqrt(array)  # [1. 1.41421356 1.73205081]

# Rounding
array = np.array([1.01, 2.5, 3.99])
np.round(array)  # [1. 2. 4.]
np.floor(array)  # [1. 2. 3.]
np.ceil(array)   # [2. 3. 4.]

# Constants
np.pi  # 3.141592653589793
```

### 🏋️ Exercise: Calculate Circle Areas
```python
radii = np.array([1, 2, 3])
areas = np.pi * radii ** 2
print(areas)  # [3.14159265 12.56637061 28.27433388]
```

### Element-wise Arithmetic
Operations between two arrays, element by element.
```python
array1 = np.array([1, 2, 3])
array2 = np.array([4, 5, 6])

# Addition
array1 + array2  # [5 7 9]

# Subtraction
array1 - array2  # [-3 -3 -3]

# Multiplication
array1 * array2  # [4 10 18]

# Division
array1 / array2  # [0.25 0.4 0.5]

# Power
array1 ** array2  # [1 32 729]
```

### Comparison Operators
Create boolean arrays.
```python
scores = np.array([91, 55, 100, 73, 82, 64])

# Check conditions
scores == 100   # [False False True False False False]
scores >= 60    # [True False True True True True]
scores < 60     # [False True False False False False]

# Conditional assignment
scores[scores < 60] = 0
print(scores)  # [91 0 100 73 82 64]
```

---

## Broadcasting

Broadcasting allows NumPy to perform operations on arrays with **different shapes**.

### Broadcasting Rules
Two arrays are compatible when:
1. **Dimensions are equal**, OR
2. **One dimension is 1**

Dimensions are checked **right to left**.

### Broadcasting Examples
```python
# Array 1: shape (1, 4)
array1 = np.array([[1, 2, 3, 4]])

# Array 2: shape (4, 1)
array2 = np.array([[1],
                   [2],
                   [3],
                   [4]])

print(array1.shape)  # (1, 4)
print(array2.shape)  # (4, 1)

# Multiply (broadcasts to 4x4)
result = array1 * array2
print(result.shape)  # (4, 4)
```

**Result:**
```
[[1  2  3  4]
 [2  4  6  8]
 [3  6  9 12]
 [4  8 12 16]]
```

### ⚠️ Broadcasting Incompatibility
```python
# Array 1: shape (2, 4)
array1 = np.array([[1, 2, 3, 4],
                   [5, 6, 7, 8]])

# Array 2: shape (4, 1)
array2 = np.array([[1],
                   [2],
                   [3],
                   [4]])

# ERROR: ValueError - shapes (2, 4) and (4, 1) not compatible
# Rows: 2 vs 4 - not equal and neither is 1
```

### 🏋️ Exercise: Multiplication Table
```python
# Array 1: shape (1, 10)
array1 = np.array([[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]])

# Array 2: shape (10, 1)
array2 = np.array([[1],
                   [2],
                   [3],
                   [4],
                   [5],
                   [6],
                   [7],
                   [8],
                   [9],
                   [10]])

# Create multiplication table
table = array1 * array2
print(table)
print(table.shape)  # (10, 10)
```

---

## Aggregate Functions

Aggregate functions **summarize data** and typically return a **single value**.

### Basic Aggregate Functions
```python
array = np.array([
    [1, 2, 3, 4, 5],
    [6, 7, 8, 9, 10]
])

# Sum of all elements
np.sum(array)     # 55

# Mean (average)
np.mean(array)    # 5.5

# Standard deviation
np.std(array)     # 2.87...

# Variance
np.var(array)     # 8.25

# Minimum value
np.min(array)     # 1

# Maximum value
np.max(array)     # 10

# Index of minimum
np.argmin(array)  # 0

# Index of maximum
np.argmax(array)  # 9
```

### Axis-based Operations
```python
array = np.array([
    [1, 2, 3, 4, 5],
    [6, 7, 8, 9, 10]
])

# Sum along axis 0 (columns)
np.sum(array, axis=0)  # [7 9 11 13 15]

# Sum along axis 1 (rows)
np.sum(array, axis=1)  # [15 40]
```

**Remember:**
- `axis=0` → operations along **columns** (vertical)
- `axis=1` → operations along **rows** (horizontal)

---

## Filtering

Filtering = selecting elements that **match a condition**.

### Basic Filtering (Boolean Indexing)
```python
ages = np.array([
    [21, 17, 19, 20, 16, 30, 18, 65],
    [39, 22, 15, 99, 18, 19, 20, 21]
])

# Find teenagers (under 18)
teenagers = ages[ages < 18]
print(teenagers)  # [17 16 15]
```

**⚠️ Note:** Boolean indexing **flattens** the array (becomes 1D).

### Multiple Conditions
```python
# Adults (18-64)
adults = ages[(ages >= 18) & (ages < 65)]
print(adults)  # [21 19 20 30 18 39 22 18 19 20 21]

# Under 18 OR 65+
non_adults = ages[(ages < 18) | (ages >= 65)]
print(non_adults)  # [17 16 65 15 99]
```

**Logical Operators:**
- `&` → AND
- `|` → OR

**⚠️ Must use parentheses!**

### More Filtering Examples
```python
# Seniors (65+)
seniors = ages[ages >= 65]
print(seniors)  # [65 99]

# Even ages
evens = ages[ages % 2 == 0]
print(evens)  # [20 16 30 18 22 18 20]

# Odd ages
odds = ages[ages % 2 != 0]
print(odds)  # [21 17 19 65 39 15 99 19 21]
```

### Preserve Shape with `np.where()`
```python
# Filter with np.where (preserves shape)
adults = np.where(ages >= 18, ages, 0)
print(adults)
# [[21  0 19 20  0 30 18 65]
#  [39 22  0 99 18 19 20 21]]
```

**Syntax:** `np.where(condition, array, fill_value)`
- Elements matching condition → keep original value
- Elements not matching → replace with fill_value

**⚠️ Note:** `np.where()` is **slower** but preserves shape.

---

## Random Numbers

### Random Number Generator Setup
```python
# Create random number generator
rng = np.random.default_rng()

# With seed (reproducible results)
rng = np.random.default_rng(seed=1)
```

### Random Integers
```python
# Single random integer (1-6)
rng.integers(low=1, high=7)  # e.g., 3

# Multiple random integers
rng.integers(low=1, high=7, size=3)  # [2 5 1]

# 2D array of random integers
rng.integers(low=1, high=101, size=(3, 2))
# [[48 73]
#  [87 15]
#  [92 34]]
```

### Random Floats
```python
# Single float (0-1)
rng.uniform()  # e.g., 0.5488135...

# Float in range (-1 to 1)
rng.uniform(low=-1, high=1)  # e.g., -0.2341

# Multiple floats
rng.uniform(low=-1, high=1, size=3)
# [-0.67 0.84 0.12]

# 2D array of floats
rng.uniform(low=-1, high=1, size=(3, 2))
# [[-0.23  0.56]
#  [ 0.89 -0.45]
#  [ 0.12  0.78]]
```

### Shuffle Array
```python
array = np.array([1, 2, 3, 4, 5])

rng.shuffle(array)
print(array)  # [3 1 5 2 4] (random order)
```

### Random Choice
```python
fruits = np.array(['apple', 'orange', 'banana', 'coconut', 'pineapple'])

# Pick one random fruit
fruit = rng.choice(fruits)
print(fruit)  # 'banana'

# Pick multiple random fruits
fruits_picked = rng.choice(fruits, size=3)
print(fruits_picked)  # ['apple' 'coconut' 'apple']

# Pick in 2D array
fruits_grid = rng.choice(fruits, size=(3, 3))
# [['banana' 'apple' 'orange']
#  ['coconut' 'banana' 'apple']
#  ['pineapple' 'orange' 'banana']]
```

### 🏋️ Fun Exercise: Random Emoji Grid
```python
emojis = np.array(['🍎', '🍊', '🍌', '🥥', '🍍'])
rng = np.random.default_rng()

emoji_grid = rng.choice(emojis, size=(3, 3))
print(emoji_grid)
# [['🍎' '🍍' '🍌']
#  ['🥥' '🍊' '🍎']
#  ['🍍' '🍌' '🍊']]
```

---

## Summary

### Key Takeaways

| Topic | Key Points |
|-------|------------|
| **Arrays** | Faster than lists, vectorized operations |
| **Dimensions** | 0D (scalar), 1D (vector), 2D (matrix), 3D (tensor) |
| **Slicing** | `[start:end:step]`, works on rows and columns |
| **Arithmetic** | Scalar, vectorized, element-wise operations |
| **Broadcasting** | Operations on different shapes |
| **Aggregates** | sum, mean, min, max, std, var |
| **Filtering** | Boolean indexing, `np.where()` |
| **Random** | integers, floats, shuffle, choice |

### Common NumPy Functions
```python
# Creation
np.array([1, 2, 3])
np.zeros((3, 3))
np.ones((2, 2))
np.arange(0, 10, 2)
np.linspace(0, 1, 5)

# Math
np.sqrt(), np.exp(), np.log()
np.sin(), np.cos(), np.tan()
np.round(), np.floor(), np.ceil()

# Statistics
np.mean(), np.median(), np.std()
np.min(), np.max(), np.sum()
np.argmin(), np.argmax()

# Random
rng.integers(), rng.uniform()
rng.shuffle(), rng.choice()
```

---

## Additional Resources

- 📚 [NumPy Official Documentation](https://numpy.org/doc/)
- 🎓 [NumPy Tutorial](https://numpy.org/doc/stable/user/quickstart.html)
- 🎥 [Bro Code YouTube Channel](https://www.youtube.com/@BroCodez)

---

**Happy Coding! 🚀**

---

*Created based on Bro Code's NumPy Tutorial*
