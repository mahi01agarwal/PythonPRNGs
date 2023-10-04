#Linear Copngruential Generator
#Let us define m , a , c, seed

m= 7829
a=378
c=2310
seed = 4321

RandomNumbers = [seed]
n =10
while(n>0):
   seed = (seed*a+c)%m
   RandomNumbers.append(seed)
   n=n-1
   
print(RandomNumbers)   


