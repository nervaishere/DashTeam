a=int(input("enter your first number:" ))
b=int(input("enter your second number:" ))
c=int(input("enter your third number:" ))
maximum=max(a,b,c)
minimum=min(a,b,c)
if a==maximum and b==minimum:
    print(a, c, b)
elif a==maximum and c==minimum:
    print(a, b, c)
elif b==maximum and a==minimum:
    print(b, c, a)
elif b==maximum and c==minimum:
    print(b, a, c)
elif c==maximum and a==minimum:
    print(c, b, a)
elif c==maximum and a==minimum:
    print(c, a , b)