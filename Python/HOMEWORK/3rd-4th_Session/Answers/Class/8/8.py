completename= input("enter your complete name:" )
age= int(input("enter your age:" ))
month= input("enter your birth month:" )
day= input("enter your birth day:" )
year= int(100-age)
sentence="hello {0}, you're {1} years old and your birthdate is: {2}/{3}/{4}"
print(sentence.format(completename, age, year, month, day))