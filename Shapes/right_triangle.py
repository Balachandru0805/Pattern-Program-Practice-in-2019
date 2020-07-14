size=int(input())
for row in range(size):
    for col in range(size-row):
        print("*",end=" ")
    print()