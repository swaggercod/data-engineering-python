# 📘Day 5: Loops and List Comprehensions
## 📚Today I Learned About LOOPS & LIST COMPREHENSIONS
1. For Loops
Used to iterate over a sequence (list, tuple, string, range, etc.)

Example:

```python
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)
```
2. While Loops
Repeats as long as a condition is True

Example:

```python
count = 0
while count < 5:
    print(count)
    count += 1
```
3. List Comprehensions
A concise way to create lists

Syntax:
[expression for item in iterable if condition]

Example:

```python
squares = [x**2 for x in range(10)]
even_numbers = [x for x in range(20) if x % 2 == 0]
