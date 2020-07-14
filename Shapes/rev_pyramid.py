size=int(input())
for row in range(size):
    for space in range(row):
        print(" ",end="")
    for star in range(size-row):
        print("*",end=" ")
    print(6)