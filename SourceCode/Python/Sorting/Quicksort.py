
def swap(A, i, j):
    A[i], A[j] = A[j], A[i]

#/* Warning: Partition is sensitive. If we don't make the right
#   position actually cross the left, then it seems hard to get things
#   to work right when there is only one element in the partition
#   (i.e., a list of 2 elements). */
#/* *** ODSATag: partition *** */
def partition(A, left, right, pivot):
    while (left <= right):      # Move bounds inward until they meet
        while (A[left] < pivot):
            left += 1
        while right >= left and A[right] >= pivot:
            right -= 1
        if right > left:        # Swap out-of-place values
            A[left], A[right] = A[right], A[left]
    return left                 # Return first position in right partition#/* *** ODSAendTag: partition *** */

#/* *** ODSATag: findpivot *** */
def findpivot(A, i, j):
    return (i + j) // 2
#/* *** ODSAendTag: findpivot *** */

#/* *** ODSATag: Quicksort *** */
def quicksort(A, i, j):
    pivotindex = findpivot(A, i, j)                 # Pick a pivot
    A[j], A[pivotindex] = A[pivotindex], A[j]       # Stick pivot at the end
    k = partition(A, i, j-1, A[j])                  # k will be the first position in the right sub-array
    A[j], A[k] = A[k], A[j]                         # Put pivot in place
    if k-i > 1:
        quicksort(A, i, k-1)                        # Sort left partition
    if j-k > 1:
        quicksort(A, k+1, j)                        # Sort right partition
#/* *** ODSAendTag: Quicksort *** */

if __name__ == '__main__':
    arr = [3, 6, 9, 2, 8, 4, 5, 1, 7]
    quicksort(arr, 0, len(arr)-1)
    print(arr)

#/* *** ODSATag: partitionshort *** */
def partition(A, left, right, pivot):
    swap(A, left, pivot)   # Put pivot at the leftmost index
    pivot = left
    left += 1              # Start partitioning from the element after the pivot
    pivotValue = A[pivot]
    while True:
        # Move `left` right as far as possible. Stop if equal to pivot!
        while left <= right and A[left] < pivotValue:
            left += 1
        # Move `right` left as far as possible. Stop if equal to pivot!
        while left <= right and A[right] > pivotValue:
            right -= 1
        # Stop here if `left` and `right` passed each other.
        if left > right:
            break
        # Otherwise, swap the elements and move `left` and `right` on by 1.
        swap(A, left, right)
        left += 1; right -= 1
    swap(A, pivot, right)   # Finally, move the pivot into place
    return right            # Return the position of the pivot
#/* *** ODSAendTag: partitionshort *** */

