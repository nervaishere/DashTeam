a, b, c, d, e = map(int,input("Enter 5 numbers: ").split())
numbers = [a,b,c,d,e]
for i in range(len(numbers)):
    numbers[i]+=i

print(numbers)
