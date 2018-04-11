# based on: pythonbeyondbasics

import re

class Money:
    def __init__(self, dollars, cents):
        self.dollars = dollars
        self.cents = cents
    def __repr__(self):
        return '${}.{}'.format(self.dollars, self.cents)
    
    @classmethod
    def get_from_pennies(cls, num_pennies):
        dollars, cents = divmod(num_pennies, 100) 
        return cls(dollars, cents)

    @classmethod
    def get_from_string(cls, astring):
        p = re.compile(r'^\$?(?P<dollars>\d+)\.(?P<cents>\d+)')
        m = p.search(astring)
        if m:
            return cls(m.group('dollars'), m.group('cents'))
        else:
            return cls(0,0)
        

if __name__ == '__main__':

    m1 = Money(12, 34)
    print(m1)
    
    m2 = Money.get_from_pennies(121)
    print(m2)
    
    m3 = Money.get_from_string('123.45')
    print(m3)
    
    m4 = Money.get_from_string('$1239.45')
    print(m4)
    
    m5 = Money.get_from_string('foobar')
    print(m5)
    
    
