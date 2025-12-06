

"""
 RULES (Must Follow - Otherwise Error):
   
 1. ✓ Can contain: letters (a-z, A-Z), digits (0-9), underscore (_)
   ✓ Must start with: letter or underscore
   ✓ Cannot start with: digit/number
   ✓ Cannot contain: spaces or special characters (@, #, $, %, etc.)
   ✓ Cannot use: Python keywords (reserved words)



2. Valid Examples:
   name, age, first_name, _value, student1, total_marks
   
3. Invalid Examples:
   2name          → Starts with number ✗
   first-name     → Contains hyphen ✗
   first name     → Contains space ✗
   @username      → Contains special character ✗
   for            → Python keyword ✗

4. Case Sensitivity:
   - Python treats these as DIFFERENT variables:
     name, Name, NAME, nAme
   - Be consistent with capitalization

5. Python Keywords (Cannot use as variable names):
   and, as, assert, break, class, continue, def, del, elif, else,
   except, False, finally, for, from, global, if, import, in, is,
   lambda, None, nonlocal, not, or, pass, raise, return, True, try,
   while, with, yield

6. BEST PRACTICES (Conventions):
   
   ✓ Use descriptive names: age (good), a (bad)
   ✓ Use lowercase: name (good), NAME (avoid for variables)
   ✓ Use underscore for multiple words: first_name (good), firstname (okay)
   ✓ Don't use single letters except for: i, j, k (in loops)
   
   Naming Convention: snake_case
   Examples: student_name, total_marks, user_age

7. Examples of Good vs Bad names:
   
   Good Names          Bad Names
   ---------           ---------
   student_age         sa
   total_price         tp
   first_name          x
   is_valid            v
   user_count          count1
""" 
#storing string in variables  
name = "aasim"
print(name)

#storing numbers in variables
num = 23
print(num)
 
print("my name is",name)
print("my age is",num)

#case sensitivity
name = "aasim"
NAME = "aasim"

#BOTH ARE DIFFERENT VARIABLES
print(name)
print(NAME)

#assigning same value to different variables
a=10
b=10
c=10

a=b=c=10
print(a)
print(b)
print(c)

#multiple values to multiple variables
a,b,c = 1,4,5
print(a)
print(b)
print(c)


#assigning different data type values to multiple variables
name,age,email = "aasim",18,"a@gmail.com"
print(name)
print(age)
print(email)


#swaping variables
a = "aasim"
b = "pratik"
print(a)
print(b)

#after swapping
temp = a
a = b
b = temp
print(a)
print(b)

#swapping without a new variable 
a,b=b,a 
print(a)
print(b)
