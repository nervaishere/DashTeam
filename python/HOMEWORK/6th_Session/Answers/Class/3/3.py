x=float(input("enter your number:" ))
a=abs(x)
z="{0:.3f}".format(a)
if abs(x)>10 and x>=0:
    print(z , 10 ,sep="\\")
elif abs(x)>10 and x<0:
    print(z , -10 , sep="\\")
elif abs(x)<10 and x>=0:
    print(z , x , sep="\\")
elif abs(x)<10 and x<0:
    print(z , x , sep="\\")


 


