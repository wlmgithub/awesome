# http://freshfoo.com/posts/itertools_groupby/ 

from itertools import groupby
from operator import itemgetter
import random

things = [('2009-09-02', 11),
          ('2009-09-02', 3),
          ('2009-09-03', 10),
          ('2009-09-03', 4),
          ('2009-09-03', 22),
          ('2009-09-06', 33)]

random.shuffle(things)
#things.sort()
things = sorted(things)

for key, items in groupby(things, itemgetter(0)):
    print key
    for subitem in items:
        print subitem
    print '-' * 20
