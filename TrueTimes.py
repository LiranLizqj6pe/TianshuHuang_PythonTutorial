x = ['Apple']
y = ['Apple']
print(x == y)
print(id(x) == id(y))
y = x
y[0] = 'Orange'
print()
print(x == y)
print(id(x) == id(y))
