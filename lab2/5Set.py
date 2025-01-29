fruits = {"apple", "banana", "orange", "orange"} # Unordered, Unchangeable, Duplicates Not Allowed
print(fruits)

print(len(fruits))

set1 = {"apple", "banana", "orange", "orange"} # or set(("apple", "banana", "orange", "orange"))
set2 = {6, 1, 7, 6, 3}
set3 = {True, False, True}
set4 = {"abc", 324, False, 4465, "m"}

print(type(fruits))

print("---------Access Set Items-----------")

fruits = {"apple", "banana", "orange", "orange"}
for x in fruits:
    print(x)

print("banana" in fruits)

print("----------Add Set Items----------")

fruits = {"apple", "banana", "orange", "orange"} 
fruits.add("kiwi")
print(fruits)

vegetables = {"carrot", "potato", "tomato"}
fruits.update(vegetables)
print(fruits)

list = ["kiwi", "orange"]
fruits.update(list)
print(fruits)

print("---------Remove Set Items-----------")

fruits = {"apple", "banana", "orange", "orange"}
fruits.remove("orange")
print(fruits)

fruits.discard("banana")
print(fruits)

fruits = {"apple", "banana", "orange", "orange"}
x = fruits.pop() # Remove a random item
print(x)
print(fruits)

fruits.clear()
print(fruits)

fruits = {"apple", "banana", "orange", "orange"}
del fruits # will delete the set completely

print("----------Loop Sets----------")

fruits = {"apple", "banana", "orange", "orange"}
for x in fruits:
    print(x)

print("----------Join Sets----------")

set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = set1.union(set2) # or set3 = set1 | set2
print(set3)

set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = {"apple", "banana", "orange"}
set4 = set1.union(set2, set3) # or set4 = set1 | set2 | set3 
print(set4)

set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set1.update(set2)
print(set1)

set1 = {1, 4, 6, 8}
set2 = {2, 6, 4, 11}
set3 = set1.intersection(set2) # or set3 = set1 & set2
print(set3)

set1 = {1, 4, 6, 8}
set2 = {2, 6, 4, 11}
set1.intersection_update(set2) # to keep ONLY the duplicates, but it will change the original set instead of returning a new set
print(set1)

set1 = {1, 4, 6, 8}
set2 = {2, 6, 4, 11}
set3 = set1.difference(set2) # or set3 = set1 - set2
print(set3)

set1 = {1, 4, 6, 8}
set2 = {2, 6, 4, 11}
set1.difference_update(set2) # to keep the items that are not present in both sets
print(set1)

set1 = {1, 4, 6, 8}
set2 = {2, 6, 4, 11}
set3 = set1.symmetric_difference(set2) # will keep only the elements that are NOT present in both sets. Also you can use set3 = set1 ^ set2.  The ^ operator only allows you to join sets with sets, and not with other data types like you can with the symmetric_difference() method.
print(set1)

set1 = {1, 4, 6, 8}
set2 = {2, 6, 4, 11}
set1.symmetric_difference_update(set2) # will also keep all but the duplicates, but it will change the original set instead of returning a new set. To keep the items that are not present in both sets
print(set1)