fruits = ("pineapple", "kiwi", "watermelon", "watermelon") #Allow Duplicates, Unchangeable, Ordered 
print (fruits)

print("----------Access Tuple Items----------")

print (fruits[1], fruits[-1])
print (fruits[2:-2])
print (fruits[:3])
print (fruits[3:])

print("---------Update Tuples-----------")

fruits = ("apple", "banana", "cherry")
x = list(fruits)
x[1] = "kiwi"
fruits = tuple(x)
print(fruits)

print (fruits)
y = list(fruits)
y.append("orange")
fruits = tuple(y)
print (fruits)

print (fruits)
y = ("orange",)
fruits += y
print (fruits)

print (fruits)
y = list(fruits)
y.remove("orange")
fruits = tuple(y)
print (fruits)

fruits = ("apple", "banana", "cherry")
del fruits # delete the tuple completely

print("----------Unpack Tuples----------")

fruits = ("apple", "banana", "cherry")
(a, b, c) = fruits
print(a)
print(b)
print(c)

fruits = ("apple", "banana", "cherry")
(a, *b, c) = fruits #Add a list of values the "tropic" variable
print(a)
print(b)
print(c)

print("----------Loop Tuples----------")

list = ("door", "book", "car", "laptop")
for x in list:
    print(x)    

for i in range(len(list)):
    print(list[i])

print("----------Join Tuples----------")

tuple1 = ("a", "b", "c")
tuple2 = (1, 2, 3)

tuple3 = tuple1 + tuple2
print (tuple3)
