import math
from dataclasses import dataclass
from typing import Self, override

from shape import Shape


@dataclass(kw_only=True, order=True)
class Point(Shape):
    x: float = 0.0
    y: float = 0.0

    @override
    def __str__(self) -> str:
        return f"{self.name + ' ' if self.name else ''}({self.x:0.3f}, {self.y:0.3f})"

    def distance(self, other: Self) -> float:
        return math.hypot(self.x - other.x, self.y - other.y)

    @override
    def translate(self, delta_x: float, delta_y: float) -> None:
        self.x += delta_x
        self.y += delta_y


if __name__ == '__main__':
    p1 = Point()
    p2 = Point(x=3.5, y=4.75)
    p3 = Point(name="A", x=6.5, y=0.75)
    for p in p1, p2, p3:
        print(p, repr(p), p.x, p.y, p.name)

    d = p2.distance(p3)
    print("distance:", d)
    p3.translate(+1, -1)
    print(p3)
