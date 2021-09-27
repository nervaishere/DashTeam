a,b,c=map(int,input("Enter your number:").split())
S1=min(a,b,c)
S2=max(a,b,c)
S3=(a+b+c)-(S1+S2)
f=S1
while f<=S3:
    print(f,end=" ")
    f+=2
print()
j=S3
while j<=S2:
    print(j,end=" ")
    j+=2
print()    


