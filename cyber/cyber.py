#!/usr/bin/env python3

import random
import re
from collections import defaultdict


# The number of words on a page in a book lies in the closed interval
# [per_page - epsilon, per_page + epsilon] (see randint vs. randrange)
words_config = {
    'per_page': 400,
    'epsilon': 50,
}


def split(text):
    return ( char for char in text.strip() )


def parseCiphertextFile(filename):
    with open(filename) as fh:
        contents = fh.read()
        matches = [ int(d) for d in re.findall(r'\d+', contents) ]
        return list(zip(matches[0::2], matches[1::2]))


def parsePlaintextFile(filename):
    with open(filename) as fh:
        contents = fh.read()
        return [ word.lower() for word in split(contents) ]


def paginate(words, password):
    'Divide words into pages'
    target = words_config['per_page']
    epsilon = words_config['epsilon']

    # Split words into pages
    random.seed(password)
    pages = []
    while words:
        count = target + random.randint(-epsilon, epsilon)
        (page, words) = (words[0:count], words[count:])
        pages.append(page)

    return pages


def coordinize(pages):
    'Coordinize pages'
    # Assign each word a list of its coordinates
    coordinates = defaultdict(list)
    for pageNr, page in enumerate(pages):
        for wordNr, word in enumerate(page):
            coordinates[word].append((pageNr, wordNr))

    return coordinates


def encode(plaintext, filename, password):
    'Encode a message based on book in filename and password'
    coordinates = coordinize(paginate(parsePlaintextFile(filename), password))

    random.seed()
    cyphertext = []
    words = ( word.lower() for word in split(plaintext) )
    for word in words:
        coords = coordinates[word]
        cyphertext.append(coords[random.randrange(0, len(coords))])

    return cyphertext


def decode(cyphertext, filename, password):
    'Decode a message by looking up in book in filename'
    pages = paginate(parsePlaintextFile(filename), password)

    # cyphertext is a list of pairs of numbers
    plaintext = []
    for (page, word) in parseCiphertextFile(cyphertext):
        plaintext.append(pages[page][word])

    return ''.join(plaintext)
