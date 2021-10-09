x=int(input("enter your number: "))
n=2
j=x
list_c=[1]
value=0
for n in range(2,x+1):
    if j%n==0:
        value=1
        list_c.append(n)
        n=n+1
list_p=[1,x]
if x==1:
    print("not prime ==> " , [1])
elif value==1:
    print("not prime ==> " , list_c)
elif value==0:
    print("prime ==> " ,  list_p)
    
        



