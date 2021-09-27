a,b,c=map(int,input("enter 3 int:").split())
z=max(a,b,c)
x=min(a,b,c)
s=a+b+c
y=s-(z+x)

list1=list(range(x,y+1,2))


list2=list(range(y,z+1,2))

print(list1,list2,sep='\n')
    





    

