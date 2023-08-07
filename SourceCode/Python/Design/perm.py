def search(k):
    if k == n:
        # process permutation
    else:
        for i in range(1, n + 1):
            if not included[i]:
                included[i] = True
                numbers[k] = i
                search(k + 1)
                included[i] = False
