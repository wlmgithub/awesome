
# Mastering Python

import functools

def coroutine(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        f = func(*args, **kwargs)
        next(f)
        return f
    return wrapper


@coroutine
def replace(search, replace):
    while True:
        item = yield
        print(item.replace(search, replace))


@coroutine
def replace(search, replace):
    while True:
        item = yield
        yield item.replace(search, replace)


@coroutine
def replace(search, replace):
    item = yield
    while True:
        item = yield item.replace(search, replace)

# Grep sends all matching items to the target
@coroutine
def grep(target, pattern):
    while True:
        item = yield
        if pattern in item:
            target.send(item)

# Replace does a search and replace on the items and sends it to
# the target once it's done
@coroutine
def replace(target, search, replace):
    while True:
        target.send((yield).replace(search, replace))

# Print will print the items using the provided formatstring
@coroutine
def print_(formatstring):
    while True:
        print(formatstring % (yield))

# Tee multiplexes the items to multiple targets
@coroutine
def tee(*targets):
    while True:
        item = yield
        for target in targets:
            target.send(item)



def main():

    # Because we wrap the results we need to work backwards from the
    # inner layer to the outer layer.
    # First, create a printer for the items:
    printer = print_('%s')

    # Create replacers that send the output to the printer
    replacer_spam = replace(printer, 'spam', 'bacon')
    replacer_eggs = replace(printer, 'eggs eggs', 'sausage')

    # Create a tee to send the input to both the spam and the eggs
    # replacers
    branch = tee(replacer_spam, replacer_eggs)
    # Send all items containing spam to the tee command
    grepper = grep(branch, 'spam')

    # Send the data to the grepper for all the processing
    for line in open('lines.txt'):
        grepper.send(line.rstrip())


if __name__ == '__main__':
    main()


