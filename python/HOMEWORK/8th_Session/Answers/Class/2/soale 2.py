def prime(x):
    y=[]
    for j in range(1,x+1):
        if x%j==0:
            y.append(j)
    if len(y)==2:
        return "prime"
    else:
        return "not prime"



def odd_or_even(y):
    if y%2==0:
        return "even"
    else:
        return "odd"


def sum_of_counters(z):
    s=[]
    j=0
    for k in range(1,z+1):
        if z%k==0:
            s.append(k)
    for p in s:
        j=j+p
    return j



a = int(input("Enter a number: "))
m = []
for i in range(a):
    n = int(input("Enter another number: "))
    m.append(n)


for q in m:
    print(str(q)+": "+str(prime(q))+"\n"+str(odd_or_even(q))+"\n"+str(sum_of_counters(q)))
