car_dict = {
    "make": "Tesla",
    "model": "Model X",
    "year": 2021
}
print(car_dict)

print(car_dict["make"])

car_dict = {
    "make": "Tesla",
    "model": "Model X",
    "year": 2021,
    "year": 2023
}
print(car_dict)

print(len(car_dict))

detailed_car_dict = {
    "make": "Tesla",
    "electric": True,
    "year": 2023,
    "features": ["autopilot", "sunroof", "heated seats"]
}

x = car_dict["model"]

x = car_dict.get("model")

x = car_dict.keys()

vehicle = {
    "make": "Tesla",
    "model": "Model 3",
    "year": 2022
}

x = vehicle.keys()
print(x)

vehicle["color"] = "black"
print(x)

vehicle["year"] = 2025
vehicle.update({"year": 2026})
vehicle.update({"trim": "Performance"})

vehicle.pop("model")
print(vehicle)

for key, value in vehicle.items():
    print(key, value)
