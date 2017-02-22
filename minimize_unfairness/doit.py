
# https://www.martinkysel.com/hackerrank-max-min-solution/


N = int(input())
K = int(input())

A = [ int(input()) for _ in range(N)]
A.sort()
#print(A)

refnum = 1000000000000
for i in range(N - K + 1):
    refnum = min(refnum, A[i+K-1] - A[i])

print(refnum)


"""  This works, but not efficient
def get_all_groups(A, N, K):
    G = []
    for i in range(N - K + 1):
        g = []
        for j in range(K):
            g.append(A[j+i])
        G.append(g)
    return G

all_groups = get_all_groups(A, N, K)

#print(all_groups)

first_group = all_groups[0]
refnum = first_group[-1] - first_group[0]

for g in all_groups[1:]:
    maxmin = g[-1] - g[0]
    if maxmin < refnum:
        refnum = maxmin
"""
