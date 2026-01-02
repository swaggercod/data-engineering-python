"""
Day 3: Conditionals
Kaggle Python Tutorial - Conditionals Section
"""

print("=== CONDITIONALS IN PYTHON ===\n")

# 1. BASIC IF STATEMENT
# ---------------------
print("1. Basic if Statement:")
print("-" * 30)

temperature = 25
print(f"Temperature: {temperature}°C")

if temperature > 30:
    print("It's hot outside!")
print("This always prints (outside if block)")

# 2. IF-ELSE STATEMENT
# --------------------
print("\n2. if-else Statement:")
print("-" * 30)

score = 75
print(f"Score: {score}")

if score >= 50:
    print("You passed the exam!")
else:
    print("You failed the exam.")

# 3. IF-ELIF-ELSE STATEMENT
# -------------------------
print("\n3. if-elif-else Statement:")
print("-" * 30)

grade_score = 85
print(f"Grade score: {grade_score}")

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

print(f"Your grade is: {grade}")

# 4. NESTED CONDITIONALS
# ----------------------
print("\n4. Nested Conditionals:")
print("-" * 30)

age = 22
has_id = True
has_ticket = False

print(f"Age: {age}, Has ID: {has_id}, Has Ticket: {has_ticket}")

if age >= 18:
    if has_id:
        if has_ticket:
            print("Welcome to the concert!")
        else:
            print("You need a ticket to enter.")
    else:
        print("ID is required for entry.")
else:
    print("You must be 18 or older to enter.")

# 5. TERNARY OPERATOR
# -------------------
print("\n5. Ternary Operator (Conditional Expression):")
print("-" * 30)

x = 10
y = 20

# Traditional if-else
if x > y:
    max_value = x
else:
    max_value = y
print(f"Max (traditional): {max_value}")

# Ternary operator
max_value = x if x > y else y
print(f"Max (ternary): {max_value}")

# Another example
number = 7
parity = "even" if number % 2 == 0 else "odd"
print(f"{number} is {parity}")

# 6. MULTIPLE CONDITIONS
# ----------------------
print("\n6. Multiple Conditions:")
print("-" * 30)

# Using 'and'
age = 25
has_license = True
print(f"Age: {age}, Has license: {has_license}")

if age >= 18 and has_license:
    print("You can drive legally.")
else:
    print("You cannot drive.")

# Using 'or'
day = "Saturday"
print(f"Day: {day}")

if day == "Saturday" or day == "Sunday":
    print("It's the weekend!")
else:
    print("It's a weekday.")

# Complex conditions
temperature = 22
is_sunny = True
print(f"\nTemperature: {temperature}°C, Is sunny: {is_sunny}")

if (temperature > 20 and temperature < 30) and is_sunny:
    print("Perfect weather for a picnic!")
else:
    print("Maybe stay indoors today.")

# 7. MATCH-CASE STATEMENT (Python 3.10+)
# ---------------------------------------
print("\n7. Match-Case Statement (Python 3.10+):")
print("-" * 30)

def describe_color(color):
    """Match different colors."""
    match color.lower():
        case "red":
            return "The color of passion and energy."
        case "blue":
            return "The color of calm and trust."
        case "green":
            return "The color of nature and growth."
        case "yellow":
            return "The color of happiness and optimism."
        case _:
            return "A beautiful color!"

colors = ["red", "blue", "purple", "green"]
for color in colors:
    print(f"{color.capitalize()}: {describe_color(color)}")

# 8. PRACTICAL EXAMPLES
# ---------------------
print("\n8. Practical Conditional Examples:")
print("-" * 30)

# Example 1: Login System
def login_system(username, password):
    print(f"\nLogin attempt: username='{username}'")
    
    valid_users = {"admin": "admin123", "user1": "pass123"}
    
    if username in valid_users:
        if valid_users[username] == password:
            return "Login successful!"
        else:
            return "Incorrect password."
    else:
        return "Username not found."

# Test login system
print(login_system("admin", "admin123"))
print(login_system("admin", "wrongpass"))
print(login_system("unknown", "pass"))

# Example 2: Shopping Cart Discount
def calculate_total(amount, is_member, coupon_code=None):
    print(f"\nPurchase amount: ${amount}")
    print(f"Member: {is_member}")
    print(f"Coupon: {coupon_code}")
    
    discount = 0
    
    # Member discount
    if is_member:
        discount += 10  # 10% for members
    
    # Coupon discount
    if coupon_code == "SAVE20":
        discount += 20
    elif coupon_code == "SAVE10":
        discount += 10
    elif coupon_code:
        discount += 5  # Generic coupon
    
    # Apply discount (max 30%)
    discount = min(discount, 30)
    
    final_amount = amount * (100 - discount) / 100
    
    print(f"Discount: {discount}%")
    print(f"Final amount: ${final_amount:.2f}")
    return final_amount

calculate_total(100, True, "SAVE20")
calculate_total(50, False, None)
calculate_total(200, True, "HOLIDAY")

# 9. ERROR HANDLING WITH CONDITIONALS
# -----------------------------------
print("\n9. Error Handling with Conditionals:")
print("-" * 30)

def safe_divide(a, b):
    if b == 0:
        return "Error: Cannot divide by zero!"
    else:
        return a / b

print(f"10 / 2 = {safe_divide(10, 2)}")
print(f"10 / 0 = {safe_divide(10, 0)}")

# 10. CHAINED COMPARISONS
# -----------------------
print("\n10. Chained Comparisons:")
print("-" * 30)

x = 15
print(f"x = {x}")

# Traditional way
if x > 10 and x < 20:
    print("x is between 10 and 20")

# Pythonic way (chained comparison)
if 10 < x < 20:
    print("x is between 10 and 20 (chained)")

# Multiple chained comparisons
y = 25
print(f"\ny = {y}")
if 20 <= y <= 30:
    print("y is between 20 and 30 inclusive")

# 11. CONDITIONAL ASSIGNMENT PATTERNS
# -----------------------------------
print("\n11. Conditional Assignment Patterns:")
print("-" * 30)

# Pattern 1: Default value if None
user_input = None
value = user_input if user_input is not None else "default"
print(f"Input: {user_input}, Value: {value}")

# Pattern 2: Using or for defaults (careful with falsy values!)
name = ""
display_name = name or "Anonymous"
print(f"Name: '{name}', Display: '{display_name}'")

# Pattern 3: Conditional dictionary value
config = {
    "debug": True,
    "mode": "production" if not True else "development"
}
print(f"Config: {config}")

# 12. REAL-WORLD SCENARIO: TRAFFIC LIGHT SYSTEM
# ---------------------------------------------
print("\n12. Real-World Scenario: Traffic Light System")
print("-" * 40)

def traffic_light_action(light_color, is_emergency=False):
    """Determine action based on traffic light."""
    
    light_color = light_color.lower()
    
    if is_emergency:
        return "Proceed with caution - Emergency vehicle"
    
    match light_color:
        case "red":
            return "STOP"
        case "yellow":
            return "SLOW DOWN and prepare to stop"
        case "green":
            return "GO"
        case "flashing red":
            return "Treat as STOP sign"
        case "flashing yellow":
            return "Proceed with caution"
        case _:
            return "Invalid light color"

# Test traffic light
lights = ["red", "yellow", "green", "flashing red", "blue"]
for light in lights:
    print(f"{light.upper()}: {traffic_light_action(light)}")

print(f"\nRED with emergency: {traffic_light_action('red', True)}")
