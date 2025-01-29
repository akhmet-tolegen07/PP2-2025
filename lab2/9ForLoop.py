fruits = ["apple", "banana", "orange"]
for x in fruits:
    print(x)

for x in "banana":
     print(x)

fruits = ["apple", "banana", "orange"]
for x in fruits:
    print(x)
    if x == "orange":
        continue
    if x == "banana":
        break

for i in range(2, 11, 2):
    print(i)
else: print("Only even numbers!")

colors = ["red", "blue", "yellow"]
fruits = ["apple", "banana", "orange"]

for i in colors:
  for j in fruits:
    print(i, j)