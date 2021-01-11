def inner(z):
    return z * x


def outer(x, y):
    return inner(x) + y


print(outer(2, 5))
