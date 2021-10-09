myList=[10,20,25,30,35,40,50]
def mod(myList):
   for i in myList:
           if(i%10==0):
                   yield i
for i in mod(myList):
   print(i)

