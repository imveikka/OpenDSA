/* *** ODSATag: slide2 *** */
# Sums the first n elements of the array, arr 
def sum(arr, n):
/* *** ODSAendTag: slide2 *** */

/* *** ODSATag: slide3 *** */
result = sum(arr, n)
/* *** ODSAendTag: slide3 *** */

/* *** ODSATag: slide4 *** */
result = sum(arr, 10)
/* *** ODSAendTag: slide4 *** */

/* *** ODSATag: slide7 *** */
sum(arr, 2) 
sum(arr, 1) 
sum(arr, 0)
/* *** ODSAendTag: slide7 *** */

/* *** ODSATag: slide12 *** */
# sums first n elements of arr 
sum(arr, n)
/* *** ODSAendTag: slide12 *** */

/* *** ODSATag: slide13 *** */
# sum first n-1 elements of arr 
sum(arr, n - 1)
/* *** ODSAendTag: slide13 *** */

/* *** ODSATag: slide15 *** */
# return sum of first n elements of arr 
return sum(arr, n - 1) + arr[n-1];
/* *** ODSAendTag: slide15 *** */

/* *** ODSATag: slide16 *** */
if base case:
    # return some simple expression
else:   # recursive case
    # some work before  
    # recursive call 
    # some work after 
/* *** ODSAendTag: slide16 *** */

/* *** ODSATag: slide17 *** */
if recursive case:
    # some work before 
    # recursive call 
    # some work after 
else:   # base case
    # return some simple expression
/* *** ODSAendTag: slide17 *** */
