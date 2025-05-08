# Dictionary comprehensions can create dictionaries
# in a single line of code, similar to list comprehensions.
# Keys are unique, and duplicate keys will be overwritten.
# Similarly, they traverse an iterable to create a new dict,
# and are generally faster than comparable loops.
# In the same way, keep it SOLID and avoid side effects.
#
# Syntax:
# {KEY_EXPRESSION: VALUE_EXPRESSION for ITEM in ITERABLE if CONDITION}
# 
# key_expression: Defines the key for each dictionary entry.
# value_expression: Defines the value associated with the key.
# item: The variable representing each element in the iterable.
# iterable: A sequence (e.g., list, tuple, range, string).
# condition (optional): Filters items based on a boolean expression.

squares = {x: x**2 for x in range(5)}
# Output: {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}

# nested loops
numbers = [1, 2, 3, 4]
parity = {x: "even" if x % 2 == 0 else "odd" for x in numbers}
# Output: {1: 'odd', 2: 'even', 3: 'odd', 4: 'even'}

# data transformation
numbers = [1, 2, 3]
squared_dict = {num: num**2 for num in numbers}
# Output: {1: 1, 2: 4, 3: 9}

# filtering
numbers = [1, 2, 3, 4, 5]
even_squares = {x: x**2 for x in numbers if x % 2 == 0}
# Output: {2: 4, 4: 16}

# inverting - swapping the keys and values
original = {'a': 1, 'b': 2, 'c': 3}
inverted = {v: k for k, v in original.items()}
# Output: {1: 'a', 2: 'b', 3: 'c'}

# mapping keys to computed values
names = ["alice", "bob"]
name_lengths = {name: len(name) for name in names}
# Output: {'alice': 5, 'bob': 3}

# combining dictionaries
dict1 = {'a': 1, 'b': 2}
dict2 = {'c': 3, 'd': 4}
combined = {k: v*2 for d in [dict1, dict2] for k, v in d.items()}
# Output: {'a': 2, 'b': 4, 'c': 6, 'd': 8}

# Key differences between list and dict comprehensions are
# lists store all elements, but dicts store key value pairs
# lists allow duplicates, dict keys must be unique and hashable.
# For dictionaries, the last value overwrites the existing.