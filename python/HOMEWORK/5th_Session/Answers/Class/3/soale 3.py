x = input("Type something: ")
L = len(x)
print(L)
if L%2==0:
    a = x[int((L/2))]
else:
    a = x[int(((L-1)/2))]
print(a)
