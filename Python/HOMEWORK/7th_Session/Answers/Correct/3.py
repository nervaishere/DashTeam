a = int(input("Enter a number: "))
str_a=str(a)
m = len(str_a)
counter_even = 0
counter_less6 = 0
print(m)
for i in range(m):
    if int(str_a[i])%2==0:
        counter_even +=1
    if int(str_a[i])<6:
        counter_less6+=1
if m%2==0:
    print(counter_even)
else:
    print(counter_less6)
