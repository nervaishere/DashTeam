x=int(input('enter an integer:'))
y=int(input('enter an enteger:'))

if x<=12 and(y>=0 and y<60) :
    HH=x
    MM=y
elif x<=24 and x>12:
    HH=x-12
else:
    print('notvalid')


print(HH,MM,sep=':')
