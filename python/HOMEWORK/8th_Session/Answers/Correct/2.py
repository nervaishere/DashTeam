a = int(input("Enter a number: "))
counter = 0
counter_sum = 0
for i in range(a):
    number = int(input())
    for x in range(1,number+1):
        if number%x==0:
            counter +=1
            counter_sum += x            
    print(number,": ",sep="",end="")
    if counter==2:
        print("prime")
    else:
        print("not prime")
    if number%2==0:
        print("even")
    else:
        print("odd")
    print(counter_sum)
    counter_sum , counter =0,0
