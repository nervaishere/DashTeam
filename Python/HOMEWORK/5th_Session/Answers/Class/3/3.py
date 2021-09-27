text=input("enter your text:" )

print(len(text))

if len(text)%2==0:

    print(text[int((len(text)-1)/2)])

elif len(text)%2==1:

    print(text[int((len(text)/2)-0.5)])




