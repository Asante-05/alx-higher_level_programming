#!/usr/bin/python3

def safe_function(fct, *args):
    try:
        result = fct(*args)
        return result
    except Exception as error:
        print("Execution: {}".format(error), file=sys.stderr)
        return None
