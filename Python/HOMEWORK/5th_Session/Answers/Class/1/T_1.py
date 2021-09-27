a,b,c=map(int,input("Enter some number: ").split())
t="\t"
if max(a,b,c)==a:
    print(max(a,b,c),t,max(b,c),t,min(b,c))
elif max(a,b,c)==b: 
    print(max(a,b,c),t,max(a,c),t,min(a,c))      
else :
     print(max(a,b,c),t,max(b,a),t,min(b,a))
     
