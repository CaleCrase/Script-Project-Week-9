"""
Program: Week9 Project8
Author: Cale Crase
Lee's strategy
"""
def printAll(seq):
    if seq:
        print(str(seq))
        print(seq[0])
        printAll(seq[1:])
