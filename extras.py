# Just some tools to convert

from string import ascii_uppercase
import itertools


def iter_all_strings():
    for size in itertools.count(1):
        for s in itertools.product(ascii_uppercase, repeat=size):
            yield "".join(s)


def find_letter(count):
    if count < 3:
        count = 3
    for s in itertools.islice(iter_all_strings(), count-2):
        pass
    return(s)


def find_number(letter):
    count = 2
    for s in iter_all_strings():
        count += 1
        if s == letter.upper():
            return(count)
