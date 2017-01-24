#!/usr/bin/env python3

import argparse
import sys

import cyber


help_messages = {
    'cyber': '''
USE
    
    cyber [encode|decode] <book> <text>
''',
    ###
    'encode': '''
USE

    cyber encode [OPTIONS] <book> <plaintext>

<book> is the file name of the book to use for encoding.
<plaintext> is the message to encode. Read from standard input if none is given.

OPTIONS

    -o, --outfile   Print output to given file
    -v, --version   Print version information
    -h, --help      Print help and exit
''',
    ###
    'decode': '''
USE

    cyber decode [OPTIONS] <book> <cyphertext>

<book> is the file name of the book to use for encoding.
<cyphertext> is the message to decode. Read from standard input if none is given.

OPTIONS

    -o, --outfile   Print output to given file
    -v, --version   Print version information
    -h, --help      Print help and exit
''',
}


# The number of words on a page in a book lies in the closed interval
# [per_page - epsilon, per_page + epsilon] (see randint vs. randrange)
words_config = {
    'per_page': 400,
    'epsilon': 50,
}


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Encrypt and decrypt text')
    parser.add_argument('-v', '--version', action='store_true')
    parser.add_argument('-o', '--outfile')

    parser.add_argument('command')
    parser.add_argument('book')
    parser.add_argument('message')

    args = parser.parse_args()

    if not (args.command and args.book and args.message):
        print(help_messages['cyber'])
        sys.exit(0)

    if not (args.book and args.message):
        print(help_messages[args.command])
        sys.exit(0)

    # TODO: Read from standard input
    password = 'foobar'

    dispatch = {
        'encode': cyber.encode,
        'decode': cyber.decode,
    }

    out = sys.stdout
    if args.outfile:
        out = open(args.outfile, 'w')

    print(dispatch[args.command](args.message, args.book, password), file=out)
