size=int(input())
n=1
low=0
high=size-1
n_list=[[0 for i in range(size)] for j in range(size)]
s1=int(size/2)+1
for row in range(s1):
    for col in range(low,high+1):
        n_list[low][col]=n
        n+=1
    for col in range(low+1,high+1):
        n_list[col][high]=n
        n+=1
    for col in range(high-1,low-1,-1):
        n_list[high][col]=n
        n+=1
    for col in range(high-1,low,-1):
        n_list[col][low]=n
        n+=1
    low+=1
    high-=1
for i in n_list:
    for j in i:
        print(format(j,"<4"),end="")
    print()