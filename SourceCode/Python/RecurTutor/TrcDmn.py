def Domino(n):
    if n == 1:
        TipOver(1)      # Manually tip the domino over
    else:
        Domino(n - 1)   # To tip the first n-1 dominos over
        TipOver(n)      # The nth domino will be tipped over subsequently
