#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    division = []
    for i in range(list_length):
        try:
            division.append(my_list_1[i] / my_list_2[i])
            continue
        except TypeError:
            division.append(0)
            print("wrong type")
        except IndexError:
            division.append(0)
            print("out of range")
        except ZeroDivisionError:
            division.append(0)
            print("division by 0")
    return division