def search(y):
    if y == n:
        counter += 1
    else:
        for x in range(n):
            if can_be_placed(y, x):
                location[y] = x
                search(y + 1)
