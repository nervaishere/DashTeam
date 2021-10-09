a=float(input("enter your first number: "))
b=float(input("enter your second number: "))
c=float(input("enter your third number: "))
l=max(a,b,c)
s=min(a,b,c)
m=a+b+c-l-s
print(s , (s+m)/2 , m, sep=" ")
print(m , (m+l)/2 , l , sep=" ")

