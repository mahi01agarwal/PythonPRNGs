def Logistic_Keys(x_init,r,NumOfKeys,ScalingFactor,UpperBound ):
    Keys=[]
    x = x_init
    for i in range(NumOfKeys):
        x = x*r*(1-x)
        key = x*ScalingFactor%UpperBound
        Keys.append(key)
    print(Keys)    
    
Logistic_Keys(0.01,3.97,20,pow(10,16),256)    
    