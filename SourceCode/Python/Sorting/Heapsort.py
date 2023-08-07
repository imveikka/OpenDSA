
#/* *** ODSATag: Heapsort *** */
def heapsort(A):
    # The heap constructor invokes the buildheap method
    H = MaxHeap(A)
    # Now sort
    for i in range(len(A)):
        H.removemax(); # Removemax places max at end of heap
#/* *** ODSAendTag: Heapsort *** */
