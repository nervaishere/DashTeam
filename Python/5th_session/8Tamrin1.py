a, b, c= map(int, input().split())
if c>0:
    s=a-b
    if s>0:
        print(s)
    else:
        print(-1*s)
elif c==0:
    print(a+b)
else:
    print(a*b)