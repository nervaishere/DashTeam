x = input("Enter your text: ")
i = int()
for letter in x:
        #print(letter,end=",")
        if letter in "AEIUOaeiou" :
                i+=1

print("There is {0} vowels in your text".format(i))