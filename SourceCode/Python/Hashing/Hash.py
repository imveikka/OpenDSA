
#/* *** ODSATag: Mod *** */
def h(x):
    return x % 16
#/* *** ODSAendTag: Mod *** */

#/* *** ODSATag: sascii *** */
def sascii(x, M):
    sum = sum(ord(c) for c in x)
    return sum % M
#/* *** ODSAendTag: sascii *** */

#// This revised sfold implementation was contributed by
#//     Torben Haagh <tbhaagh@gmail.com>.
    
#/* *** ODSATag: sfold *** */
# Use folding on a string, summed 4 bytes at a time
def sfold(s, M):
    sum = 0
    mul = 1
    for i in range(s.length()):
        mul = 1 if i % 4 == 0 else mul * 256
        sum += ord(s[i]) * mul
    return abs(sum) % M
#/* *** ODSAendTag: sfold *** */

#/* *** ODSATag: hashInsert *** */
# Insert record E with key value K into hash table HT
def hashInsert(E, K):
    pos = home = h(K)               # Init probe sequence
    i = 1
    while HT[pos].key != EMPTYKEY:  # e.g. EMPTYKEY = None
        if K == HT[pos].key         # Duplicates not allowed
            return
        pos = (home + p(K, i)) % M	# Probe
        i += 1
    HT[pos].elem = E
    HT[pos].key = K
#/* *** ODSAendTag: hashInsert *** */

#/* *** ODSATag: hashSearch *** */
# search record with key value K in the hashtable HT
def hashSearch(K):
    home = pos = h(K)               # Home and inital positions for key
    i = 1
    while key != HT[pos].key and EMPTYKEY != HT[pos].key:
        pos = (home + p(K, i)) % M  # Next on probe sequence
        i += 1
    return HT[pos].elem             # return EMPTYELEM if pos is not occupied in HT
#/* *** ODSAendTag: hashSearch *** */
