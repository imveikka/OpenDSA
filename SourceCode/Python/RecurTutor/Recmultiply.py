def multiply(x, y):
    if x == 1:
        return y
    else:
        return multiply(x - 1, y) + y
