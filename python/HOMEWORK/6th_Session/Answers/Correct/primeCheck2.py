x = int(input("Enter a number: "))
counter =0
print("(",end="")
for number in range(1,x+1):
        if x%number==0:
                if number < x:
                        print(number,end=",")
                else:
                        print(number,end=")")
                counter+=1

if counter>2 or counter==1:
        print("/NOT prime")

else:
        print("/prime")
