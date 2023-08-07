
#/* *** ODSATag: Mergesort *** */
def mergesort(A, temp, left, right):
  if left == right:                 # List has one record
    return
  mid = (left+right)/2              # Select midpoint
  mergesort(A, temp, left, mid)     # Mergesort first half
  mergesort(A, temp, mid+1, right)  # Mergesort second half
  for i in range(left, right+1):    # Copy subarray to temp
    temp[i] = A[i]
  # Do the merge operation back to A
  i1 = left
  i2 = mid + 1
  for curr in range(left, right+1):
    if i1 == mid+1:                 # Left sublist exhausted
      A[curr] = temp[i2]
      i2 += 1
    elif i2 > right:                # Right sublist exhausted
      A[curr] = temp[i1]
      i1 += 1
    elif temp[i1] <= temp[i2]:      # Get smaller value
      A[curr] = temp[i1]
      i1 += 1
    else:
      A[curr] = temp[i2]
      i2 += 1
#/* *** ODSAendTag: Mergesort *** */


#/* *** ODSATag: MergesortOpt *** */
def mergesortOpt(A, temp, left, right):
  mid = (left+right)/2      # Select the midpoint
  if (left == right):       # List has one record
    return
  if mid-left >= THRESHOLD:
    mergesortOpt(A, temp, left, mid)
  else:
    insertionsort(A, left, mid)
  if right-mid > THRESHOLD:
    mergesortOpt(A, temp, mid+1, right)
  else:
    insertionsort(A, mid+1, right)
  # Do the merge operation.  First, copy 2 halves to temp.
  for i in range(left, mid+1):
    temp[i] = A[i]
  i = mid+1
  for j in range(right, mid, -1):
    temp[i] = A[j]
    i += 1
  # Merge sublists back to array
  i = left; j = right
  for k in range(left, right+1):
    if temp[i] <= temp[j]:
      A[k] = temp[i]
      i += 1
    else:
      A[k] = temp[j]
      j -= 1
#/* *** ODSAendTag: MergesortOpt *** */

#/* *** ODSATag: mergesort *** */
def mergesort(inlist):
    if len(inlist) <= 1:
        return inlist
    l_1 = inlist[len(inlist) // 2 :]    # half of the items from inlist
    l_2 = inlist[: len(inlist) // 2]    # other hald of the items
    return merge(mergesort(l_1), mergesort(l_2))
#/* *** ODSAendTag: mergesort *** */


#/* *** ODSATag: merge *** */
def merge(l_1, l_2):
    answer = []
    while l_1 or l_2:
        if not l_1:     # l_1 is empty, append rest items from l_2
            answer += l_2
            break
        elif not l_2:   # l_2 is empty, append rest items from l_1
            answer += l_1
            break
        elif l_1[0] <= l_2[0]:
            answer.append(l_1.pop(0))
        else:
            answer.append(l_2.pop(0))
    return answer
#/* *** ODSAendTag: merge *** */
