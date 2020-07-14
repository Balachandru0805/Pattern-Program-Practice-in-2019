for row in range(5):
    for col in range(7):
        if col==0 or col==6 or col-row==2 and row>0 and row<4:
            print("*",end="")
        elif row+col==4 and row>1 and row<4:
            print("*",end="")
        else:
            print(end=" ")
    print()