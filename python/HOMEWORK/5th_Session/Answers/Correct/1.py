a = int(input("Enter a number: "))
b = int(input("Enter a number: "))
c = int(input("Enter a number: "))
max = max(a,b,c)
min = min(a,b,c)
mid = a + b + c - min - max
print(max,mid,min)
