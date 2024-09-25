a=int(input("enter number of lines :"))
for i in range(a):
    for j in range(a-i,0,-1):
        print(j,end="")
    print()

