for i in range(10):
    name , lastname , age = map(str,input("Enter user's information: ").split())
    age = int(age)
    if age>=18:
        print(name,lastname,age)
