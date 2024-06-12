def square_plus_one(x):
    """
    Transform x with formula x^2 + 1

    :param x: value to transform, must be numeric
    :return: value transformed with formula
    """
    return x**2 + 1


def gcd(a: int, b: int) -> int:
    while b != 0:
        t = b
        b = a % b
        a = t
    return a


if __name__ == '__main__':
    y = square_plus_one(12)
    print(y)
    z = square_plus_one(2.5)
    print(z)


