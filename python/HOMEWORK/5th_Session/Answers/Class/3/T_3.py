a=input("Enter your Text: ")
L=len(a)
print(L)
if L%2==0:
    m=int((L/2))-1
    print(a[m])
else:
    m=int(L/2)
    print(a[m])
