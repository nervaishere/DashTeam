a = int(input("Enter a number: "))
b = int(input("Enter another number: "))
c = int(input("Enter another number: "))
if a>=b and a>=c:
    if b>=c:
        x = a,b,c
    else:
        x = a,c,b
elif b>=a and b>=c:
    if a>=c:
        x = b,a,c
    else:
        x = b,c,a
else:
    if a>=b:
        x = c,a,b
    else:
        x = c,b,a

print(x)
