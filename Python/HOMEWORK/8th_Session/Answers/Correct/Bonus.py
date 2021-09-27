a,b,c,d,e,f,g,h,i,j = map(int,input().split())
numbers = [a,b,c,d,e,f,g,h,i,j]


avg = int()
temp = int()
for i in range(len(numbers)):
    for j in range(i+1,len(numbers)):
        if numbers[j]>numbers[i]:
            temp = numbers[i]
            numbers[i]=numbers[j]
            numbers[j]=temp

    avg += numbers[i]
avg/=len(numbers)
avg = int(avg)
counter = 1
common = 0
for i in range(len(numbers)-1):
    for j in range(i+1,len(numbers)):
        if numbers[j]==numbers[i]:
            common = numbers[j]
            counter+=1
        if counter>1 and common==numbers[j]:
            break
        
if counter==1:
    common=0
    counter=0
print(counter)
print("{0}\\ {1}:{2}\\ {3}".format(numbers,common,counter,avg))

   

