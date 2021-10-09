x=int(input('enter an integer:'))

if x==1:
        print('not prime')
elif x>1 or x<-1:
    for i in range (2,x):
        if x%i==0:
            print('prime')
else:
    print('not prime')
