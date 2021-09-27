x=float(input("enter your first number:"))
y=float(input("enter your second number:"))
z=float(input("enter your third number:"))
t=float(input("enter your fourth number:"))
list=[x,y,z,t]
count=0
value=0
for i in list:
    if i>10:
        count=count+1
for i in list:
    if i%2==0:
        break
    value=1

if 5<x<10 and 5<y<10 and 5<z<10 and 5<t<10 and value==0:
    print("1,2,3,4,5,6,7,8,9,10")
elif 1<count<4 and value==0:
    print("10,12,14,16,18")
elif count==4 or value==1:
    print("****")
else:
    print(":(")

#در مثال ها 1و2و3و4 آورده شده بود که در شرط سوم صدق میکنند پس در برنامه من برعکس خروجی مثال، خروجی **** است
