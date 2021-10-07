a,b = map(int,input("Enter 2 numbers: ").split())
m = 1
c = 0
p = max(a,b)
for i in range(1,max(a,b)):
    if a%i==0 and b%i==0:
        c = i
m = int(a*b/c)
if (a%2==0 or b%2==0) and (a*b%5!=0):
    print(c)
else:
    counter =0
    max = 0
    for i in range(2,p+1):
        for x in range(1,i+1):
            if i%x==0:
                counter +=1
        if counter==2 and max<i and i!=p:
                max = i
        counter=0
    if a%5==0 and b%5==0:
        print(m)
    else:
        print(max)



