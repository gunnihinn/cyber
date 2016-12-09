#!/usr/bin/env python3

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
    try:
        subcommand = sys.argv[1]
    except IndexError:
        subcommand = 'cyber'

    if len(sys.argv) < 3:
        print(help_messages[subcommand])
        sys.exit(0)

    book = sys.argv[2]

    # TODO: Read from standard input
    password = 'foobar'

    try:
        message = sys.argv[3]
    except IndexError:
        message = '-'

    dispatch = {
        'encode': cyber.encode,
        'decode': cyber.decode,
    }

    print(dispatch[subcommand](message, book, password))
