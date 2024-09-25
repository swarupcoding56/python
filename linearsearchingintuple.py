tuple=(1,4,9,16,25,36,49,64,81,100)
print("enter the value of x")
a=int(input())
i=0
b=0
a=len(tuple)
while i<a:
    if(tuple[i]==a):
         print("the number",a,"is present in the tuple")
         b=1
         break
    else:
        i=i+1
        b=0
        continue
if(b==0):
    print("the elemnt is not present in the tupple")
    