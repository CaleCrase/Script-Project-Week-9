"""
Program: Week9 Project5
Author: Cale Crase
Sort List
"""
def isSorted(x):
    if len(x) < 2:
        return True
    else:
        for y in range (len(x)):
            if y < len(x) - 1 and x[y] > x[y+1]:
                return False
            return True
