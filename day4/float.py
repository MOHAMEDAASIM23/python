a = 3.2
b = 8.2

print(a)
print(b)

print(type(a))
print(typr(b))
# FLOAT DATA TYPE IN PYTHON

# Float means: number with decimal point

x = 3.14
y = -2.5
z = 0.0

print(x, y, z)

# To check the data type
print(type(x))   # <class 'float'>
print(type(y))   # <class 'float'>
print(type(z))   # <class 'float'>


# Basic arithmetic operations with float

a = 5.5
b = 2.0

# Addition
print(a + b)   # 7.5

# Subtraction
print(a - b)   # 3.5

# Multiplication
print(a * b)   # 11.0

# Division
print(a / b)   # 2.75 (normal division, result is float)

# Floor division //
print(a // b)  # 2.0 (cuts off decimal part, result is still float)

# Remainder (Modulo)
print(a % b)   # 1.5

# Power (Exponent)
print(a ** b)  # 5.5 ** 2.0 = 30.25


# Mixing int and float

p = 10      # int
q = 3.5     # float

print(p + q)   # 13.5 (float)
print(p * q)   # 35.0 (float)
print(p / q)   # 2.857142857142857 (float)


# Comparison operators with float

m = 10.5
n = 20.0

print(m == n)    # False
print(m != n)    # True
print(m > n)     # False
print(m < n)     # True
print(m >= 10.5) # True
print(n <= 20.0) # True


# Type conversion (casting) with float

# int -> float
num_int = 5
num_float = float(num_int)
print(num_int, type(num_int))       # 5 <class 'int'>
print(num_float, type(num_float))   # 5.0 <class 'float'>

# string -> float
s1 = "3.5"
s2 = "10"
print(float(s1))    # 3.5
print(float(s2))    # 10.0

# Invalid conversions (will give error if you try)
# float("abc")     # ValueError
# float("10a")     # ValueError


# ----- BUILT-IN FUNCTIONS AND USEFUL THINGS WITH FLOAT ----- #

# type() - to check the data type
val = 4.75
print(type(val))    # <class 'float'>

# float() - to convert other types to float
print(float(7))         # 7.0 (int -> float)
print(float("2.25"))    # 2.25 (string -> float)

# round() - to round float values

pi = 3.14159265

print(round(pi))       # 3      (rounded to nearest integer)
print(round(pi, 2))    # 3.14   (2 decimal places)
print(round(pi, 3))    # 3.142  (3 decimal places)

# Example: floating-point precision issue
print(0.1 + 0.2)         # 0.30000000000000004 (small precision error)
print(round(0.1 + 0.2, 2))  # 0.3 (use round to clean it)
