# Knapsack problem for K and items. Stores solutions in table
def P(i, K):
    if i >= 0 and K >= 0:               # Check indices are inside table
        if table[i][K] == "":           # Not solved
            if P(i - 1, K - items[i]):  # Add "I" if included
                table[i][K] += "I"
            if P(i - 1, K):             # Add "O" if omitted
                table[i][K] += "O"
            if table[i][K] == "":       # Place "-" if no solution found
                table[i][K] = "-"
        return table[i][K] != "-"       # True if any solution found
    else:
        return K == 0                   # Solved if K = 0 (all knapsack is used)
