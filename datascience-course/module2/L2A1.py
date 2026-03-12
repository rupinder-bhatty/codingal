# 1) Create different types of tuples:
#    a) Empty tuple, tuple of integers, tuple with mixed data types, and a nested tuple.    
empty_tuple = ()
int_tuple = (1, 2, 3, 4, 5)
mixed_tuple = ("Hello", 42, 3.14, [1, 2, 3])
nested_tuple = (1, "Nested", (2, 3), [4, 5])


# 2) Access tuple elements using indexing:
#    a) Print the first element and last element using indexes like `[0]` and `[last]`.
print("First element of int_tuple:", int_tuple[0])
print("Last element of int_tuple:", int_tuple[-1])  

# 3) Access elements inside a nested tuple:
#    a) Use double indexing to access:
#       - a character from a string inside the tuple
print("Character from nested string:", nested_tuple[1][0])
#       - a value from a list inside the tuple
print("Value from nested list:", nested_tuple[3][0])

# 4) Slice the tuple:
#    a) Print a portion of the tuple using slicing like `[start:end]`.
sliced_tuple = int_tuple[1:4]
print("Sliced tuple (index 1 to 3):", sliced_tuple)
# 5) Iterate through the tuple:
#    a) Use a `for` loop to print each element with a message.
for element in int_tuple:
    print(f"Element: {element}")    