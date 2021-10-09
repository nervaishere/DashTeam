a, b, c= map(int, input().split())
if a%2==0 or (b%2==0 and c%2==0):
    print('good')
else:
    print('bad')