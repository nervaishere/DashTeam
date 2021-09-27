x=int(input("enter your number:" ))
z=x
count=0
while z>0:
    count=count+1
    z=z//10
newcount=count-1
j=x
y=0
while newcount>=0:
    n=j%10
    y=y+(n*(10**newcount))
    newcount=newcount-1
    j=j//10

print(y)
    
