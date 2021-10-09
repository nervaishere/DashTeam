n = int(input("Enter n:"))
Prime = True
for i in (2, n // 2+ 1):
 if n % i == 0:
   Prime = False
   break
if (Prime == True):
   print("Prime")
else:
   print("No prime")
