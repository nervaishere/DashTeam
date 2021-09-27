x,y = map(int,input("Enter two numbers: ").split())
if x>0 and x<=24 and y>=0 and y<60 :
    if x>12:
        x -= 12
        if x<10:
            x = ('0{}'.format(x))
            x = int(x)
    if x<10:
        x = ('0{}'.format(x))
    if y<10:
        y = ('0{}'.format(y))
    print(x,y,sep=":")
else:
    print("Not Valid")
