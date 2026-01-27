# Pandas Complete Tutorial 🐼

A comprehensive guide to Pandas based on Bro Code's tutorial. Master data manipulation and analysis with Python's most powerful data library.

---

## Table of Contents
1. [Introduction](#introduction)
2. [Installation](#installation)
3. [Series](#series)
4. [DataFrames](#dataframes)
5. [Importing Data](#importing-data)
6. [Selection](#selection)
7. [Filtering](#filtering)
8. [Aggregation](#aggregation)
9. [Data Cleaning](#data-cleaning)

---

## Introduction

### What is Pandas?
**Pandas** is a Python library built on top of **NumPy**. It's widely used in:
- 📊 **Data Analysis**
- 🔬 **Data Science**
- 🤖 **Machine Learning**

The name "pandas" comes from the term **"Panel Data"** (an econometrics term). Unfortunately, it has nothing to do with pandas the animal! 🐼

### Key Concepts
With Pandas, you typically work with two main objects:
- **Series:** One-dimensional labeled column
- **DataFrame:** Two-dimensional labeled grid or table

Think of Pandas as **Python's version of Microsoft Excel, but on steroids**! 💪

---

## Installation

### Install Pandas
```bash
pip install pandas
```

### Alternative Installation (if multiple Python versions)
```bash
python -m pip install pandas
```

### Import Pandas
```python
import pandas as pd

# Check version
print(pd.__version__)  # Example: 2.3.2
```

---

## Series

A **Series** is a Pandas one-dimensional labeled array. Think of it like a **single column in a spreadsheet**.

**Analogy:** A single hallway with apartments. Each apartment holds data and has a label/number.

### Creating a Series

#### From a List
```python
import pandas as pd

# Create a list
data = [100, 102, 104]

# Convert to Series
series = pd.Series(data)
print(series)
# 0    100
# 1    102
# 2    104
# dtype: int64
```

### Data Types in Series
```python
# Floats
data = [100.1, 102.2, 104.3]
series = pd.Series(data)
# dtype: float64

# Strings
data = ['A', 'B', 'C']
series = pd.Series(data)
# dtype: object

# Booleans
data = [True, False, True]
series = pd.Series(data)
# dtype: bool
```

### Custom Index Labels
```python
# Default index (0, 1, 2)
data = [100, 102, 104]
series = pd.Series(data, index=['A', 'B', 'C'])
print(series)
# A    100
# B    102
# C    104
# dtype: int64

# Custom labels
series = pd.Series(data, index=['Apartment 1', 'Apartment 2', 'Apartment 3'])
```

### Accessing Values
```python
series = pd.Series([100, 102, 104], index=['A', 'B', 'C'])

# By label (loc)
print(series.loc['A'])  # 100
print(series.loc['B'])  # 102
print(series.loc['C'])  # 104

# By integer position (iloc)
print(series.iloc[0])   # 100
print(series.iloc[1])   # 102
print(series.iloc[2])   # 104
```

### Updating Values
```python
series = pd.Series([100, 102, 104], index=['A', 'B', 'C'])

# Update using loc
series.loc['C'] = 200
print(series)
# A    100
# B    102
# C    200
```

### Filtering by Value
```python
series = pd.Series([100, 102, 104, 200, 202], index=['A', 'B', 'C', 'D', 'E'])

# Filter values >= 200
print(series[series >= 200])
# D    200
# E    202

# Filter values < 200
print(series[series < 200])
# A    100
# B    102
# C    104
```

### 🏋️ Real-World Example: Calorie Tracker
```python
# Create a dictionary
calories = {
    'Day 1': 1750,
    'Day 2': 2100,
    'Day 3': 1700
}

# Convert to Series
series = pd.Series(calories)
print(series)
# Day 1    1750
# Day 2    2100
# Day 3    1700
# dtype: int64

# Access specific day
print(series.loc['Day 1'])  # 1750

# Update a value
series.loc['Day 3'] += 500  # Added a cookie!
print(series.loc['Day 3'])  # 2200

# Filter: Days over 2000 calories
print(series[series >= 2000])
# Day 2    2100
# Day 3    2200

# Filter: Days under 2000 calories
print(series[series < 2000])
# Day 1    1750
```

---

## DataFrames

A **DataFrame** is a tabular data structure with rows and columns. It's **two-dimensional**, similar to an Excel spreadsheet.

### Creating DataFrames

#### From a Dictionary
```python
# Dictionary of lists
data = {
    'Name': ['Spongebob', 'Patrick', 'Squidward'],
    'Age': [30, 35, 50]
}

df = pd.DataFrame(data)
print(df)
#        Name  Age
# 0  Spongebob   30
# 1    Patrick   35
# 2  Squidward   50
```

### Custom Index Labels
```python
data = {
    'Name': ['Spongebob', 'Patrick', 'Squidward'],
    'Age': [30, 35, 50],
    'City': ['Bikini Bottom', 'Bikini Bottom', 'Bikini Bottom']
}

df = pd.DataFrame(data, index=['Employee 1', 'Employee 2', 'Employee 3'])
print(df)
#                   Name  Age          City
# Employee 1   Spongebob   30  Bikini Bottom
# Employee 2     Patrick   35  Bikini Bottom
# Employee 3   Squidward   50  Bikini Bottom
```

### Selecting Rows
```python
# By label (loc)
print(df.loc['Employee 1'])
# Name    Spongebob
# Age            30
# City    Bikini Bottom

# By position (iloc)
print(df.iloc[0])  # First row
print(df.iloc[1])  # Second row
print(df.iloc[2])  # Third row
```

### Adding a New Column
```python
# Add 'Job' column
df['Job'] = ['Cook', 'NA', 'Cashier']
print(df)
#                   Name  Age          City      Job
# Employee 1   Spongebob   30  Bikini Bottom     Cook
# Employee 2     Patrick   35  Bikini Bottom       NA
# Employee 3   Squidward   50  Bikini Bottom  Cashier
```

### Adding New Rows
```python
# Create a new DataFrame with one row
new_row = pd.DataFrame([{
    'Name': 'Sandy',
    'Age': 28,
    'Job': 'Engineer'
}], index=['Employee 4'])

# Concatenate with existing DataFrame
df = pd.concat([df, new_row])
print(df)
#                   Name  Age          City      Job
# Employee 1   Spongebob   30  Bikini Bottom     Cook
# Employee 2     Patrick   35  Bikini Bottom       NA
# Employee 3   Squidward   50  Bikini Bottom  Cashier
# Employee 4       Sandy   28           NaN  Engineer
```

### Adding Multiple Rows
```python
# Add multiple rows
new_rows = pd.DataFrame([
    {'Name': 'Sandy', 'Age': 28, 'Job': 'Engineer'},
    {'Name': 'Eugene', 'Age': 60, 'Job': 'Manager'}
], index=['Employee 4', 'Employee 5'])

df = pd.concat([df, new_rows])
print(df)
```

---

## Importing Data

### Reading CSV Files
```python
# Basic CSV reading
df = pd.read_csv('data.csv')

# Display first and last 5 rows
print(df)

# Display all rows
print(df.to_string())
```

### Example: Pokemon Dataset
```python
# Read Pokemon CSV
df = pd.read_csv('data.csv')

print(df)
# Output shows Pokemon from Bulbasaur (#1) to Mewtwo (#150)
# Columns: Number, Name, Type1, Type2, Height, Weight, Legendary
```

**Sample Data:**
```
Number,Name,Type1,Type2,Height,Weight,Legendary
1,Bulbasaur,Grass,Poison,0.7,6.9,0
2,Ivysaur,Grass,Poison,1.0,13.0,0
3,Venusaur,Grass,Poison,2.0,100.0,0
4,Charmander,Fire,,0.6,8.5,0
5,Charmeleon,Fire,,1.1,19.0,0
...
150,Mewtwo,Psychic,,2.0,122.0,1
```

### Reading JSON Files
```python
# Read JSON file
df = pd.read_json('data.json')

print(df)
# Same Pokemon data in JSON format
```

---

## Selection

### Selection by Column
```python
df = pd.read_csv('data.csv')

# Select single column (returns Series)
print(df['Name'])
# 0      Bulbasaur
# 1        Ivysaur
# 2       Venusaur
# ...

# Select single column (returns DataFrame)
print(df[['Name']])

# Select multiple columns
print(df[['Name', 'Height', 'Weight']])

# Display all rows
print(df[['Name', 'Height', 'Weight']].to_string())
```

### Selection by Row
```python
# Set custom index
df = pd.read_csv('data.csv', index_col='Name')

# Select by label (loc)
print(df.loc['Pikachu'])
# Number           25
# Type1      Electric
# Type2           NaN
# Height          0.4
# Weight            6
# Legendary         0

# Search for Charizard
print(df.loc['Charizard'])
# Number           6
# Type1         Fire
# Type2       Flying
# Height         1.7
# Weight        90.5
# Legendary        0

# Select specific columns
print(df.loc['Charizard', ['Height', 'Weight']])
# Height     1.7
# Weight    90.5
```

### Range of Rows
```python
# Select range (Charizard to Blastoise)
print(df.loc['Charizard':'Blastoise'])
#           Number Type1  Type2  Height  Weight  Legendary
# Charizard      6  Fire Flying     1.7    90.5          0
# Squirtle       7 Water    NaN     0.5     9.0          0
# Wartortle      8 Water    NaN     1.0    22.5          0
# Blastoise      9 Water    NaN     1.6    85.5          0
```

### Selection by Integer Position (iloc)
```python
# First 10 rows
print(df.iloc[0:11])

# Every second row (first 10)
print(df.iloc[0:11:2])

# First 10 rows, first 3 columns
print(df.iloc[0:11, 0:3])
```

### 🏋️ Interactive Search Exercise
```python
try:
    pokemon = input('Enter a Pokemon name: ')
    print(df.loc[pokemon])
except KeyError:
    print(f"{pokemon} not found.")

# Example:
# Enter a Pokemon name: Pikachu
# Number           25
# Type1      Electric
# ...

# Enter a Pokemon name: Snorlax
# Number          143
# Type1        Normal
# ...

# Enter a Pokemon name: Digimon
# Digimon not found.
```

---

## Filtering

**Filtering** = keeping rows that match a condition when working with DataFrames.

### Basic Filtering
```python
df = pd.read_csv('data.csv')

# Filter: Pokemon with height >= 2 meters
tall_pokemon = df[df['Height'] >= 2]
print(tall_pokemon)

# Filter: Pokemon with weight > 100 kg
heavy_pokemon = df[df['Weight'] > 100]
print(heavy_pokemon)

# Filter: Legendary Pokemon
legendary_pokemon = df[df['Legendary'] == 1]
# or
legendary_pokemon = df[df['Legendary'] == True]
print(legendary_pokemon)
# Articuno, Zapdos, Moltres, Mewtwo
```

### Multiple Conditions
```python
# OR condition (|)
# Water type in Type1 OR Type2
water_pokemon = df[(df['Type1'] == 'Water') | (df['Type2'] == 'Water')]
print(water_pokemon)

# AND condition (&)
# Fire type AND Flying type
fire_flying = df[(df['Type1'] == 'Fire') & (df['Type2'] == 'Flying')]
print(fire_flying)
# Charizard, Moltres
```

**Important:** Use `&` for AND, `|` for OR (C-style operators, not Python's `and`/`or`)

---

## Aggregation

**Aggregate functions** reduce a set of values into a single summary value. They're used to summarize and analyze data.

### Aggregate Functions on Entire DataFrame
```python
df = pd.read_csv('data.csv')

# Mean (average) of all numeric columns
print(df.mean(numeric_only=True))
# Number      75.5
# Height       1.2
# Weight      46.2
# Legendary   0.026

# Sum of all numeric columns
print(df.sum(numeric_only=True))

# Minimum values
print(df.min(numeric_only=True))
# Number        1
# Height      0.2
# Weight      0.1
# Legendary     0

# Maximum values
print(df.max(numeric_only=True))
# Number      150
# Height      8.8
# Weight      460
# Legendary     1

# Count (includes all columns)
print(df.count())
# Number       150
# Name         150
# Type1        150
# Type2         67  (not all Pokemon have Type2)
# Height       150
# Weight       150
# Legendary    150
```

### Aggregate Functions on Single Column
```python
# Mean height
print(df['Height'].mean())  # 1.2

# Sum of all heights
print(df['Height'].sum())   # 180

# Minimum height
print(df['Height'].min())   # 0.2

# Maximum height
print(df['Height'].max())   # 8.8

# Count non-null values
print(df['Height'].count()) # 150
print(df['Type2'].count())  # 67 (many Pokemon lack Type2)
```

### GroupBy Operations
```python
# Group by Type1 and calculate mean height
grouped = df.groupby('Type1')
print(grouped['Height'].mean())
# Type1
# Bug         0.9
# Dragon      2.6
# Electric    1.1
# Fire        1.3
# ...

# Sum of heights by type
print(grouped['Height'].sum())
# Type1
# Bug        10.8
# Dragon      8.0
# Electric   10.2
# ...

# Minimum height by type
print(grouped['Height'].min())

# Maximum height by type
print(grouped['Height'].max())

# Count Pokemon by type
print(grouped['Height'].count())
# Type1
# Bug         12
# Dragon       3
# Electric     9
# Fire         12
# ...
# Water       32
```

---

## Data Cleaning

**Data cleaning** is the process of fixing or removing incomplete, incorrect, or irrelevant data.

**Important:** Approximately **75%** of work in Pandas is data cleaning! 🧹

### 1. Drop Irrelevant Columns
```python
# Drop single column
df = df.drop(columns=['Legendary'])

# Drop multiple columns
df = df.drop(columns=['Number', 'Legendary'])
print(df)
```

### 2. Handle Missing Data

#### Drop Rows with Missing Values
```python
# Drop rows where Type2 is missing
df = df.dropna(subset=['Type2'])
print(df.to_string())
# Only Pokemon with Type2 remain
# Bulbasaur (Grass/Poison), Charizard (Fire/Flying), etc.
```

#### Fill Missing Values
```python
# Replace NaN values with 'None'
df = df.fillna({'Type2': 'None'})
print(df.to_string())
# Pokemon without Type2 now show 'None'
```

### 3. Fix Inconsistent Values
```python
# Replace values in Type1 column
df['Type1'] = df['Type1'].replace({
    'Grass': 'GRASS',
    'Fire': 'FIRE',
    'Water': 'WATER'
})
print(df)
# Type1 now shows GRASS, FIRE, WATER in uppercase
```

### 4. Standardize Text
```python
# Convert all names to lowercase
df['Name'] = df['Name'].str.lower()
print(df)
# bulbasaur, ivysaur, venusaur, charmander, etc.
```

### 5. Fix Data Types
```python
# Convert Legendary column to boolean
df['Legendary'] = df['Legendary'].astype(bool)
print(df)
# 0 becomes False, 1 becomes True
```

### 6. Remove Duplicates
```python
# Suppose we have duplicate entries in CSV:
# 1,Bulbasaur,Grass,Poison,0.7,6.9,0
# 1,Bulbasaur,Grass,Poison,0.7,6.9,0  (duplicate)
# 1,Bulbasaur,Grass,Poison,0.7,6.9,0  (duplicate)

# Remove duplicates
df = df.drop_duplicates()
print(df)
# Only one Bulbasaur remains
```

---

## Common Pandas Patterns

### Read → Clean → Analyze Pattern
```python
# Read data
df = pd.read_csv('pokemon.csv')

# Clean data
df = df.dropna(subset=['Type2'])
df = df.drop(columns=['Number'])
df['Legendary'] = df['Legendary'].astype(bool)

# Analyze
mean_height_by_type = df.groupby('Type1')['Height'].mean()
print(mean_height_by_type)
```

---

## Quick Reference

### Essential DataFrame Methods

| Method | Description |
|--------|-------------|
| `df.head()` | First 5 rows |
| `df.tail()` | Last 5 rows |
| `df.info()` | DataFrame info |
| `df.describe()` | Statistical summary |
| `df.shape` | (rows, columns) |
| `df.columns` | Column names |
| `df.dtypes` | Data types |
| `df.to_string()` | Display all rows |

### Selection Methods

| Method | Description |
|--------|-------------|
| `df['col']` | Select column (Series) |
| `df[['col1', 'col2']]` | Select columns (DataFrame) |
| `df.loc[label]` | Select by label |
| `df.iloc[position]` | Select by position |
| `df.loc[row, col]` | Specific cell |

### Filtering
```python
# Single condition
df[df['Age'] > 30]

# Multiple conditions (AND)
df[(df['Age'] > 30) & (df['City'] == 'NYC')]

# Multiple conditions (OR)
df[(df['Age'] < 20) | (df['Age'] > 60)]
```

### Aggregate Functions
```python
df.mean()          # Average
df.sum()           # Sum
df.min()           # Minimum
df.max()           # Maximum
df.count()         # Count
df.std()           # Standard deviation
df.var()           # Variance
df.groupby('col')  # Group by column
```

### Data Cleaning
```python
df.drop(columns=['col'])       # Drop column
df.dropna()                    # Drop missing values
df.fillna(value)               # Fill missing values
df.replace(old, new)           # Replace values
df.drop_duplicates()           # Remove duplicates
df['col'].str.lower()          # Lowercase text
df['col'].astype(type)         # Change data type
```

---

## Practice Exercises

### Exercise 1: Pokemon Analysis
```python
# 1. Load Pokemon data
df = pd.read_csv('pokemon.csv')

# 2. Find all Fire type Pokemon
fire_pokemon = df[df['Type1'] == 'Fire']

# 3. Calculate average height by type
avg_height = df.groupby('Type1')['Height'].mean()

# 4. Find heaviest Pokemon
heaviest = df[df['Weight'] == df['Weight'].max()]

# 5. Count legendary Pokemon
legendary_count = df[df['Legendary'] == 1].count()
```

### Exercise 2: Data Cleaning
```python
# 1. Remove Pokemon without Type2
df_clean = df.dropna(subset=['Type2'])

# 2. Fill missing weights with average
df['Weight'] = df['Weight'].fillna(df['Weight'].mean())

# 3. Convert names to uppercase
df['Name'] = df['Name'].str.upper()

# 4. Remove duplicates
df = df.drop_duplicates()
```

---

## Additional Resources

- 📚 [Pandas Official Documentation](https://pandas.pydata.org/docs/)
- 📖 [10 Minutes to Pandas](https://pandas.pydata.org/docs/user_guide/10min.html)
- 🎓 [Pandas Cheat Sheet](https://pandas.pydata.org/Pandas_Cheat_Sheet.pdf)
- 🎥 [Bro Code YouTube Channel](https://www.youtube.com/@BroCodez)
- 🎮 [Pokemon Dataset](https://www.kaggle.com/datasets/abcsds/pokemon)

---

## Summary

### Key Takeaways

1. **Series** = One-dimensional labeled array (single column)
2. **DataFrame** = Two-dimensional labeled table (rows + columns)
3. **Selection** = Extract specific rows/columns using `.loc[]` and `.iloc[]`
4. **Filtering** = Keep rows matching conditions using boolean indexing
5. **Aggregation** = Summarize data with functions like `.mean()`, `.sum()`, `.groupby()`
6. **Data Cleaning** = Fix/remove bad data (75% of Pandas work!)

### The Pandas Workflow
```python
# 1. Import
import pandas as pd

# 2. Load data
df = pd.read_csv('data.csv')

# 3. Explore
print(df.head())
print(df.info())

# 4. Clean
df = df.dropna()
df = df.drop_duplicates()

# 5. Analyze
results = df.groupby('category')['value'].mean()

# 6. Export
df.to_csv('cleaned_data.csv', index=False)
```

---

**Happy Data Analysis! 📊🐼**

---

*Created based on Bro Code's Pandas Tutorial*
*Pokemon dataset used for educational purposes*
