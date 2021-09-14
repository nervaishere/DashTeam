x = input()
x = x.split()
counter = int()

for word in x:
       for letter in word:
               if letter in "AEIOUaeiou":
                       counter+=1

print("your input has {} vowels".format(counter))

