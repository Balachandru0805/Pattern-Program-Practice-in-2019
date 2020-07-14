size=int(input())
s1=int(size/2)
s2=size+(int(size/3))
for row in range(size):
    for col in range(size):
        if row+col==s1 or row+col==s2 or row-col==s1 or col-row==s1:
            print("*",end="")
        else:
            print(" ",end="")
    print()
