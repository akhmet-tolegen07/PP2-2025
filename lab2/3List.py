fruits = ["pineapple", "kiwi", "watermelon", "watermelon", "orange", "mango"] # Allow duplicates, Changeable, Ordered
print (fruits)

print("----------Access List Items----------")

print (fruits[1], fruits[-1])
print (fruits[2:-2])
print (fruits[:3])
print (fruits[3:])

if "pineapple" in fruits: print("Yes, we have a pineapple")

print("----------Change List Items----------")

print (fruits)
fruits[0:3] = ["apple", "apple"]
print (fruits)
fruits[0:3] = ["pineapple", "kiwi", "watermelon"]

print("----------Add List Items----------")

print (fruits)
fruits.append("cherry")
print (fruits)
fruits.insert(0, "cherry")
print (fruits)

vegetables = ["carrot", "potato", "tomato"]
fruits.extend(vegetables)
print (fruits)

print("----------Remove List Items----------")

print (fruits)
fruits.remove("watermelon")
print (fruits)

fruits.pop(0)
print (fruits)
fruits.pop() #The last item
print (fruits)

del fruits[-1]
print (fruits)

print (vegetables)
vegetables.clear()
print (vegetables)

print("----------Loop Lists----------")

cars = ["mercedes", "toyota", "ferrari"]
for i in cars: print(i)
for i in range(len(cars)): print(cars[i])
i = 0
while i < len(cars):
    print(cars[i])
    i = i + 1
[print(x) for x in cars]

print("----------List Comprehension----------")

list = ["door", "book", "car", "laptop"]
newlist = []
for i in list: # newlist = [x for x in fruits if "o" in x]
    if "o" in i:
        newlist.append(i)
print(newlist)

newlist = [x for x in list]
print(newlist)

new = [x for x in range(1,11) if x != 5]
print(new)
 
newlist = [x.upper() for x in list]
print(newlist)

newlist = ["new" for x in list]
print(newlist)

print("----------Sort Lists----------")

fruits = ["pineapple", "banana", "mango", "apple"]
fruits.sort()
print (fruits)

numbers = [10, 1, 5, 6, 4]
numbers.sort(reverse = True)
print (numbers)

def myfunc(n):
    return abs(n - 5)

numbers = [10, 5, 6, 2, 3] #Sort the list based on how close the number is to 5
numbers.sort(key = myfunc)
print(numbers)

print("----------Copy Lists----------")

list = ["apple", "banana", "cherry"]
newlist = list.copy() # or newlist = list(list) or newlist = list[:]
print(newlist)

print("----------Join Lists----------")

list1 = [1, 2, 3]
list2 = ["x", "y", "z"]

print(list3 := list1 + list2)