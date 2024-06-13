from dataclasses import dataclass
from typing import override

from mesurable import Mesurable1D
from point import Point
from shape import Shape


@dataclass(kw_only=True)
class Segment(Shape, Mesurable1D):
    ends: tuple[Point, Point]

    @override
    def translate(self, delta_x: float, delta_y: float) -> None:
        for end in self.ends:
            end.translate(delta_x, delta_y)

    @override
    def length(self) -> float:
        return self.ends[0].distance(self.ends[1])


if __name__ == '__main__':
    p1 = Point(x=3, y=4)
    p2 = Point(x=21, y=25)
    s = Segment(ends=(p1,p2))
    print(s)
    s.translate(+1,-1)
    print(s)