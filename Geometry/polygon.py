from collections.abc import Iterable, Sized
from dataclasses import dataclass
from typing import override, Iterator

from mesurable import Mesurable2D
from point import Point
from shape import Shape


@dataclass(kw_only=True)
class Polygon(Shape, Mesurable2D, Iterable, Sized):
    vertices: tuple[Point, ...]

    @override
    def translate(self, delta_x: float, delta_y: float) -> None:
        for v in self.vertices:
            v.translate(delta_x, delta_y)

    @override
    def surface(self) -> float:
        result = 0.0
        prev = self.vertices[-1]
        for cur in self.vertices:
            result += (prev.x * cur.y) - (prev.y * cur.x)
            prev = cur
        return 0.5 * abs(result)

    @override
    def perimeter(self) -> float:
        result = 0.0
        prev = self.vertices[-1]
        for cur in self.vertices:
            result += prev.distance(cur)
            prev = cur
        return result

    def order(self) -> int:
        return len(self.vertices)

    def is_valid(self) -> bool:
        return self.order() >= 3

    def autoname(self, sep='', replace_name='?') -> None:
        self.name = sep.join((vertix.name if vertix.name else replace_name) for vertix in self.vertices)

    @override
    def __iter__(self) -> Iterator[Point]:
        return iter(self.vertices)

    @override
    def __len__(self) -> int:
        return self.order()


if __name__ == '__main__':
    p1 = Point(name="A", x=3, y=10)
    p2 = Point(name="B", x=3, y=13)
    p3 = Point(name="C", x=7, y=13)
    p4 = Point(name="D", x=7, y=10)
    p5 = Point()
    triangle_abc = Polygon(name="ABC", vertices=(p1, p2, p3))
    rectangle_abcd = Polygon(name="ABCD", vertices=(p1, p2, p3, p4))
    for poly in triangle_abc, rectangle_abcd:
        print(poly.name, '; surface:', poly.surface(), '; perimeter:', poly.perimeter())
    print(repr(triangle_abc))
    triangle_abc.translate(+1, -1)
    print(repr(triangle_abc))
    print(triangle_abc)
    poly = Polygon(vertices=(p1,p5,p3,p4))
    poly.autoname()
    print(poly)
    poly.autoname(sep='-')
    print(poly)
    poly.autoname(sep='-', replace_name='#')
    print(poly)
    poly.autoname(replace_name='_')
    print(poly)

