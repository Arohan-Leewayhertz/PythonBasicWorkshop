f=int(input("Enter the number :"))
def factor(f):
    fac=1
    if(f==0 or f==1):
        print ("The Factorial is 1")
    else:
        for i in range(1,f+1):
            fac*=i    
        print ("The factorial is ",fac)
factor(f)