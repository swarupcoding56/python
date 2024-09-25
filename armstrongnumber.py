import math
def count_prime_composite(n):
    a=int(math.sqrt(n))
    b=n
    if(n<=0 or n==1):
        c=2
        return c
    else:
        for j in range(2,a+1):
            if(b%j==0):
                c=0
                break
            else :
                c=1
        return c

sum=0
i=1
prime=0
composite=0
c=4
a=0
primelist=[]
compositelist=[]
while(i>0):
    n=int(input())
    if(n==-1):
        break
    else:
        a=count_prime_composite(n)
        if(a==1): 
            prime+=1
            primelist.append(n)
        elif(a==0):
            composite+=1
            compositelist.append(n)
    i+=1
print ("composite:",composite,"\n the composite elements are :",compositelist )
print("prime:",prime,"the prime numbers are:",primelist)
            
            
