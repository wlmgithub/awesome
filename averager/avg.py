
def average1():
    count = 1
    total = yield
    while True:
        print('count: %s, total: %s' % (count, total))
        total += yield total / count
        count += 1

def average():
    count = 0
    total = 0.
    while True:
        count += 1
        total += yield
        print('%f' % (total / count))


averager = average()

next(averager)

#print( averager.send(2) )
#print( averager.send(4) )
#print( averager.send(6) )

avg = averager.send

for i in (2,4, 6, 7):
    #print(avg(i))
    avg(i)
