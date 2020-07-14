size=int(input())
n1=int(size/2)
for row in range(n1):
    for space in range((n1-(row+1))):
        print(" ",end="")
    for star in range(row+1):
        print("*",end=" ")
    for space in range(2*(n1-(row+1))):
        print(" ",end="")
    for star in range(row+1):
        print("*",end=" ")
    print()
sr="chandru"
n2=size-len(sr)
s1=int(n2/2)
s2=n2-s1
print("* "*s1,end="")
for i in sr:
    print(i,end=" ")
print("* "*s2,end="\n")
for row in range(size):
    for space in range(row):
        print(" ",end="")
    for star in range(size-row):
        print("*",end=" ")
    print()
    
    