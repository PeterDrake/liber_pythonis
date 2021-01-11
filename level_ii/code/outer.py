def outer(x, y):
    def inner(z):
        return z * x
    return inner(x) + y

print(outer(2, 5))
