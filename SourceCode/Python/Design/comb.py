def search(k):
    if k == n:
        print(numbers)
    else:
        for i in range(1, m + 1):
            numbers[k] = i
            search(k + 1)
