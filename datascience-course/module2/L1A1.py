# 1) Create a list with a few fruit names:
#    a) Store multiple string items inside a list variable.
fruits = ["Apple", "Banana", "Cherry", "Date", "Elderberry"]

# 2) Print basic list details:
#    a) Print the length of the list using `len()`.
print("Length of the list:", len(fruits))
#    b) Print the first element using index `[0]`.
print("First element:", fruits[0])
#    c) Print the last element using index `[-1]`.
print("Last element:", fruits[-1])

# 3) Add a new item to the list:
#    a) Use `.append()` to add one more fruit.
fruits.append("Fig")
#    b) Print the updated list.
print("Updated list:", fruits)

# 4) Remove an item from the list:
#    a) Use `.remove()` to delete a specific fruit by name.
fruits.remove("Banana")
#    b) Print the updated list.
print("Updated list:", fruits)

# 5) Sort the list:
#    a) Use `.sort()` to arrange items in alphabetical order.
fruits.sort()
#    b) Print the sorted list.
print("Sorted list:", fruits)

# 6) Remove an item using index:
#    a) Use `.pop(index)` to remove an element at a specific position.
fruits.pop(0)
#    b) Print the updated list.
print("Updated list:", fruits)

# 7) Reverse the list order:
#    a) Use `.reverse()` to reverse the items.
fruits.reverse()
#    b) Print the reversed list.
print("Reversed list:", fruits)

# 8) Multiply the list:
#    a) Print the list repeated multiple times using `list * 2`.
print("Multiplied list:", fruits * 2)

# 9) Slice the list:
#    a) Keep only the first few elements using slicing (example: `list[:4]`).
sliced_list = fruits[:4]
#    b) Print the sliced list.
print("Sliced list:", sliced_list)

# 10) Clear the list:
#     a) Use `.clear()` to remove all elements. 
fruits.clear()
#     b) Print the updated (empty) list.    
print("Cleared list:", fruits)