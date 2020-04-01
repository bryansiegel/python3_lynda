from decimal import *

#x = 7 / 3 #type float
#x = 7 // 3 #remove remainder
x = .1 + .1 + .1 - .3

#this is how you get zero
a = Decimal('.10')
b = Decimal('.30')
x = a + a + a - b

print(f'x is {x}')
print(type(x))