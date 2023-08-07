# J = array of jobs; D = array of deadlines; P = array of profits
def schedule(J, D, P):
    J.sort()                                # Sort the jobs in decreasing order of profit
    S = [None] * len(J)                     # Schedule array
    for i in range(len(J)):
        for j in range(D[i] - 1, -1, -1):   # find the latest possible free slot meeting the job's deadline
        if not S[j]:
            S[j] = J[i]                     # Add the job to the schedule if the job will be done before the deadline
            break
    return S
