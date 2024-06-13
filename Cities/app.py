from city import City

# create one object City: call constructor with parameters by keyword
city1 = City(name='Toulouse', population=500_000, code_postal="31_000")
# create one object City: call constructor with parameters by position
city2 = City('Lyon', 700_000, '69000')
# shared references:
city3 = city1
# copy object
city4 = City(name=city1.name, population=city1.population, code_postal=city1.code_postal)
city5 = city1.copy()
city1.population += 1_000

for city in city1, city2:
    print(city, str(city))
    print(repr(city))
    print(f"a city {city} with its str conversion.")
    print(f"a city {city!r} with its representation.")
    print(city.name, city.population, city.code_postal)
    print()

print("city1 == city2:", city1 == city2)
print("city1 != city2:", city1 == city2)
print("city1 == city3 (same ref):", city1 == city3)
print("city4 == city5 (clones):", city4 == city5)

# with @dataclass:
# TypeError: '<' not supported between instances of 'City' and 'City'
# with @dataclass(order=True)
print("city1 < city2:", city1 < city2) # False 'Toulouse' > 'Lyon'
print("city3 < city1:", city3 < city1) # False: same
print("city4 < city1:", city4 < city1) # True: name ==, pop4 < pop1
