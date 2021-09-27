a=int(input("Enter number of hour:"))
b=int(input("Enter number of minute:"))
if( b>=60 or a>24):
    print("The number of hour or minute is nit valid")
else:

    if a>12:
          a=a-12
          print(format(a, "0<2d"),":",format(b, "0<2d"))  
