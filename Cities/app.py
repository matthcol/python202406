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
    print(city)
    print(city.name, city.population, city.code_postal)
    print()
