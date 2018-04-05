

book = {
    2: ['a','b','c'],
    3: ['d','e','f'],
    4: ['g','h','i'],
    5: ['j','k','l'],
    6: ['m','n','o'],
    7: ['p','q','r', 's'],
    8: ['t','u','v'],
    9: ['w','x','y', 'z'],

}

print(book)


def gen_numbers():
    g = (
        '%d%d%d%d%d%d%d%d%d%d' % (
            n1, 
            n2, 
            n3, 
            n4, 
            n5, 
            n6, 
            n7, 
            n8, 
            n9, 
            n10
            )
        for n1 in range(2,10)
        for n2 in range(2,10)
        for n3 in range(2,10)
        for n4 in range(2,10)
        for n5 in range(2,10)
        for n6 in range(2,10)
        for n7 in range(2,10)
        for n8 in range(2,10)
        for n9 in range(2,10)
        for n10 in range(2,10)
    )
    return g

def gen_words(num):
    print(num)
    n1, n2, n3, n4, n5, n6, n7, n8, n9, n10  =  list(str(num)) 
    n1 = int(n1)
    n2 = int(n2)
    n3 = int(n3)
    n4 = int(n4)
    n5 = int(n5)
    n6 = int(n6)
    n7 = int(n7)
    n8 = int(n8)
    n9 = int(n9)
    n10 = int(n10)
    
    g = (
        '%s%s%s%s%s%s%s%s%s%s' % (
            c1,
            c2,
            c3,
            c4,
            c5,
            c6,
            c7,
            c8,
            c9,
            c10,
            )
        for c1 in book[n1]
        for c2 in book[n2]
        for c3 in book[n3]
        for c4 in book[n4]
        for c5 in book[n5]
        for c6 in book[n6]
        for c7 in book[n7]
        for c8 in book[n8]
        for c9 in book[n9]
        for c10 in book[n10]

    )
    return g


def testme():
  for w in gen_words('2345557777'):
      print(w)

def main():
  for n in gen_numbers():
  
      print('=============')
      print(n)
      for w in  gen_words(n):
          print(w)
      


if __name__ == '__main__':
    #testme()
    main()
