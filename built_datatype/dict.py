# Dictionary
# Dictionaries are used to store data values in key:value pairs.
# A dictionary is a collection which is ordered*, changeable and do not allow duplicates.

# dict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# print(dict)
# print(len(dict))#length of the dictionary

#The dict() Constructor
# It is also possible to use the dict() constructor to make a dictionary.

# dict01 = dict(name = "John", age = 36, country = "Norway")
# print(dict01)

# 1.Accessing Items
# You can access the items of a dictionary by referring to its key name, inside square brackets:

# dict =	{
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# x = dict["model"]
# print(x)

# There is also a method called get() that will give you the same result:

# x = dict.get("model")
# print(x)

# The keys() method will return a list of all the keys in the dictionary.

# x = dict.keys()
# print(x)

# The values() method will return a list of all the values in the dictionary.

# x = dict.values()
# print(x)

# The items() method will return each item in a dictionary, as tuples in a list.

# x = dict.items()
# print(x)

# 2.Change Values
# You can change the value of a specific item by referring to its key name:

# dict =	{
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }

# dict["year"] = 2018
# print(dict)

# Update Dictionary
# The update() method will update the dictionary with the items from the given argument.
# The argument must be a dictionary, or an iterable object with key:value pairs.

#dict.update({"year": 2020})
# print(dict)

# 3.Adding Items
# Adding an item to the dictionary is done by using a new index key and assigning a value to it:

# dict["color"] = "red"
# print(dict)

# The update() method will update the dictionary with the items from a given argument. 
# If the item does not exist, the item will be added.

# dict.update({"color": "red"})
# print(dict)

# 4.Removing Items
# There are several methods to remove items from a dictionary:

# dict.pop("model")
# print(dict)

# The popitem() method removes the last inserted item

# dict.popitem()
# print(dict)

# The del keyword removes the item with the specified key name:

# del dict["model"]
# print(dict)

# The clear() method empties the dictionary:

# dict.clear()
# print(dict)

# 5.Copy a Dictionary
# Make a copy of a dictionary with the copy() method

# dict2 = dict.copy()
# print(dict2)

#Make a copy of a dictionary with the dict() function:

# MY1 = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# MY2 = dict(MY1)
# print(MY2)

# 6.Nested Dictionaries
# A dictionary can contain dictionaries, this is called nested dictionaries.

# my = {
#   "child1" : {
#     "name" : "Emil",
#     "year" : 2004
#   },
#   "child2" : {
#     "name" : "Tobias",
#     "year" : 2007
#   },
#   "child3" : {
#     "name" : "Linus",
#     "year" : 2011
#   }
# }

# print(my)


#Or, if you want to add three dictionaries into a new dictionary:

# child1 = {
#   "name" : "Emil",
#   "year" : 2004
# }
# child2 = {
#   "name" : "Tobias",
#   "year" : 2007
# }
# child3 = {
#   "name" : "Linus",
#   "year" : 2011
# }

# my = {
#   "child1" : child1,
#   "child2" : child2,
#   "child3" : child3
# }

# # print(my)

# # 7.Access Items in Nested Dictionaries

# # To access items from a nested dictionary,
# # you use the name of the dictionaries, starting with the outer dictionary:

# print(my["child2"]["name"])
