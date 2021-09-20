car = {
    "brand" : "Ford",
    "model" : "Mustang",
    "year" : 1964
}
car.update({"color" : "white"})
car["number"] = 100
print(car)
car.pop("model")
print(car)