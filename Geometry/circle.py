import math
from collections.abc import Container
from dataclasses import dataclass
from typing import override

from mesurable import Mesurable2D
from point import Point
from shape import Shape


@dataclass(kw_only=True)
class Circle(Shape, Mesurable2D, Container):

    radius: float = 1.0
    center: Point

    @override
    def translate(self, delta_x: float, delta_y: float) -> None:
        self.center.translate(delta_x, delta_y)

    @override
    def surface(self) -> float:
        return math.pi * self.radius**2

    @override
    def perimeter(self) -> float:
        return math.pi*2*self.radius

    def diameter(self):
        return 2*self.radius

    @override
    def __contains__(self, o) -> bool:
        if not isinstance(o, Point):
            return False
        return self.center.distance(o) <= self.radius


if __name__ == '__main__':
    p1 = Point(name="A", x=6.5, y=0.75)
    p2 = Point(name="A", x=8.5, y=0.75)
    p3 = Point(name="A", x=17.5, y=0.75)
    circle1 = Circle(name="C1", radius=10.0, center=p1)
    circle2 = Circle(center=p1)
    for c in circle1, circle2:
        print(c)
        print(repr(c))
        print(c.name, c.radius, c.center.name)

    print(p2, "inside", circle1, ":", p2 in circle1)
    print(p1, "inside", circle1, ":", p3 in circle1)
    circle1.translate(+1, -1)
    print(circle1)



