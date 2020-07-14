size=int(input())
x=0
while x<size:
    y=0
    while y<size-x:
        print("*",end=" ")
        y+=1
    print()
    x+=1