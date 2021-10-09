x=int(input("enter your number: "))
i=1
if x<0:
    print("not valid")
if x==0:
    print(0)
if x>0:
    for i in range(1,x+1):
        print("*"*i)

print()