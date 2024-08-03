# my = ("apple", "banana", "cherry")
# print(my)#print tuple
# print(len(my))#length  of tuple
# print(my[1])#access tuple element

# x = ("apple", "banana", "cherry")#Once a tuple is created, you cannot change its values. 
# y = list(x)#You can convert the tuple into a list, change the list, and convert the list back into a tuple.
# y[1] = "kiwi"
# x = tuple(y)
# print(x)

#Add Items
#Convert into a list: Just like the workaround for changing a tuple, you can convert it into a list, 
# add your item(s), 
# and convert it back into a tuple.
# that = ("apple", "banana", "cherry")
# y = list(that)
# y.append("orange")
# that = tuple(y)
# print(that)

#Add tuple to a tuple
#You are allowed to add tuples to tuples, so if you want to add one item,
#  (or many), create a new tuple with the item(s), and add it to the existing tuple:
# this = ("apple", "banana", "cherry")
# y = ("orange",)
# this += y
# print(this)

#Remove Items
#Convert the tuple into a list, remove "apple", and convert it back into a tuple
# Items = ("apple", "banana", "cherry")
# y = list(Items)
# y.remove("apple")
# Items = tuple(y)
# print(Items)

#Or you can delete the tuple completely:
#The del keyword can delete the tuple completely:
# Items = ("apple", "banana", "cherry")
# del Items
# print(Items)

#Unpacking a Tuple
#When we create a tuple, we normally assign values to it. This is called "packing" a tuple:
#But, in Python, we are also allowed to extract the values back into variables. This is called "unpacking":
# fruits = ("apple", "banana", "cherry")
# (green, yellow, red) = fruits
# print(green)
# print(yellow)
# print(red)

#Loop Through a Tuple
#You can loop through the tuple items by using a for loop.
# this = ("apple", "banana", "cherry")
# for x in this:
#   print(x)

# Join Two Tuples
# To join two or more tuples you can use the + operator:
# tuple1 = ("a", "b" , "c")
# tuple2 = (1, 2, 3)

# tuple3 = tuple1 + tuple2
# print(tuple3)

#Multiply Tuples
#If you want to multiply the content of a tuple a given number of times, you can use the * operator:
# fruits = ("apple", "banana", "cherry")
# my = fruits * 2
# print(my)