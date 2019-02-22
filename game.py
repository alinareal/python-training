import argparse
import hashlib
import hmac
import random
from sys import argv


def define_winner(user_choice, computer_choice, list_param):
    result = (computer_choice - int(user_choice)) % len(list_param)
    if result >= (len(list_param)-1) or result < 0:
        print 'Computer win'
    elif result == 0:
        print 'Draw'
    else:
        print 'You win!'


def check_user_choice(user_choice, list_param):
    try:
        user_choice = int(user_choice)
    except ValueError:
        raise ValueError('Choice should be a number!')
    if user_choice == 0:
        exit('Program was stopped')
    if not 1 <= user_choice <= len(list_param):
        raise ValueError('Incorrect choice! Try again! Diaposon minimum is 1, maximum is {}'.format(str(len(list_param))))


secret = str(random.SystemRandom().getrandbits(128))


def encode_choice(choice):
    # secret = "secret_word"
    hmacObj = hmac.new(secret, 'Hi!', digestmod=hashlib.sha384)
    hmacObj.update(str(choice))
    return hmacObj.hexdigest()


def printList(list_param):
    for counter, value in enumerate(list_param, start=1):
        print '{}. {}'.format(counter, value)
    print '0. exit'


def check_list_param(list_param):
    if len(list_param) % 2 == 0 or len(list_param) == 1:
        raise ValueError('List should contain odd number of elements, except 1.')


def create_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument("list_param", nargs='+', help='help')
    return parser


if __name__ == '__main__':
    parser = create_parser()
    namespace = parser.parse_args(argv[1:])
    l_params = namespace.list_param
    check_list_param(l_params)
    printList(l_params)
    computer_choice = random.randrange(1, len(l_params) + 1)
    encoded_comp_choice = encode_choice(computer_choice)
    print 'HMAC: {}'.format(encoded_comp_choice)
    user_choice = raw_input('')
    check_user_choice(user_choice, l_params)
    define_winner(user_choice, computer_choice, l_params)
    print 'Computer choice: ' + str(computer_choice) + ', key: ' + secret