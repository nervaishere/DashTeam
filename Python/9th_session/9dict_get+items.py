car = { "brand" : "Ford", "model" : "Mustang", "year" : 1964 }

x = car.get("model")
print(x)
y = car.get("price", 15000)
print(y)
z = car.items()
print(z)