size=int(input())
for row in range(size):
    for col in range(2*size-1):
        if (row==size-1 and col%2==0)  or row+col==size-1 or col-row==size-1:
            print("*",end="")
        else:
            print(end=" ")
    print()