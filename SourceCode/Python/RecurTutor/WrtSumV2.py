def sum(arr, n):
    if n == 0:
        result = 0
    else:
        smallResult = sum(arr, n - 1);
        result = smallResult + arr[n - 1]
    return result
