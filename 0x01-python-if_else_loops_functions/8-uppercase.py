#!/usr/bin/python3
def uppercase(str):
    for p in str:
        if (ord(p) > 96 and ord(p) < 123):
            p = chr(ord(p) - 32)
        print("{:s}".format(p), end="")
    print("")
