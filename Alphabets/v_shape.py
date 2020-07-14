for row in range(5):
    for col in range(9):
        if row==col or row+col==8 and row<4:
            print("*",end="")
        else:
            print(end=" ")
    print()