x , y = 15 , 34
if x > y: print("x is greater than y")
elif x == y: print("x and y are equal")
else: print("y is greater than x")

a , b = 10 , 20
print ("A") if a > b else print("B")

if y > x and y > b: print("Y")

if x > y or x > a: print("X ")

if not x > y: print("Y")

if x > a: 
    print("x is greater than a")
    if x > b:
        print("And also greater than b")
    else: 
        print("But not greater than b")
if x > y: pass # to avoid getting an error