# 📘 Data Engineering Python - Day 3: Conditionals
## 🎯 Today I Learned About CONDITIONALS
1. Basic if Statement
```python
temperature = 25

if temperature > 30:
    print("It's hot outside!")
# Only executes if condition is True
```
2. if-else Statement
```python
score = 75

if score >= 50:
    print("You passed!")
else:
    print("You failed.")
```
3. if-elif-else Statement
```python
grade_score = 85

if grade_score >= 90:
    grade = "A"
elif grade_score >= 80:
    grade = "B"
elif grade_score >= 70:
    grade = "C"
elif grade_score >= 60:
    grade = "D"
else:
    grade = "F"
```
4. Nested Conditionals
```python
age = 22
has_id = True
has_ticket = True

if age >= 18:
    if has_id:
        if has_ticket:
            print("Welcome!")
        else:
            print("Need ticket")
    else:
        print("Need ID")
else:
    print("Must be 18+")
```
5. Ternary Operator (Conditional Expression)
```python
# Traditional way
if x > y:
    max_value = x
else:
    max_value = y

# Ternary operator
max_value = x if x > y else y

# Another example
number = 7
parity = "even" if number % 2 == 0 else "odd"
```
6. Multiple Conditions
```python
# AND operator
age = 25
has_license = True

if age >= 18 and has_license:
    print("Can drive")

# OR operator
day = "Saturday"
if day == "Saturday" or day == "Sunday":
    print("Weekend!")

# Complex conditions with parentheses
if (temperature > 20 and temperature < 30) and is_sunny:
    print("Great weather!")
```
7. Match-Case Statement (Python 3.10+)
```python
def describe_color(color):
    match color.lower():
        case "red":
            return "Color of passion"
        case "blue":
            return "Color of calm"
        case "green":
            return "Color of nature"
        case _:
            return "Beautiful color"
```
8. Chained Comparisons
```python
x = 15

# Traditional way
if x > 10 and x < 20:
    print("Between 10 and 20")

# Pythonic way
if 10 < x < 20:
    print("Between 10 and 20")

# Multiple comparisons
if 20 <= y <= 30:
    print("Between 20 and 30 inclusive")
```
9. Conditional Assignment Patterns
```python
# Default value if None
value = user_input if user_input is not None else "default"

# Using OR for defaults (careful with falsy values!)
display_name = name or "Anonymous"

# Conditional dictionary value
config = {
    "mode": "production" if not debug_mode else "development"
}
```
🛠 Practical Data Engineering Examples
1. Data Validation & Quality Checks
```python
def validate_record(record):
    """Validate a data record."""
    if not record:
        return False, "Empty record"
    
    # Check required fields
    required_fields = ["id", "timestamp", "value"]
    for field in required_fields:
        if field not in record:
            return False, f"Missing field: {field}"
    
    # Validate data types
    if not isinstance(record["id"], (int, str)):
        return False, "Invalid id type"
    
    # Validate value ranges
    if "price" in record and record["price"] <= 0:
        return False, "Price must be positive"
    
    # Check timestamp (not in future)
    if record["timestamp"] > datetime.now():
        return False, "Future timestamp"
    
    return True, "Valid record"

# Usage
record = {"id": 1, "timestamp": datetime.now(), "value": 100, "price": 50}
is_valid, message = validate_record(record)
```
2. ETL Pipeline Control Flow
```python
def run_etl_pipeline(data, config):
    """Control ETL pipeline execution."""
    
    # Check if pipeline should run
    if not config.get("enabled", True):
        print("Pipeline disabled")
        return None
    
    # Extract
    if not data:
        if config.get("skip_empty", False):
            print("No data to process")
            return []
        else:
            raise ValueError("No data provided")
    
    # Transformation rules based on config
    transformed_data = []
    for item in data:
        # Apply conditional transformations
        if config.get("clean_strings", False) and isinstance(item.get("name"), str):
            item["name"] = item["name"].strip().title()
        
        if config.get("filter_invalid", False) and item.get("value") is None:
            continue  # Skip invalid records
        
        # Data type conversion
        if config.get("convert_types", False):
            try:
                item["value"] = float(item["value"])
            except (ValueError, TypeError):
                if config.get("strict_mode", False):
                    raise
                else:
                    item["value"] = 0.0
        
        transformed_data.append(item)
    
    # Load based on conditions
    if config.get("write_to_db", False):
        if len(transformed_data) > 0:
            load_to_database(transformed_data)
        else:
            print("No data to load")
    
    return transformed_data
```
3. Error Handling & Recovery
```python
def process_data_chunk(chunk, retry_count=0):
    """Process data with error handling and retries."""
    
    max_retries = 3
    
    try:
        # Attempt processing
        result = complex_processing(chunk)
        
        # Validate result
        if not result or len(result) == 0:
            if config.get("allow_empty_results", False):
                return []
            else:
                raise ValueError("Empty result")
        
        return result
        
    except (ConnectionError, TimeoutError) as e:
        # Network errors - retry
        if retry_count < max_retries:
            print(f"Retrying... Attempt {retry_count + 1}")
            return process_data_chunk(chunk, retry_count + 1)
        else:
            if config.get("skip_on_failure", False):
                print("Skipping chunk after max retries")
                return []
            else:
                raise
    
    except ValueError as e:
        # Data errors - log and optionally skip
        if config.get("skip_invalid_data", True):
            print(f"Skipping invalid chunk: {e}")
            return []
        else:
            raise
    
    except Exception as e:
        # Unexpected errors
        if config.get("log_and_continue", False):
            log_error(e)
            return []
        else:
            raise
```
4. Feature Flag Management
```python
class FeatureFlags:
    def __init__(self):
        self.flags = {
            "new_algorithm": False,
            "enable_caching": True,
            "parallel_processing": True,
            "debug_logging": False
        }
    
    def process_data(self, data, use_new_algorithm=None):
        """Process data using feature flags."""
        
        # Determine which algorithm to use
        if use_new_algorithm is None:
            use_new_algorithm = self.flags["new_algorithm"]
        
        if use_new_algorithm:
            result = self._new_algorithm(data)
        else:
            result = self._legacy_algorithm(data)
        
        # Apply caching if enabled
        if self.flags["enable_caching"]:
            self.cache_result(data, result)
        
        # Log debug info if enabled
        if self.flags["debug_logging"]:
            self.log_debug_info(data, result)
        
        return result
```
5. Data Routing & Filtering
```python
def route_data(data, destination_rules):
    """Route data to different destinations based on rules."""
    
    destinations = {
        "database": [],
        "data_warehouse": [],
        "api_endpoint": [],
        "file_export": []
    }
    
    for record in data:
        # Apply routing rules
        if destination_rules.get("high_priority", False) and record.get("priority") == "high":
            destinations["api_endpoint"].append(record)
        
        elif record.get("type") == "transaction":
            destinations["database"].append(record)
        
        elif record.get("requires_analytics", False):
            destinations["data_warehouse"].append(record)
        
        # Archive old data
        elif record.get("timestamp") < datetime.now() - timedelta(days=365):
            destinations["file_export"].append(record)
        
        else:
            # Default routing
            destinations["database"].append(record)
    
    return destinations
```
6. Conditional Data Transformation
```python
def clean_and_transform(data, rules):
    """Apply conditional transformations to data."""
    
    cleaned_data = []
    
    for record in data:
        # Skip null records if configured
        if rules.get("skip_null_records", True) and record is None:
            continue
        
        # Apply field-specific rules
        transformed_record = {}
        
        for field, value in record.items():
            # Handle missing values
            if value is None:
                if rules.get("fill_missing", False):
                    if field in rules.get("default_values", {}):
                        value = rules["default_values"][field]
                    else:
                        value = rules.get("default_fill", "N/A")
                elif rules.get("drop_missing", False):
                    continue  # Skip this field
            
            # Type-specific cleaning
            if isinstance(value, str):
                if rules.get("trim_strings", True):
                    value = value.strip()
                if rules.get("lowercase_strings", False):
                    value = value.lower()
            
            elif isinstance(value, (int, float)):
                if rules.get("round_numbers", False):
                    decimals = rules.get("decimal_places", 2)
                    value = round(value, decimals)
                
                # Outlier handling
                if rules.get("handle_outliers", False):
                    min_val = rules.get("min_value", float('-inf'))
                    max_val = rules.get("max_value", float('inf'))
                    if value < min_val or value > max_val:
                        if rules.get("clip_outliers", True):
                            value = max(min_val, min(value, max_val))
                        else:
                            continue  # Skip this record
            
            transformed_record[field] = value
        
        # Only add record if it meets minimum criteria
        if len(transformed_record) >= rules.get("min_fields", 1):
            cleaned_data.append(transformed_record)
    
    return cleaned_data
