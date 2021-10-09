a,b=map(float,input('enter 2 nums:').split())

x=len(str(a))
y=len(str(b))

if a%5==0 and b%5==0 and x>4 and y>4:
    print(round(a,-1),round(b,-1),sep="*")
else:
    print(format(a,".3f"),end="*")
    print(format(b,".3f")) 
    
