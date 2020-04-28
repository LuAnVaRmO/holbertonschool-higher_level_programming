#!/usr/bin/python3
for fn in range(10):
    for sn in range((fn + 1), 10):
        print("{:d}{:d}".format(fn, sn), end="")
        if ((fn == 8) and (sn == 9)):
            print("")
            break
        print(", ", end="")
