x1, y1= map(int, input().split())
x2, y2= map(int, input().split())
x3, y3= map(int, input().split())
x4, y4= map(int, input().split())

a = ((x1-x2)**2+(y1-y2)**2)**0.5
b = ((x2-x3)**2+(y2-y3)**2)**0.5
c = ((x3-x4)**2+(y3-y4)**2)**0.5
d = ((x4-x1)**2+(y4-y1)**2)**0.5

if a==b==c==d :
    print("lozi")
elif a==c and b==d:
    print("motevazi azla")
elif a==b and c==d: 
    print("kite") 
elif a==d and b==c:
    print("kite")    
else :
    print("others")