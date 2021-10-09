x = int(input("Enter a number: "))
counter=0
for number in range(1,x+1):
        if x%number == 0:
                counter+=1

if counter>2:
        print("not prime",end=" ===> (")
elif counter ==1:
        print("not prime",end=" ===> (1)\n")
else:
        print("prime",end=" ===> (1,{0})\n".format(x))

if counter>2:
        for number in range(1,x+1):
                if number<x:
                        if x%number == 0:
                                print(number,end=",")
                else:
                        print(number,end=")\n")

