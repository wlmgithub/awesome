from pprint import pprint
import itertools

DIGIT_TO_LETTERS = {
    '2': ['A','B','C'],
    '3': ['D','E','F'],
    '4': ['G','H','I'],
    '5': ['J','K','L'],
    '6': ['M','N','O'],
    '7': ['P','Q','R','S'],
    '8': ['T','U','V'],
    '9': ['W','X','Y','Z'],
}

def gen_phone_numbers():
    phone_numbers_iter =  itertools.product(
        range(2,10), 
        range(2,10),
        range(2,10), 
        range(2,10), 
        range(2,10), 
        range(2,10), 
        range(2,10), 
        range(2,10), 
        range(2,10), 
        range(2,10), 
    )
    for phone_number_tuple in phone_numbers_iter:
        phone_number = ''.join(map(str, phone_number_tuple))
        yield phone_number

def gen_letters_for(phone_number):
#    print('gen letters for phone #: {}'.format(phone_number))
#    pprint(DIGIT_TO_LETTERS)

    iter_str = 'itertools.product('
    for n in phone_number:
#        print(n, DIGIT_TO_LETTERS[n])
        iter_str += str(DIGIT_TO_LETTERS[n]) + ','
    iter_str = iter_str[:-1]
    iter_str += ')'

    # e.g., for 2345557777
    # the iter_str should be:
    #  
    # itertools.product(['A', 'B', 'C'],['D', 'E', 'F'],['G', 'H', 'I'],['J', 'K', 'L'],['J', 'K', 'L'],['J', 'K', 'L'],['P', 'Q', 'R', 'S'],['P', 'Q', 'R', 'S'],['P', 'Q', 'R', 'S'],['P', 'Q', 'R', 'S'])

    # TODO: there might be a better way to do without using eval
    iter_letters = eval(iter_str)

    for letter_str in iter_letters:
        print('{} {}'.format(phone_number, ''.join(letter_str)))

def test_one_number():
    gen_letters_for('2345557777')


def main():
    for phone_number in gen_phone_numbers():
        gen_letters_for(phone_number)


if __name__ == '__main__':
#     test_one_number()
    main()

