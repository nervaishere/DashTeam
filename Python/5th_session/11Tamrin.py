a, b, c=map(int, input('enter three numbers:').split())
x=max(a,b,c)
y=min(a,b,c)
if a%2==0 and b%2==0 and c%2==0:
    if (x==a and y==c) or (x==c and y==a):
        print(b)
    elif (x==b and y==c) or (x==c and y==b):
        print(a)
    elif (x==a and y==b) or (x==b and y==a):
        print(c)
else:
    if a%2==1 and b%2==1 and c%2==1:
        print(x)
    elif a%2==0:
        if max(b,c)%2==0:
            print(min(b,c))
        else:
            print(max(b,c))
    elif b%2==0:
        if max(a,c)%2==0:
            print(min(a,c))
        else:
            print(max(a,c))
    else:
        print(c)