# List comprehensions are a useful way for creating and populating
# a list in a single line of code. Note, lambdas should adhere to 
# the Single Responsibility Principle (Be SOLID!)
# Comprehensions are generally faster than equivalent loops
# as they are optimized in the python interpreter.
# 
# Syntax:
# [EXPRESSION for ITEM in ITERABLE if CONDITION]
#
# expression: The value or transformation applied to each item.
# item: The variable representing each element in the iterable.
# iterable: A sequence (e.g., list, tuple, string, range).
# condition (optional): Filters items based on a boolean expression.

squares = [x**2 for x in range(5)]
# Output: [0, 1, 4, 9, 16]

# nested loops can be applied
pairs = [(x, y) for x in [1, 2] for y in [3, 4]]
# Output: [(1, 3), (1, 4), (2, 3), (2, 4)]

# data transformation can be applied to each element
words = ["hello", "world"]
upper = [word.upper() for word in words]
# Output: ['HELLO', 'WORLD']

# an existing iterable can be filtered by condition
numbers = [1, 2, 3, 4, 5]
odds = [x for x in numbers if x % 2 != 0]
# Output: [1, 3, 5]

# lists can be reshaped. Below flattens a 2-dimensional list.
nested = [[1, 2], [3, 4]]
flat = [num for sublist in nested for num in sublist]
# Output: [1, 2, 3, 4]