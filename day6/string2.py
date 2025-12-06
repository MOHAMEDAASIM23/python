sample_str = "hello WORLD"

#converting to uppercase
upper_str = sample_str.upper()
print("uppercase",upper_str)

#converting to lowercase
lower_str = sample_str.lower()
print("lowercase",lower_str)

#capitalizing first character
title_str = sample_str.title()
print("title case",title_str)

#string capitalizing
capitalize_str = sample_str.capitalize()
print("capitalized",capitalize_str)

#removing whitrespace character
whitespace_str = "  hello world  "

#removing leading and trailing whitespace
stripped_str = whitespace_str.strip()
print("stripped string",stripped_str)

# Removing leading whitespace
leading_str = whitespace_str.lstrip()
print("Leading Whitespace Removed:", leading_str)

# Removing trailing whitespace
trailing_str = whitespace_str.rstrip()
print("Trailing Whitespace Removed:", trailing_str)

#finding substrings
main_str = "hello welcome to the school"
#finding the first occurence of the substring
first_index = main_str.find("hello") #case sensitive
print("replaced string",first_index)

#replacing substrings
#replacing all occurences of a substring case sensitive
replaced_str = main_str.replace("hello","hi")
print("replaced string",replaced_str)
