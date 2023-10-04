seed = 17

EcondingVector=[]   
#First let us find k such that k is the smallest positive integer such that  n<2^k
k=1
while(True):
    if(pow(2,k)>seed):
       break
    else:
        k=k+1

#Defining function:
def X(n):
    return n%2
def T(n):
    return int((n*pow(3,X(n)) + X(n))/2)

EcondingVector.append(X(seed))

i=1
while(i<k):
    seed = T(seed)
    EcondingVector.append(X(seed)) 
    i=i+1
    
print(EcondingVector)    
       

