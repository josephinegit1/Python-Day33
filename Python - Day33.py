import math
import random

print(math.factorial(5))
print(int(math.sqrt(4)))
print(math.pi)

print(random.choice([1,2,3,4,6]))
print(random.randint(1,100))

import mymodule

print(mymodule.greet("john"))
print(mymodule.pi)

from mymodule import greet

print(greet("Alice"))

import pandas as pd

data = {"Name":["Alice","Bob"],"Age":[25,30]}
df = pd.DataFrame(data)
print(df)

print(dir(math))
