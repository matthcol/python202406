import math
from dataclasses import dataclass
from typing import Self, override

from shape import Shape


@dataclass(kw_only=True, order=True)
class Point(Shape):  # inherits from class object
    x: float = 0.0
    y: float = 0.0

    @override
    def __str__(self) -> str:
        return f"({self.x:0.3f}, {self.y:0.3f})"

    @override
    def translate(self, delta_x: float, delta_y: float) -> None:
        self.x += delta_x
        self.y += delta_y

    def distance(self, other: 'Point') -> float:
        return math.hypot(self.x - other.x, self.y - other.y)


if __name__ == '__main__':
    p1 = Point()
    p2 = Point(x=3.5, y=4.75)
    p3 = Point(name="A", x=6.5, y=0.75)
    for p in p1, p2, p3:
        print(p, repr(p), p.x, p.y)

    d = p2.distance(p3)
    print("distance:", d)
    print(p3)
