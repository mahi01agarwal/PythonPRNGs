seed =17
RandomNumbers = [seed]
while(seed!=1):
    if(seed%2==0):
       seed = int(seed/2)
       RandomNumbers.append(seed)
    else:
        seed = 3*seed +1
        RandomNumbers.append(seed)


#Printing Trajectory for given seed
print(RandomNumbers)            