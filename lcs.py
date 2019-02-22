import argparse
from sys import argv


def create_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument("list_param", nargs='+', help='help')
    return parser


def long_substr(data):
    substr = ''
    if len(data) > 1 and len(data[0]) > 0:
        for i in range(len(data[0])):
            for j in range(len(data[0])-i+1):
                if j > len(substr) and is_substr(data[0][i:i+j], data):
                    substr = data[0][i:i+j]
    elif len(data) == 1:
        return data[0]
    else:
        return ''
    return substr


def is_substr(find, data):
    if len(data) < 1 and len(find) < 1:
        return False
    for i in range(len(data)):
        if find not in data[i]:
            return False
    return True


if __name__ == '__main__':
    parser = create_parser()
    namespace = parser.parse_args(argv[1:])
    l_params = namespace.list_param
    check_list_param(l_params)
    print long_substr(l_params)
