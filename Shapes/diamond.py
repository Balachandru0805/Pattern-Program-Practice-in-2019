size=int(input())
for row in range(size):
    for space in range(size-(row+1)):
        print(" ",end="")
    for star in range(row+1):
        print("*",end=" ")
    print()
for row in range(size-1):
    for space in range(row+1):
        print(" ",end="")
    for star in range((size)-(row+1)):
        print("*",end=" ")
    print()
        