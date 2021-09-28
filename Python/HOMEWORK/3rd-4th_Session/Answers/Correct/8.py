fname = input("Enter your first-name: ")
lname = input("Enter your last-name: ")
age = int(input("How old are you? "))
month = int(input("Enter you birth month as a number: "))
day = int(input("Enter you birthdate day: "))
Bdy = (1400 - age)%100
print("Hello {0}{1},you're {2} years old and your birthdate is:\n{3}/{4}/{5}".format(fname,lname,age,Bdy,month,day))

