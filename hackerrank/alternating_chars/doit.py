
"""
5
AAAA
BBBBB
ABABABAB
BABABA
AAABBB
"""

nums = int(input())

def get_num_dels(s):
    res = 0
    prev = s[0]
    for c in s[1:]:
        if c == prev:
            res += 1
        else:
            prev = c
    return res
        
        
for n in range(nums):
    num_dels = get_num_dels(input())
    print(num_dels)



