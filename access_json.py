import json

# Json files are often used to store configuration settings, data interchange formats, or APIs.
# Dictionaries are often used to represent JSON data in Python.

# READING / CONVERTING JSON DATA
print("Reading and Converting JSON Data")

# json.loads(str): Parse a JSON string into a Python object (e.g., dict, list).
json_string = '{"name": "Alice", "age": 30, "hobbies": ["reading", "cycling"]}'
data = json.loads(json_string)
print(data)  

# json.dumps(obj): Convert a Python object into a JSON-formatted string.
data = {"name": "Alice", "age": 30, "hobbies": ["reading", "cycling"]}
json_string = json.dumps(data)
print(json_string)  

# Optional Parameters:
# indent: Format output for readability (e.g., json.dumps(data, indent=2)).
# sort_keys: Sort dictionary keys (e.g., json.dumps(data, sort_keys=True)).
print(json.dumps(data, indent=2))

# json.load(file): Read JSON data from a file-like object into a Python object.
with open('data.json', 'r', encoding='utf-8') as file:
    data = json.load(file)
print(data)

# json.dump(obj, file): Write a Python object as JSON to a file-like object.
data = {"name": "Alice", "age": 30}
with open('output.json', 'w', encoding='utf-8') as file:
    json.dump(data, file, indent=2)


# ACCESSING JSON DATA
print("\nAccessing JSON Data")
# Accessing Dictionary Keys:
# Use square brackets ([]) or the .get() method for safe access.
data = json.loads('{"name": "Alice", "age": 30, "address": {"city": "Boston", "zip": "02101"}}')
name = data['name']
city = data['address']['city'] 
zip_code = data.get('address').get('zip') 
missing = data.get('phone', 'N/A') 

# Accessing Lists/Arrays:
# Use indexing for lists.
data = json.loads('{"hobbies": ["reading", "cycling", "hiking"]}')
first_hobby = data['hobbies'][0] 
all_hobbies = data['hobbies'] 

# Iterating Over JSON:
# Loop through dictionaries or lists to process data.
data = json.loads('{"users": [{"name": "Alice"}, {"name": "Bob"}]}')
for user in data['users']:
    print(user['name']) 
    

# MODIFYING JSON DATA
print("\nModifying JSON Data")
# Updating Dictionary Values:
# Assign new values to existing keys or add new key-value pairs.
data = json.loads('{"name": "Alice", "age": 30}')
data['age'] = 31
data['email'] = "alice@example.com"
json_string = json.dumps(data)
print(json_string) 

# Modifying Nested Data:
# Access nested structures and update them.
data = json.loads('{"address": {"city": "Boston", "zip": "02101"}}')
data['address']['city'] = "New York"
print(json.dumps(data))

# Appending to Lists:
# Use list methods like append() or extend().
data = json.loads('{"hobbies": ["reading", "cycling"]}')
data['hobbies'].append("hiking")
print(json.dumps(data))

# Deleting Data:
# Use del or pop() to remove keys or list items.
data = json.loads('{"name": "Alice", "age": 30}')
del data['age']
print(json.dumps(data)) 

# Merging JSON Objects:
# Combine dictionaries using update().
data = json.loads('{"name": "Alice"}')
new_data = {"age": 30, "city": "Boston"}
data.update(new_data)
print(json.dumps(data)) 