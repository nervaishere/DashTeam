x = int(input("Enter a number: "))
reverse=int()
while x>0:
    rem = x % 10
    reverse = reverse * 10 + rem
    x//=10

print(reverse)