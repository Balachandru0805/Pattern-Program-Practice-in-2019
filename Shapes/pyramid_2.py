size=int(input())
no=1
for row in range(size):
    for space in range(size-(row+1)):
        print(format(" ","<5"),end="")
    for col in range(row+1):
        print(format(no,"<10"),end="")
        no+=1
    print()