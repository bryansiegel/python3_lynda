x = (1, 'two', 3.0, [4, 'four'], 5)
y = [1, 'two', 3.0, [4, 'four'], 5]

print(id(x[0]))
print(id(y[0]))

print(type(x))
print(type(y))

if isinstance(x, tuple):
    print('yep')

