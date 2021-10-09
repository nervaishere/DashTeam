x = int(input("Enter a number: "))
first = 0
second = 1
third = 0
i = 0
while x > i:
        i+=1
        if x==1:
                print(first)
                break
        elif x==2:
                print(second)
                break
        else:
                third = first + second
                first = second
                second = third
        if i==x-2:
                print(third)

