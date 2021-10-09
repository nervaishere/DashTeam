x = int(input("Enter a number: "))
if x>=0:
    if x==0:
        print("0")
    else:
        for x in range(0,x):
            count = 0
            while count <= x:
                print('*', end =' ')
                count = count+1
            print()
else:
    print("not valid")

