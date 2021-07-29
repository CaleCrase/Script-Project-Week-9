"""
Program: Week9 Project9
Author: Cale Crase
File text average
"""
fileName = input("Enter filename: ")
inputFile = open(fileName, "r")
x = inputFile.read().split()
z = []
for y in x:
    z.append(int(y))
    inputFile.close()
    avg = float(sum(z))/len(z)
print("The average of these numbers are", avg)
