x , y , z = map(int,input().split())
min = min(x,y,z)
max = max(x,y,z)
mid = x + y + z - max - min

for number in range(min,mid,2):
        print(number,end=" ")
        
print()
for number in range(mid,max,2):
        print(number,end=" ")

