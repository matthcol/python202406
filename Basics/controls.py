population = 177000

if population < 100000:
    # block if condition is True
    print("small city")
else:
    # block else: condition is False
    print("big city")
# end if

# for "foreach" accepts Iterable objects
for i in range(1000):
    print("Spam")
# end for

# list of str (homogeneous)
cities = ["Toulouse", "Pau", "Lyon", "Valence"]
print(len(cities), cities)
cities.append("Saint Etienne")
print(len(cities), cities)
# try: extend, insert, remove, sort
cities.extend(["Paris", "Marseille"])
print(len(cities), cities)
cities.insert(2, "Lille")
print(len(cities), cities)
cities.remove("Pau")
print(len(cities), cities)
cities.sort()
print(len(cities), cities)
for city in cities:
    print(city, city.upper(), city.isalpha())
print("The End")

