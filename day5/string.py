# STRING (str) - Text data

# Creating strings - Method 1: Double quotes
name = "John Doe"
city = "Mumbai"

# Creating strings - Method 2: Single quotes
message = 'Hello World'
quote = 'Python is awesome'

# Both work the same
print(name)
print(message)

# When to use which quotes?
# Use single quotes inside double quotes
sentence1 = "Python's syntax is easy"
print(sentence1)

# Use double quotes inside single quotes
sentence2 = 'He said "Python is great"'
print(sentence2)

#empty string
empty_str = ""
empty_str = ''
print("the empty string is",empty_str)


# Multi-line strings - Triple quotes
paragraph = """This is line 1
This is line 2
This is line 3"""
print(paragraph)
print(type(paragraph))

paragraph2 = '''This is also
a multi-line
string'''
print(paragraph2)
print(type(paragraph2))

#string is a sequence of characters
sample_str = "hello"
"""
h -> 0 
e -> 1
l -> 2
l -> 3
0 -> 4
indexing starts from 0
"""
#accesing characters using indexing
first_char = sample_str[0]
second_char = sample_str[1]
third_char = sample_str[2]
last_char = sample_str[4]
error_char = sample_str[5]#Index error: string index out of range
print("First character:", first_char)
print("Second character:", second_char)
print("Third character:", third_char)   
print("Last character:", last_char)
print("error character:", error_char)


#accesing characters using negative indexing
#starts with -1
first_char = sample_str[0]   # 'H'
second_char = sample_str[1]  # 'e'
third_char = sample_str[2]   # 'l'
fourth_char = sample_str[3]   # 'l'
last_char = sample_str[4]    # 'o'
print("First character:", first_char)
print("Second character:", second_char)
print("Third character:", third_char)   
print("Fourth character:", fourth_char)   
print("Last character:", last_char)


# Accessing characters using negative indexing
last_char = sample_str[-1]    # 'o'
fourth_char = sample_str[-2]   # 'l'
third_char = sample_str[-3]  # 'l'
second_char = sample_str[-4]   # 'e'
first_char = sample_str[-5]   # 'H'
error_char =  sample_str[-6] # IndexError 
print("First character:", first_char)
print("Second character:", second_char)
print("Third character:", third_char)  
print("Fourth character:", fourth_char)    
print("Last character:", last_char)
print("Error character:", error_char)
