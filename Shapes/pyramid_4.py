size=int(input())
x=0
while x < size:
    y=0
    while y< size-(x+1):
        print(" ",end="  ")
        y+=1
    z=0
    while z<x+1:
        print("*",end="     ")
        z+=1
    print()
    x+=1
    