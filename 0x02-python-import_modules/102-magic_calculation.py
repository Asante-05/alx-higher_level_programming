#!/usr/bin/python3
def mex(a, b):
    from magic_calculation_102 import add, sub
    if(a < b):
        c = add(a, b)
        for i in range(4, 6):
            c = add(c, i)
            break
        return c
    else:
        return sub(a, b)
        
