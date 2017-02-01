
import itertools

def powerset1(seq):
    for size in range( len(seq) + 1 ):
        for item in itertools.combinations(seq, size):
            yield item

def powerset2(seq):
    ps = [[]]
    for elem in seq:
        for i in range(len(ps)):
            ps.append(ps[i] + [elem])
    return ps

def powerset(seq):
    res = [[]]
    for x in seq:
        res.extend( [ sub + [x] for sub in res ] )
    return res

if __name__ == '__main__':
    p = powerset('abc')
    for i in p:
        print(i)
