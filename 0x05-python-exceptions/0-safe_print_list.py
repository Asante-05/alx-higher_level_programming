#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    try:
        c = 0
        while (c < x):
            print("{:d}".format(my_list[c]), end="")
            c += 1
    except IndexError:
        raise IndexError
    finally:
        print()
        return c
