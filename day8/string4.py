#splitting and joining strings
#when we split a string it becomes a list of substrings
#when there is no paramter placed in split, it defaultly splits by whitespace

words_str = "hello world weelcome to python programming"
#splitting a string into list of worlds
split_str = words_str.split()
print("splitting a substring",split_str)

fruits_str = "apple,banana,orange,date"
fruits_list = fruits_str.split(" ")
print("fruits list",fruits_list)

#joining the list of words back to a single string
#it does not have any default value
#we cn specify the seperatror while joining
joined_str = " ".join(split_str)
print("joined string",joined_str)

joined_strcomma = ",".join(fruits_list)
print("joined string with comma",joined_strcomma)

#startswith() and endswith() menthods
#it checks if the string is starting or ending with the specified substring
#it returns true or false
#it is case sensitive
test_str = "hello welcome to python programming."
#checks if the string starts with hello
startswith_hello = test_str.startswith("hello")
print("starts with hello",startswith_hello)
startswith_hellosir = test_str.startswith("hellosir")
print("starts with hellosir",startswith_hellosir)

#checks whether the string ends with programming.
endswith_programming = test_str.endswith("programming.")
print("ends with programming",endswith_programming)
ends_with_java = test_str.endswith("java")
print("ends with java:",ends_with_java)

#count method()
#it counts the number of occurences in a substring
#it is case sensitive
count_str = "python is great,python is awesome,pythone is easy to learn"
#count occurences of python
python_count = count_str.count("python")
print("occurences of python:",python_count)
#count occurences of is
is_count = count_str.count("is")
print("occurences of is:",is_count)
#count occurences of java
java_count = count_str.count("java")
print("occurences of java:",java_count)
#count occurences of s
s_count = count_str.count("s")
print("occurences of s:",s_count)

#IMPORTANT
# VVVIMP
# Slicing strings
# Slicing allows us to extract a portion of a string using indexing
# last index is not included   vvvimp point
# default start is 0 and default end is length of string   
slice_str = "pythonprogramming"
# Extracting substring from index 0 to 5 (not including 5)
substring1 = slice_str[0:5]  # 'pytho'
print("Substring from index 0 to 5:", substring1)
substring_default_start = slice_str[:6]  # 'python'
print("Substring from start to index 6:", substring_default_start)
substring_default_end = slice_str[6:]  # 'programming'
print("Substring from index 6 to end:", substring_default_end)
substring_default_start_and_end = slice_str[:]  # 'pythonprogramming'
print("Substring with default start and end:", substring_default_start_and_end)

# Extracting substring using negative indexing
substring2 = slice_str[-4:-1]  # 'min'
print("Substring from index -4 to -1:", substring2)

