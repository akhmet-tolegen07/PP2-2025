x, y, z = 12, 2135321432, -123241
print (type(x), type(y), type(z))

x1, y1, z1 = 1.2, 43.0, -12.7
print (type(x1), type(y1), type(z1))

x = float(x)
x1 = int(x1)
print(type(x), x)
print(type(x1), x1)

import random
print(random.randrange(1,10))