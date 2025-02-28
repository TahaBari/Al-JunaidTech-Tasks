print("Task#01")
print("01:")

# Task 1: Declare variables and print personal information
name = "Taha Bari"
gender = "Male"
age = 23
address = "Flat# D-104, Iqra city phase1, Gulshan-e-Iqbal, block4a, Karachi"
degree = "Bachelor of Science in Software Engineering"
dob = "2001-10-17"
email = "taha.abdulbari8@gmail.com"

print("Personal Information:")
print(f"Name: {name}")
print(f"Gender: {gender}")
print(f"Age: {age}")
print(f"Address: {address}")
print(f"Degree: {degree}")
print(f"Date of Birth: {dob}")
print(f"Email: {email}")

print("\n" + "="*40 + "\n")

print("02:")
# Task 2: Type casting and swapping two variables
a = 5
b = 10
print("Before Swapping:")
print(f"a = {a}, b = {b}")

# Type casting while swapping
a, b = float(b), int(a)

print("After Swapping:")
print(f"a = {a}, b = {b}")

print("\n" + "="*40 + "\n")

print("03:")
# Task 3: Declare variables with different data types and display their types
var_int = 10
var_float = 10.5
var_string = "Hello, Python!"
var_bool = True
var_list = [1, 2, 3, 4, 5]
var_tuple = (10, 20, 30)
var_dict = {"name": "John", "age": 25}
var_set = {1, 2, 3, 4, 5}

print("Variables with Different Data Types:")
print(f"Integer: {var_int} (Type: {type(var_int)})")
print(f"Float: {var_float} (Type: {type(var_float)})")
print(f"String: {var_string} (Type: {type(var_string)})")
print(f"Boolean: {var_bool} (Type: {type(var_bool)})")
print(f"List: {var_list} (Type: {type(var_list)})")
print(f"Tuple: {var_tuple} (Type: {type(var_tuple)})")
print(f"Dictionary: {var_dict} (Type: {type(var_dict)})")
print(f"Set: {var_set} (Type: {type(var_set)})")

print("\n" + "="*40 + "\n")

print("Task#02")
print("01:")
# Task 1: Perform arithmetic operations on two variables
num1 = 15
num2 = 4

print("Arithmetic Operations:")
print(f"Addition: {num1} + {num2} = {num1 + num2}")
print(f"Subtraction: {num1} - {num2} = {num1 - num2}")
print(f"Multiplication: {num1} * {num2} = {num1 * num2}")
print(f"Division: {num1} / {num2} = {num1 / num2}")
print(f"Modulo: {num1} % {num2} = {num1 % num2}")

print("\n" + "="*40 + "\n")

print("02:")
# Task 2: Compare two numerical variables using comparison operators
print("Comparison Operations:")
print(f"{num1} == {num2} : {num1 == num2}")  # Equal to
print(f"{num1} != {num2} : {num1 != num2}")  # Not equal to
print(f"{num1} > {num2} : {num1 > num2}")    # Greater than
print(f"{num1} < {num2} : {num1 < num2}")    # Less than
print(f"{num1} >= {num2} : {num1 >= num2}")  # Greater than or equal to
print(f"{num1} <= {num2} : {num1 <= num2}")  # Less than or equal to

print("\n" + "="*40 + "\n")

print("03:")
# Task 3: Demonstrate assignment operators
x = 10
print("Assignment Operators:")
print(f"Initial x: {x}")
x += 5
print(f"x += 5 : {x}")
x -= 3
print(f"x -= 3 : {x}")
x *= 2
print(f"x *= 2 : {x}")
x /= 4
print(f"x /= 4 : {x}")
x %= 3
print(f"x %= 3 : {x}")

print("\n" + "="*40 + "\n")

print("04:")
# Task 4: Demonstrate logical operators
a = True
b = False

print("Logical Operations:")
print(f"a and b : {a and b}")  # Logical AND
print(f"a or b : {a or b}")    # Logical OR
print(f"not a : {not a}")      # Logical NOT
print(f"not b : {not b}")      # Logical NOT

# Logical conditions
numA = 10
numB = 20
print(f"(numA > 5 and numB < 30) : {numA > 5 and numB < 30}")
print(f"(numA < 5 or numB > 15) : {numA < 5 or numB > 15}")
print(f"not(numA == 10) : {not(numA == 10)}")
