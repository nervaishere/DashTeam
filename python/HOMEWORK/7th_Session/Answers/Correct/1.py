n , m = map(int,input("Enter two integers as m and n: ").split())
counter = int()
for i in range(1,n+1):
    text=input()
    counter += text.count("*")

print(counter)
