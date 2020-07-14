for row in range(7):
    for col in range(7):
        if col==3 and row>2:
            print("*",end="")
        elif (row==col  or row+col==6) and row<3:
            print("*",end="")
        else:
            print(end=" ")
    print()