#!/usr/bin/python3
def multiple_returns(sentence):
    if sentence == "" or sentence is None:
        return None
    tup = tuple(sentence)
    return len(tup), tup[0]
