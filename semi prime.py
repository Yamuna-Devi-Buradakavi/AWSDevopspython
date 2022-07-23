from math import *
def semiprime(n):
    ran=sqrt(n)
    i=2
    while(i<=ran):
        c=0
        if(n%i==0):#finding factors
            for j in range(2,i):#checking whether any other number can divide the factor
                if(i%j==0):#if it is divided by other,it is not prime
                    c=1#increase count
            if(c==0):#if not
                for k in range(2,n//i):#check the quotient is divided by other number,then it is not prime
                    if((n//i)%k==0):#if it is divid4ed by other,it is not prime
                        c=1
            if(c==0):#true if both are prime.
                return True
        i+=1
    return False
n=int(input())
print(semiprime(n))
