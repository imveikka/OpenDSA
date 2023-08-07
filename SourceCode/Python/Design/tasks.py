def search(k, h):
    if k == n:
        p = min(p, h)
    else:
        for i in range(n):
            if not included[i]:
                included[i] = True
                search(k + 1, h + cost[k][i])
                included[i] = False
