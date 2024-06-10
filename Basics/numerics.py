# operators:
# binary: + - * / // % **
# unary: + -
population = 470_000
population = population + 10_000
print(population)
print(-population)
print(+population)
print(population / 4)
print(population / 7) # resultat toujours en flottant
print(population // 7) # quotient division Euclidienne
print(population % 7) # reste/reminder/modulo
print(2**32, 2**64, 2**10, 10**3)

# int vs float
print(1+2, 1+2.0, 2.5+3.5)

# int as a binary
print(0b1101) # 1.2^3 + 1.2^2 + 0.2^1 + 1.2^0
print(0xd)

big_distance = 1E308
print(big_distance, big_distance*10)
big_distance = big_distance*10
print(big_distance / big_distance)

big_distance = float('inf')
nan_distance = float('nan')
print(big_distance, nan_distance, big_distance + nan_distance)

# ZeroDivisionError: float division by zero
# print(1.0 / 0.0)

# float: base 10 vs base 2
price = 0.1 # base 2: 0.00011001100110011001100110011..
print(price, 2*price, 3*price)

# assignment:
#   =
#   (in place binary numeric operators) += -= *= /= //= %= **=
population = 77000
population += 10
print(population)
++population # not an incrementation, just twice unary operator +
print(population)

# comparisons
print(population == 77010, population != 77010)
print(
    population < 77010,
    population <= 77010,
    population >= 77010,
    population > 77010
)
