# 1.Set
# Sets are used to store multiple items in a single variable.
#Sets are written with curly brackets.
#A set is a collection which is unordered, unchangeable*, and un_indexed

# set = {"apple", "banana", "cherry"}
# print(set)

# 2.Access Items
# You cannot access items in a set by referring to an index or a key.
# But you can loop through the set items using a for loop,
# or ask if a specified value is present in a set, by using the in keyword.

# set = {"apple", "banana", "cherry"}
# for x in set:
#   print(x)

#Check if "banana" is present in the set:True/false
# set = {"apple", "banana", "cherry"}
# print("banana" in set)

# 3.Add Items
#Once a set is created, you cannot change its items, but you can add new items.
#To add one item to a set use the add() method.
# set = {"apple", "banana", "cherry"}
# set.add("orange")
# print(set)

# 4.Add Sets
#To add items from another set into the current set, use the update() method.
# set01 = {"apple", "banana", "cherry"}
# set02 = {"pineapple", "mango", "papaya"}
# set01.update(set02 )
# print(set01)

# 4.Remove Item
# To remove an item in a set, use the remove(), or the discard() method.
# set = {"apple", "banana", "cherry"}
# set.remove("banana")
# print(set)

#Remove "banana" by using the discard() method:
# set = {"apple", "banana", "cherry"}
# set.discard("banana")
# print(set)

#The return value of the pop() method is the removed item.
#set = {"apple", "banana", "cherry"}
#x = set.pop()
#print(x) #removed item
#print(set) #the set after removal

#The clear() method empties the set:
# set = {"apple", "banana", "cherry"}
# set.clear()
# print(set)

#The del keyword will delete the set completely:
# set = {"apple", "banana", "cherry"}
# del set
# print(set)

# 5.Join Two Sets
# set1 = {"a", "b" , "c"}
# set2 = {1, 2, 3}
# set3 = set1.union(set2)
# print(set3)

#The update() method inserts the items in set2 into set1:
# set1 = {"a", "b" , "c"}
# set2 = {1, 2, 3}
# set1.update(set2)
# print(set1)

# 6.Keep ONLY the Duplicates
#The intersection_update() method will keep only the items that are present in both sets.
# x = {"apple", "banana", "cherry"}
# y = {"google", "microsoft", "apple"}
# x.intersection_update(y)
# print(x)

# 7.Keep All, But NOT the Duplicates
# The symmetric_difference_update() method will keep only the elements that are NOT present in both sets.
# x = {"apple", "banana", "cherry"}
# y = {"google", "microsoft", "apple"}
# x.symmetric_difference_update(y)
# print(x)

# The symmetric_difference() method will return a new set,
# that contains only the elements that are NOT present in both sets.
# x = {"apple", "banana", "cherry"}
# y = {"google", "microsoft", "apple"}
# z = x.symmetric_difference(y)
# print(z)



