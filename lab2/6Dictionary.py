car = {
  "brand": "Mercedes", # Changeable. Duplicates Not Allowed. Python version 3.7, dictionaries are ordered. In Python 3.6 and earlier, dictionaries are unordered.
  "model": "Benz",
  "year": 1987,
  "year": 2023
}
print(car)
print(car["brand"])

print("----------Access Dictionary Items----------")

car = {
  "brand": "Mercedes",
  "model": "Benz",
  "year": 1987,
}
x = car["model"]
y = car.get("model")
print (x, y)
print (car.keys())\

x = car.keys()
print(x) #before the change
car["color"] = "yellow"
print(x) #after the change

print("----------Change Dictionary Items----------")

car = {
  "brand": "Mercedes",
  "model": "Benz",
  "year": 1987,
}
car["year"] = 2018
car.update({"year": 2020})
print(car["year"])

print("----------Add Dictionary Items----------")

car = {
  "brand": "Mercedes",
  "model": "Benz",
  "year": 1987,
}
car["color"] = "yellow" # or car.update({"color": "red"})
print(car)

print("----------Remove Dictionary Items----------")

car = {
  "brand": "Mercedes",
  "model": "Benz",
  "year": 1987,
}
car.pop("model")
print(car)
car.popitem() # removes the last inserted item
print(car)
#del car["model"] removes the item with the specified key name  
car.clear() # empties the dictionary
print(car)
del car # can also delete the dictionary completely

print("----------Loop Dictionaries----------")

car = {
  "brand": "Mercedes",
  "model": "Benz",
  "year": 1987,
}
for x in car: print(x) # all key names in the dictionary
for x in car.keys(): print(x) # all key names in the dictionary
for x in car: print(car[x]) # all values in the dictionary
for x in car.values(): print(x) # all values in the dictionary
for x, y in car.items(): print(x, y) # both keys and values in the dictionary

print("----------Copy Dictionaries----------")

car = {
  "brand": "Mercedes",
  "model": "Benz",
  "year": 1987,
}
newcar = car.copy() # or newcar = dict(car)
print(newcar)

print("----------Nested Dictionaries----------")
 
family = { # A dictionary can contain dictionaries, this is called nested dictionaries.
  "child1" : {
    "name" : "Aidos",
    "year" : 2000
  },
  "child2" : {
    "name" : "Tobi",
    "year" : 2005
  },
  "child3" : {
    "name" : "Peter",
    "year" : 1998
  }
}

print(family["child1"]["year"])

for x, z in family.items(): # through the keys and values of all nested dictionaries
    print(x)
    for y in z:
        print(y + ':', z[y])