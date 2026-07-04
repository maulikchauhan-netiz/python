#dictionary pratice

car={
    "name":"bmw",
    "colour":"black",
    "number":1
}
print(type(car))
print(car["name"])
car["name"]= "audi"
print(car)
car["price"]=1000000
print(car)
car.pop("price")
print(car)
print(car.keys())
print(car.values())

#practice
marks={
    "maths":94,
    "science":80,
    "english":70

}
print(marks)