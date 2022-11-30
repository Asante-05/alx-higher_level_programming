#!/usr/bin/python3
def pow(a, b):
    c = a
    if b > 0:
        for i in range(1, b):
            a *= c
        return a
    else:
        for i in range(1, -b):
            a *= c
        a = 1/a
        return a
