
# https://www.martinkysel.com/hackerrank-number-list-solution/

def numberList(a ,k):
    result = 0
    last_biggest = -1
    a_len = len(a)

    for idx in range(a_len):
        if a[idx] > k:
            result += (idx-last_biggest)*(a_len-idx)
            last_biggest = idx

    return result


T = int(input())

for _ in range(T):
    N, K = input().split()
    N, K = int(N), int(K)
    A = input().split()
    A = [ int(i) for i in A ]

    #print(N, K)
    #print(A)
    res = numberList(A, K)
    print(res)
