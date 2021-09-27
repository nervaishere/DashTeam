x=input("enter your text:")
y=len(x)
print(y)
if y%2==0:
    print(x[int(y/2)])
else:
    print(x[int((y-1)/2)])
          
