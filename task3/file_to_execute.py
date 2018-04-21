def sum_(x, y):
    return x + y


def pow_(x, y):
    return x ** y


y = 7
x = pow_(sum_(3, y), 3)
print(x, y)
print(x - y == 993, end="\nThat's cool!\n")
