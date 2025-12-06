#checking what string contains
word = "python123"

#checking if all are alphabets
is_alpha = word.isalpha()
print("is alphabetic:",is_alpha)
print("aasim".isalpha())


#checking if all the characters are numeric
is_digit = word.isdigit()
print("is digit",is_digit)
print("123".isdigit())



# Check if all characters are alphanumeric (letters+numbers, no special characters, no spaces,  only letters, only numbers)
# returns True if all characters are either letters or numbers
# returns False if there are any special characters
# returns False if the string is empty  - for all built-in functions
is_alnum = word.isalnum()
print("Is alphanumeric:", is_alnum)  # True
word4 = "Python3"
print("Is alphanumeric:", word4.isalnum())  # True
print("Python@3".isalnum())  

#checks if all the characters are lowercase
words = "python"
is_lower = words.islower()
print("isolwer",is_lower)


#checks if all the characters are uppercase
words = "PYTHON"
is_upper = words.isupper()
print("isupper",is_upper)
print("Python".isupper())

#checking if the string contains only whitespaces
white_space = "   "
is_space = white_space.isspace()
print("is whitespace",is_space)
white_space2 = "22 "
is_space = white_space2.isspace()
print("is whitespace",is_space)
white_space3 = "  \t\n "            #tabs and newlines are also whitespaces
is_space = white_space3.isspace()
print("is whitespace",is_space)