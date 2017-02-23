
https://shubhambhattar.wordpress.com/2015/09/27/ncr-table/

def main():
    from sys import stdin, stdout
    t = int(stdin.readline())
    m = 1000000000
 
    table = [[0 for i in range(1001)] for i in range(1001)]
    for i in range(1001):
        #easy base case for nC0 and nCn
        table[i][0] = 1
        table[i][i] = 1
     
    for i in range(2, 1001):
        for j in range(1, i):
            #fill table using the dp relation
            table[i][j] = (table[i-1][j-1] + table[i-1][j]) % m
 
    for i in range(t):
        n = int(stdin.readline())
        for j in range(n+1):
            stdout.write(str(table[n][j]) + ' ')
        stdout.write('\n')
 
 
if __name__ == '__main__':
    main()


