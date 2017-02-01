
# from python recipe book

import collections

#def flatten(items, ignored_types=(str)):
def flatten1(items):
    for x in items:
#        if isinstance(x, collections.Iterable) and not isinstance(x, ignored_types):
        if isinstance(x, collections.Iterable):
            yield from flatten(x)
#            for i in flatten(x):
#                yield i
        else:
            yield x


def flatten(items, ignored_types=(str)):
    for item in items:
        if not isinstance(item, ignored_types):
            try:
                yield from flatten(item)
            except TypeError:
                yield item

if __name__ == '__main__':
    items = [1, 2, [3, 4, [5, 6], 7], 8, 'aaa', [9, [10]]]

    print(items)
    print(list(flatten(items)))
