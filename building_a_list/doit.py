
# https://github.com/algorhythms/HackerRankAlgorithms/blob/master/Building%20a%20List.py

def dfs(seq, cur, res):
    res.append(cur)
    if seq:
        for i in range(len(seq)):
            dfs(seq[i+1:], cur + seq[i], res)

N = int(input())
for _ in range(N):
    len_of_s = int(input())
    s = input()
    #print(len_of_s, s)
    res = []
    seq = ''
    dfs(s, '', res)
    print('\n'.join(res[1:]))



