a=int(input("enter your number: "))
x=a
count=0
number=str(a)
evencount=0
while x>0:
    count+=1
    if x%2==0:
        evencount+=1
    x=x//10

if count%2==0:
    print(count, evencount, sep="\n")
newcount=0
if count%2==1:
    for i in range(0,count):
        if int(number[i])<6:
            newcount+=1
    print(count,newcount, sep="\n")
        


