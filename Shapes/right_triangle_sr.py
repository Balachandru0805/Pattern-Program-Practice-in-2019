sr=input()
for row in range(len(sr)):
    for col in range(row+1):
        print(sr[col],end=" ")
    print()