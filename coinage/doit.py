# https://github.com/algorhythms/HackerRankAlgorithms/blob/master/Coinage.py

class Solution:
    def __init__(self):
        self.coinage = [1, 2, 5, 10]
        self.count = {}
        self.A = None

    def solve(self, cipher):
        """
        dp
        :param cipher: the cipher
        """
        target, self.A = cipher
        return self.get_count(target, 3)

    def get_count(self, n, k):
        """
        algorithm top-down dp
        bottom-up dp: https://github.com/derekhh/HackerRank/blob/master/coinage.cpp
        :param seq:
        :param n: target
        :param k: current examining coin
        """
        if (n, k) not in self.count:
            if k == 0:
                if n % self.coinage[k] == 0 and self.coinage[k] * self.A[k] >= n:
                    self.count[(n, k)] = 1
                else:
                    self.count[(n, k)] = 0
            else:
                i = 0
                cnt = 0
                while i <= self.A[k] and i * self.coinage[k] <= n:
                    cnt += self.get_count(n - i * self.coinage[k], k - 1)
                    i += 1
                self.count[(n, k)] = cnt

        return self.count[(n, k)]


if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        # construct cipher
        target = int(input())
        lst =  [ int(i) for i in input().split() ]
        cipher = target, lst
        # solve
        s = "%s\n" % (Solution().solve(cipher))
        print('{}'.format(s), end='')
