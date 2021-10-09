a=int(input("a:"))
b=int(input("b:"))
c=int(input("c:"))
d=int(input("d:"))
e=int(input("e:"))
thislist=[a,b,c,d,e]
for i in range(0,5):
    thislist[i]=i+thislist[i]

print(thislist)


    

