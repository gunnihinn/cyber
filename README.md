# Cyber

This is an implementation of a book cipher, with the twist that we encode and
decode messages via eBooks instead of a physical book. Since an eBook doesn't
come with a splitting into pages, we create one randomly to encode a message.
The message can then be decoded by creating the same page splitting. To acheive
this, the random splitting is determined by a password that both parties must
share.

Book cipher: https://en.wikipedia.org/wiki/Book_cipher

## TODO

* Find a better name, I guess.
* Grab a couple of example books from Project Gutenberg.
* Create an actual interface people can use.
* Write a function that will check if the words we want to encode are in a given
  book.
* Write a function that filters a list of books and returns those that contain
  the words in the message we want to encode.

## What's in a book cipher?

In a traditional book cipher, two people agree on a specific edition on a book.
To encode messages, they look up each word in the message in the book and note
its page, line and word number, and assign the word that triple. Each word is
encoded this way, and the two persons exchange the list of triples. To decode
the message, we must have the exact same edition of the book so all possible
triples match up.

Suppose now that we have an eBook, or just a text file with the given book. We
no longer have a given coordinization of the words in the book, but we can
create one by splitting the book into pages, lines and so on. The trick is then
that we have to be able to do this in the same way for two people.  The obvious
thing is to do this completely deterministically, but given how fast a computer
can decode a message, this renders the cipher rather useless.

Instead we can try to randomize the coordinization by declaring that the number
of words on a page lies in some range, and its exact value will be determined by
a random number, for example, and similarly for the other levels of
coordinization. We then ensure that the receiver is able to decode the message
by seeding the random number generator with the same value as the sender did;
possibly by having the seed be the hash of a password or -phrase.

## Is this any better than a book cipher?

I think so. A problem with book ciphers today is that computers can very quickly
check if a message can be decoded with a given book. By randomizing the page
splitting, we should create enough of a combinatorial explosion in the number of
possible encoding schemes for a given book that brute-forcing is no longer a
viable attack technique.

For example, say we have a 90.000 word book. On average, there are about 400
words per page in a book in English. We've defaulted to having between 350 and
450 words per page. Suppose now that we're going to split our book into pages. 
The first page will contain between 350 and 450 words, so we have 100
possibilities for choosing the first page break. At the next page we again
have 100 possibilities for choosing the page break, and so on. The number of
possible paginations of the book, and thus ways of assigning coordinates to the
words in it, is then at least about

    100^(90000/450) = 10^400.

A computer can coordinize a book very quickly, and check if the resulting
encoding makes any sense pretty quickly too. If we say a computer can do this
for a given book and a given message in a millisecond, it'll take it

    10^400 * 0.001 = 10^397 seconds

to check all possible encodings, which is something like 10^390 years.
