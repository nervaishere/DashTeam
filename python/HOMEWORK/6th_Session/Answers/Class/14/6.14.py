a,b,c,d=map(int,input("enter 4 nums:").split())

if (5<=a<10 and 5<=b<10 and 5<=c<10 and 5<=d<10):
    print(1,2,3,4,5,6,7,8,9,10)
if(a>10 and b>10) or (a>10 and c>10) or (a>10 and d>10) or (b>10 and c>10) or (b>10 and d>10) or (c>10 and d>10) or (a>10 and b>10 and c>10) or (a>10 and b>10 and d>10) or (b>10 and c>10 and d>10) or( a>10 and c>10 and d>10) or (a>10 and b>10 and c>10 and d>10):
    print(10,12,14,16,18)
elif (a>10 and b>10 and c>10 and d>10) or (a%2==0) or (b%2==0) or (c%2==0) or (d%2==0) or (a%2==0 and b%2==0) or (a%2==0 and c%2==0) or (a%2==0 and d%2==0) or (b%2==0 and c%2==0) or (b%2==0 and d%2==0) or (c%2==0 and d%2==0) or (a%2==0 and b%2==0 and c%2==0) or (a%2==0 and b%2==0 and d%2==0) or (b%2==0 and c%2==0 and d%2==0) or(a%2==0 and c%2==0 and d%2==0) or (a%2==0 and b%2==0 and c%2==0 and d%2==0):
    print("****")
else:
    print(":(")


 
    
