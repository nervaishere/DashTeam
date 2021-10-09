def fib(num):
    if num==0 or num==1:
        return 1
    else:
        return fib(num-1)+fib(num-2)

i = int(input("Enter a number: (STARTS FROM ZERO)"))
if i==0:
    print(str(i+1)+"st:",fib(i))
elif i==1:
    print(str(i+1)+"nd:",fib(i))
elif i==3:
    print(str(i+1)+"rd:",fib(i))
else:
    print(str(i+1)+"th:",fib(i))
