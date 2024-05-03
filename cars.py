mustang = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964,
}

i7 = {
  "brand": "BMW",
  "model": "i7",
  "year": 1965
}

x = {
  "brand": "Tesla",
  "model": "X",
  "year": 2020
}

cars= {
  "mustang": mustang,
  "i7": i7,
  "x": x
}

car = {}
for key, value in cars.items():
    if type(value) == type({}):
        for inner_key, inner_value in value.items():
            car[f"{key}_{inner_key}"] = inner_value
print(car)

