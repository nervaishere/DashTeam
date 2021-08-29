text = "Python"

"""
+---+---+---+---+---+---+
| P | y | t | h | o | n |  =====>length: 6
+---+---+---+---+---+---+
  0   1   2   3   4   5

"""
print(text[4])
print(text[1:4])
print(text[:5:2])
print(text[::3])

print(text[-5:5])

newtext = text * 2

"""
+---+---+---+---+---+---+---+---+---+---+---+---+
| P | y | t | h | o | n | P | y | t | h | o | n |  =====>length: ?
+---+---+---+---+---+---+---+---+---+---+---+---+
  0   1   2   3   4   5   6   7   8   9  10  11

"""
print(len(newtext))

print(newtext[-12:-1:3])

