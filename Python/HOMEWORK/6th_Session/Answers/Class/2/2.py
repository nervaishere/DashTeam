hour=int(input("enter hour:" ))
minute=int(input("enter minute:" ))
newhour=hour-12
if hour>24 or hour<0 or minute<0 or minute>60 :
    print("not valid")
elif hour>11:
    print(newhour, minute, sep=":")
elif 0<hour<=11:   
    print(hour, minute, sep=":")





