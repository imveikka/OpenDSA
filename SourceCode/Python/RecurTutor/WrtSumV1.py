def sum(arr, n):
    if n == 0:
        return 0
    else:
        smallResult = sum(arr, n - 1);
        return smallResult + arr[n - 1]
