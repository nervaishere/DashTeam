text=input("enter your text: ")
count=0
for i in text:
    if i==" ":
        count+=1
x=0
for j in range(1,count+1):
    newtext=text.replace(" ", x )
    x+=1

print(newtext)



