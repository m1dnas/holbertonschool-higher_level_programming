#!/usr/bin/python3
def islower(c):
    for x in range(97, 123):
        if (ord(c) == ord(chr(x))):
            return True
        else:
            return False
