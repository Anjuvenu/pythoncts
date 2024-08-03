# 1.List
#Lists are used to store multiple items in a single variable.

# list = ["apple", "banana", "cherry"]
# print(list)
# print(len(list))#length of the list

# 2.type()
#From Python's perspective, lists are defined as objects with the data type 'list':

# list = ["apple", "banana", "cherry"]
# print(type(list))

# 3.The list() Constructor
#It is also possible to use the list() constructor when creating a new list.

# list1 = list(("apple", "banana", "cherry")) # note the double round-brackets
# print(list1)

# 4.Access Items
#List items are indexed and you can access them by referring to the index number:

# list = ["apple", "banana", "cherry"]
# print(list[1])

# Negative Indexing
# Negative indexing means start from the end
# -1 refers to the last item, -2 refers to the second last item etc.

# list = ["apple", "banana", "cherry"]
# print(list[-1])

# 5.Check if Item Exists
# To determine if a specified item is present in a list use the in keyword:

# list = ["apple", "banana", "cherry"]
# if "apple" in list:
#   print("Yes, 'apple' is in the fruits list")

# 6. Change Item Value
# To change the value of a specific item, refer to the index number:

# list = ["apple", "banana", "cherry"]
# list[1] = "blackcurrant"
# print(list)

# 7.Insert Items
# To insert a new list item, without replacing any of the existing values, we can use the insert() method.

# list = ["apple", "banana", "cherry"]
# list.insert(2, "watermelon")
# print(list)

# 8.Append Items
# To add an item to the end of the list, use the append() method:

# list = ["apple", "banana", "cherry"]
# list.append("orange")
# print(list)

# 9.Extend List
# To append elements from another list to the current list, use the extend() method.

# list = ["apple", "banana", "cherry"]
# tropical = ["mango", "pineapple", "papaya"]
# list.extend(tropical)
# print(list)


# 10.Remove Specified Item
# The remove() method removes the specified item.

# list = ["apple", "banana", "cherry"]
# list.remove("banana")
# print(list)

# Remove Specified Index
# The pop() method removes the specified index.

# list = ["apple", "banana", "cherry"]
# list.pop(1)
# print(list)

# The del keyword can also delete the list completely.

# list = ["apple", "banana", "cherry"]
# del list

# 11.Clear the List
# The clear() method empties the list.The list still remains, but it has no content.

# list = ["apple", "banana", "cherry"]
# list.clear()
# print(list)

# 12.List Comprehension
# List comprehension offers a shorter syntax when you want to create a new list.
# based on the values of an existing list.

# fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
# list = []

# for x in fruits:
#   if "a" in x:
#     list.append(x)

# print(list)

# 13.Sort Lists
# i.Sort List Alphanumerically
# List objects have a sort() method that will sort the list alphanumerically, ascending, by default

# list = ["orange", "mango", "kiwi", "pineapple", "banana"]
# list.sort()
# print(list)

# list = [100, 50, 65, 82, 23]
# list.sort()
# print(list)


# ii.Sort Descending
# To sort descending, use the keyword argument reverse = True:

# list = ["orange", "mango", "kiwi", "pineapple", "banana"]
# list.sort(reverse = True)
# print(list)

# list = [100, 50, 65, 82, 23]
# list.sort(reverse = True)
# print(list)

# iii.Case Insensitive Sort
# By default the sort() method is case sensitive, resulting in all capital letters being 
# sorted before lower case letters:

# list = ["banana", "Orange", "Kiwi", "cherry"]
# list.sort()
# print(list)

# iv.Reverse Order
# The reverse() method reverses the current sorting order of the elements.

# list = ["banana", "Orange", "Kiwi", "cherry"]
# list.reverse()
# print(list)

# 14.Copy a List
#There are ways to make a copy, one way is to use the built-in List method copy().

# list1 = ["apple", "banana", "cherry"]
# list2 = list1.copy()
# print(list2)

# Another way to make a copy is to use the built-in method list().

# list1 = ["apple", "banana", "cherry"]
# list2 = list(list1)
# print(list2)

# 15.Join Lists

# Join Two Lists
# There are several ways to join, or concatenate, two or more lists in Python.
# One of the easiest ways are by using the + operator.

# list1 = ["a", "b", "c"]
# list2 = [1, 2, 3]

# list3 = list1 + list2
# print(list3)

# Another way to join two lists is by appending all the items from list2 into list1, one by one:

# list1 = ["a", "b" , "c"]
# list2 = [1, 2, 3]

# for x in list2:
#   list1.append(x)

# print(list1)

# Or you can use the extend() method, where the purpose is to add elements from one list to another list:

# list1 = ["a", "b" , "c"]
# list2 = [1, 2, 3]

# list1.extend(list2)
# print(list1)
