name = "Doni"
def func():
    print ("My name is " + name)
func()

g = "Gg"
def g():
    g = "Aa"
    print (g)
g()
print (g)

f = "Journal"
def f():
    global f 
    f = "Book"
    print (f)
f()
print (f)