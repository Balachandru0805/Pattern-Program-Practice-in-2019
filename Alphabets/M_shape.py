for row in range(7):
    for col in range(8):
        if col==0 or col==7 or (row==col and row<4) or row+col==7 and row<3:
            print("*",end="")
        else:
            print(end=" ")
    print()