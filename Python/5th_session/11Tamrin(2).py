a, b, c = map(int, input('enter three numbers:').split())
max = max(a, b, c)
min = min(a, b, c)
mid = a + b + c - (min + max)

if a%2==0 and b%2==0 and c%2==0:
        print(mid)

elif max%2==1:
        print(max)
elif mid%2==1:
        print(mid)
else:
        print(min)
