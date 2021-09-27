a=int(input("Enter your number:"))
if a<0:
    print("not valid")
elif a==0:
    print("0") 
else:
  i=a
  for j in range(a+1):
        print("*"*j)