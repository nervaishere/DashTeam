x=float(input("enter your first number: "))
y=float(input("enter your second number: "))
#x="{0:.3f}".format(x)
#y="{0:.3f}".format(y)
#با وجود این قسمت برنامه کار نمیکند،اما نمیفهمم چرا
z=x
t=y
count_x=0
count_y=0
while z>0:
    count_x=count_x+1
    z=z//10
while t>0:
    count_y=count_y+1
    t=t//10

if count_x>3 and x%5==0:
    x=round(x,-1)

if count_y>3 and y%5==0:
    y=round(y,-1)

print(x , "*" , y)






