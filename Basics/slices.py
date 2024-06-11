city = "Saint Etienne"
fibo_sequence = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181]

# get one element
letter = city[0]
print(letter)
print(len(city))
print(city[0], city[1], '...', city[-2], city[-1])

print(fibo_sequence[0], fibo_sequence[1], '...', fibo_sequence[-2], fibo_sequence[-1])

# set one element
# TypeError: 'str' object does not support item assignment
# city[0] = 'B'
fibo_sequence[0] = 444
print(fibo_sequence)

# get/set multiple elements with slices
city = "tOulOuSE"
print(city.title())
city_normalized = city[0].upper() + city[1:].lower()
print(city_normalized)

city = "Saint Etienne"
print(city[:2])     # 'Sa'
print(city[2:5])    # 'int'
print(city[5:8])    # ' Et'
print(city[8:])     # 'ienne'
print(city[-3:])    # 'nne'
print(city[:])      # 'Saint Etienne' (copy)
print(city[::2])    # 'SitEine'
print(city[1::2])   # 'an ten'
print(city[::-1])   # 'enneitE tniaS'

# 5 last letters except last one
print(city[-5:-1])      # 'ienn'
print(city[-2:-5])      # ''
print(city[-2:-5:-1])   # 'nne'

print(fibo_sequence[1:10])

