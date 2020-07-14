
size=int(input())
s1=size+(size-1)
for row in range(size):
    for col in range(size):
        if row==0 or col==size-1 or row==col:
            print("*",end=" ")
        else:
            print(end="  ")
    print()