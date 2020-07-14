size=int(input())
for row in range(size):
    for space in range(size-(row+1)):
        print(format(" ","<3"),end="")
    for n1 in range(row+1,0,-1):
        print(format(n1,"<3"),end="")
    for n2 in range(2,row+2):
        print(format(n2,"<3"),end="")
    print()
    