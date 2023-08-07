# J = array of jobs; D = array of deadlines; P = array of profits
def schedule(J, D, P):
    J.sort()                    # Sort the jobs in decreasing order of profit
    S = [None] * len(J)         # Schedule array
    counter = 0                 # counter to the amount of jobs in the schedule
    for i in range(len(J)):
        if D[i] >= counter + 1:
            S[counter] = J[i]   # Add the job to the schedule if the job will be done before the deadline
            counter += 1
    return S
