from dataclasses import dataclass
from typing import override

from mesurable import Mesurable2D
from point import Point
from shape import Shape

@dataclass(kw_only=True)
class Polygon(Shape, Mesurable2D):
    vertices: tuple[Point,...]

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
