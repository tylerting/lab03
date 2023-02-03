#!/usr/bin/python3


def evens(n):
    '''
    Returns a list of even numbers from 0 to n inclusive.
    '''
    result = []
    numbers = []
    if n >= 0:
        numbers = list(range(n+1))
    elif n < 0:
        numbers = list(range(n, 1, -1))
    for i in numbers:
        if i % 2 == 0:
            result.append(i)
    return result
