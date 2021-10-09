x = float(input("Enter a number: "))
if x<0:
    z = (-1)*x
else:
    z = x
print(format(z,".3f"),end="\\")
if x > 10:
    print("{:+f}".format(+50))
elif x < -10:
    print("{:+f}".format(-50))
else:
    print("{:+f}".format(x))
