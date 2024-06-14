from dataclasses import dataclass
from typing import override # python 3.12

from point import Point


@dataclass
class WeightedPoint(Point):
    weight: float = 1.0

    @override # python 3.12
    def __str__(self) -> str:
        return f"{super().__str__()}#{self.weight}"




if __name__ == '__main__':
    p1 = Point(x=3, y=4)
    p2 = WeightedPoint(x=7, y=7, weight=25)
    print(p1, repr(p1), sep='         ')
    print(p2, repr(p2), sep='         ')
    d1 = p1.distance(p2)
    d2 = p2.distance(p1)
    print(d1, d2)
