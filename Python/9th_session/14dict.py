thisdict =  {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
for x in thisdict:
    print(x)
print('*****')
for y in thisdict:
    print(thisdict[y])
print('*****')
for y in thisdict.values():
    print(y)
print('*****')
for z in thisdict.keys():
    print(z)
print('*****')
for key , value in thisdict.items():
    print(key, value)