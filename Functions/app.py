from maths import square_plus_one, gcd
from textgame import is_palindrome

x = 12
y = square_plus_one(x)
print(y)

x = 15
y = 21
c = gcd(x, y)
print(c)

c2 = gcd(21, 15)
c3 = gcd(a=21, b=15)
c4 = gcd(a=x, b=y)
c5 = gcd(15, b=22)
print(c2, c3, c4, c5)

# incorrect calls
# TypeError: gcd() missing 2 required positional arguments: 'a' and 'b'
# c6 = gcd()
# TypeError: gcd() missing 1 required positional argument: 'b'
# c6 = gcd(15)
# TypeError: unsupported operand type(s) for %: 'int' and 'str'
# c6 = gcd(15, "21") # typing error by pycharm, mypy, ...
# TypeError: gcd() takes 2 positional arguments but 3 were given
# c6 = gcd(15, 21, 33)
# SyntaxError: positional argument follows keyword argument
# c5 = gcd(a=15, 22)
# TypeError: gcd() got multiple values for argument 'a'
# c5 = gcd(15, a=22)

for word in "kayak", "Kayak", "python", "a", "":
    print(word, 'is a palindrome (ci):', is_palindrome(word))
    print(word, 'is a palindrome (cs):', is_palindrome(word, case=True))

