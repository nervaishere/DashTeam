n=int(input("enter your number: "))
m=0
p=1
if n<1:
    print("not valid")
elif n==1:
    print(0)
elif n==2:
    print(0,1)
elif n>2:
    print(0, 1, sep=" , " , end=" , ")
    for n in range(2,n):
        f=m+p
        print(f, end=" , ")
        m=p
        p=f