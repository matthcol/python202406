import pytest
from maths import gcd


@pytest.mark.parametrize(
    ["a", "b", "expected_gcd"],
    [
        (1, 1, 1),
        (1, 5, 1),
        (5, 1, 1),
        (15, 22, 1),
        (15, 21, 3),
        (21, 15, 3),
    ]
)
def test_gcd(a, b, expected_gcd):
    assert expected_gcd == gcd(a, b)


# TODO: test inputs <= 0
