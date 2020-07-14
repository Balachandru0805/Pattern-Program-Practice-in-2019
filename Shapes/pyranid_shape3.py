size=int(input())
for row in range(size):
    for space in range(size-(row+1)):
        print(" ",end="  ")
    for n1 in range(row+1):
        print("*",end="     ")
    print()