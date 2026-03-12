# 1) Create dictionaries (empty, integer keys, mixed keys, simple details).
empty_dict = {}
int_keys_dict = {1: "one", 2: "two", 3: "three"}
mixed_keys_dict = {"name": "Alice", 1: "first", 2.5: "two and a half"}
simple_details_dict = {"brand": "Ford", "model": "Mustang", "year": 1964}

# 2) Access values:
#    a) Use `dict[key]` and `dict.get(key)` to print values.
print("Value for key 'name' in mixed_keys_dict:", mixed_keys_dict["name"])
print("Value for key 'year' in simple_details_dict:", simple_details_dict.get("year"))

# 3) Update and add:
#    a) Update an existing key’s value.
simple_details_dict["model"] = "F-150"
print("Updated model in simple_details_dict:", simple_details_dict["model"])
#    b) Add a new key-value pair and print the dictionary.
simple_details_dict["color"] = "Red"
print("Updated dictionary:", simple_details_dict)

# 4) Remove and clear:
#    a) Remove a key using `.pop(key)` and print.
removed_value = simple_details_dict.pop("brand")
print("Removed value for 'brand':", removed_value)
print("Dictionary after removal:", simple_details_dict)
#    b) Access a value again using `.get()`.
print("Value for key 'year' in simple_details_dict:", simple_details_dict.get("year"))
#    c) Clear all items using `.clear()` and print the empty dictionary.
simple_details_dict.clear()
print("Cleared dictionary:", simple_details_dict)