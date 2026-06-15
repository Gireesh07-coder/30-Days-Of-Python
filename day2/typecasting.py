# ==========================================
# Day 2 - 30 Days of Python Challenge
# Author: Gireesh S Bhajantri
# ==========================================

# Exercise 1: Check the data type of different values

print("Data Types")
print(type(5))
print(type(5.45))
print(type("Gireesh"))
print(type([12, 23, 4, 5]))
print(type({34, 45, 6}))
print(type((34, 23, 21, 2)))
print(type({"name": "Gireesh", "age": 22, "city": "Hirekerur"}))

print("-" * 40)

# Exercise 2: Length of first name

first_name = "Gireesh"
last_name = "Bhajantri"

print("Length of first name:", len(first_name))
print("Length of last name:", len(last_name))

if len(first_name) > len(last_name):
    print("First name is longer than last name.")
elif len(first_name) < len(last_name):
    print("Last name is longer than first name.")
else:
    print("Both names have the same length.")

print("-" * 40)

# Exercise 3: Arithmetic Operations

num_one = 5
num_two = 4

total = num_one + num_two
difference = num_one - num_two
product = num_one * num_two
division = num_one / num_two
remainder = num_one % num_two
exponent = num_one ** num_two
floor_division = num_one // num_two

print("Addition:", total)
print("Subtraction:", difference)
print("Multiplication:", product)
print("Division:", division)
print("Remainder:", remainder)
print("Exponent:", exponent)
print("Floor Division:", floor_division)

print("-" * 40)

# Exercise 4: Circle Calculations

radius = 30
pi = 3.14

area_of_circle = pi * radius * radius
circumference_of_circle = 2 * pi * radius

print("Area of Circle:", area_of_circle)
print("Circumference of Circle:", circumference_of_circle)

print("-" * 40)

# Exercise 5: User Input for Radius

radius = float(input("Enter the radius: "))
area = pi * radius * radius

print("Area of Circle:", area)

print("-" * 40)

# Exercise 6: User Details

first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")
country = input("Enter your country: ")
age = int(input("Enter your age: "))

print("\n----- User Details -----")
print("First Name :", first_name)
print("Last Name  :", last_name)
print("Country    :", country)
print("Age         :", age)

print("-" * 40)

# Exercise 7: Python Keywords

help("keywords")