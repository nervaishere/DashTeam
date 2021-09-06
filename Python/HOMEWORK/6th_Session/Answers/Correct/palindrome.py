x = int(input("Enter a number: "))
str_x= str(x)
len_x = len(str_x)
i = 0
while len_x>1:
        if str_x[i]==str_x[len_x-1-i] and i<=len_x/2 :
                pass
        else:
                print("not a palindrome")
                break
        i+=1
        if i==len_x/2:
                print("a palindrome")
                break

