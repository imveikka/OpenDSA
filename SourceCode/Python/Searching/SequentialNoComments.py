#/* *** ODSATag: Sequential *** */
def sequentialSearch(elements, e):
    for i in range(len(elements)):
        if elements[i] == e:
            return i
    return -1
#/* *** ODSAendTag: Sequential *** */
