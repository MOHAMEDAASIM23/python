a = 5
b = 4
c = 2
print(a,b,c)

#to find the data type of the value
print(type(a))
print(type(b))
print(type(c))

#basic operations with int

#addition
print(a+b)

#subtraction
print(a-b)

#multiplication
print(b*c)

#division
print(b/c)
print(b//c) #floor division- cut off the decimal part

#remaider
print(a%b)

#power
print(a**3)

#comparison operator
print(a>b)
print(a==b)
print(c>b)
print(c>=b)
print(c!=b)
print(a<=b)


# INT (INTEGER) DATA TYPE IN PYTHON

# int means: whole number without decimal point

a = 10
b = -20
c = 0

print(a, b, c)

# To check the data type 
print(type(a))   # <class 'int'>
print(type(b))   # <class 'int'>
print(type(c))   # <class 'int'>


# ----- BASIC ARITHMETIC OPERATIONS WITH int ----- #

a = 10
b = 3

# Addition
print(a + b)   # 13

# Subtraction
print(a - b)   # 7

# Multiplication
print(a * b)   # 30

# Division – / vs //
print(a / b)   # 3.3333333333 (normal division, result is float)
print(a // b)  # 3            (floor division, result is int)

# / → normal division (can give decimal)
# // → “cut off” the decimal part (floor division)


# Remainder (Modulo)
print(a % b)   # 1

# % gives remainder after division.
# Example: 10 / 3 is 3 with remainder 1 → % gives 1.


# Power (Exponent)
print(a ** b)  # 10 ** 3 = 1000

# a ** b means “a to the power b”.


# ----- COMPARISON OPERATORS WITH int ----- #

# Comparison always returns True or False (bool).

x = 10
y = 20

print(x == y)   # False
print(x != y)   # True
print(x > y)    # False
print(x < y)    # True
print(x >= 10)  # True
print(y <= 20)  # True


# ----- TYPE CONVERSION (CASTING) WITH int ----- #

# float -> int (cuts off decimal part)
f1 = 3.9
f2 = 5.1

print(int(f1))   # 3  (not 4, decimal part is removed)
print(int(f2))   # 5

# string -> int (string must be a whole number)
s1 = "10"
s2 = "250"

print(int(s1))   # 10
print(int(s2))   # 250

# Invalid conversions (will give error if you try)
# int("10.5")    # ValueError (string has decimal)
# int("abc")     # ValueError


# ----- BUILT-IN FUNCTIONS AND USEFUL THINGS WITH int ----- #

# type() - to check the data type
num = 42
print(type(num))    # <class 'int'>

# int() - to convert other types to int
print(int(7.8))       # 7   (float -> int, decimal removed)
print(int("15"))      # 15  (string -> int, valid number string)

# You can also use int() in simple programs like taking user input (later):
# age = int(input("Enter your age: "))


# ----- int IN REAL EXAMPLES ----- #

# Example 1: Age after 5 years
age = 17
age_after_5_years = age + 5
print("Age after 5 years:", age_after_5_years)   # 22

# Example 2: Area of a rectangle (length * width)
length = 5
width = 3
area = length * width
print("Area of rectangle:", area)   # 15