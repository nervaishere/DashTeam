a, b, c = map(int,input("Enter three numbers: ").split())
if (a>b and b<c) or (a<b and a>c):
    x = a
elif (b>a and b<c) or (b<a and b>c):
    x = b
else:
    x = c
for i in range(x-4,x+1,2):
    print(i,end=" ")
print()
for j in range(x,x+5,2):
    print(j,end=" ")
print()
