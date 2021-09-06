x = input("Enter a text: ")
x = x.split()
i=int()
for word in x:
        i+=1
        if i<len(x):
                print(word,i,end=" ")
        else:
                print(word)
print(print())