size = int(input("Enter the list's size: "))
numbers = list()
for i in range(size):
    number = int(input("Enter a number: "))
    numbers.append(number)
flag = True
for x in range(3):
    for i in range(size):
        if size%2==0:
            if numbers[i]%2==0:
                print(numbers[i])
                flag = False
            elif i==size-1 and flag:
                print("@")
        else:
            if numbers[i]%2==1:
                print(numbers[i]+1)
                flag=False
                
            elif i==size-1 and flag:
                print("@")
       
        numbers[i]*=3
        numbers[i]+=1       
    print(numbers)
