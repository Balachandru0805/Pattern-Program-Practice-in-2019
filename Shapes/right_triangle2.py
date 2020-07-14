size=int(input())
for row in range(size):
    for col in range(row+1):
        print("*",end=" ")
    print()