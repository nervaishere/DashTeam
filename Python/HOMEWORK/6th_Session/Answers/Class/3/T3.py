a=float(input("Enter your number:"))
print(format(a,".3f"),end="\\")
if (a<0 and (-1*a)<10):
    print(format(a))
elif(a<0 and (-1*a)>10):
    print("-50")    
elif(a>0 and a<10):
    print(format(a))
else:
    print("+50")