# Python Basics

print("It was coffee time")
print(12)
print(12.75)
print('Coffee', 12, 25.2)

# text is in Unicode: type=str
print("aujourd'hui")
print("je dis: \"aujourd'hui\"")
print("cœur, bientôt l'été")
print("東京")
print("parrot: 🦜")

city1 = "Toulouse"
print(city1)
print(type(city1))
city1 = "Pau"
print(city1)

# TypeError: can only concatenate str (not "int") to str
# print(city1 + 2)
print(city1 + "2")  # result: Pau2

print(city1.upper())
print(city1.lower())

# integer numbers: type=int
population = 470_000
print("population:", population)
print(type(population))
big_number = 1500000005555555555555555555555558888888888888888888888888888888888888888888888888888888888888888888888888888888888884
print(big_number + 2)

# AttributeError: 'int' object has no attribute 'upper'
# print(population.upper())

# floating numbers: type=float
speed = 49.75
print(speed, type(speed))
big_speed = 1E80
print(big_speed, type(big_speed))

# boolean: True, False   type=bool
ok = True
print(ok, True, False, type(True))

# special value to represent nothing, null, emptyness, optional
nothing=None
print("None:", None, nothing)
print("Type of None:", type(None))

# complex number
coords = 3+4j
print(coords, type(coords))
