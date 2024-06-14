from point import Point
from circle import Circle
from mesurable import Mesurable2D, Mesurable1D
from polygon import Polygon
from segment import Segment
from shape import Shape
from weightedpoint import WeightedPoint

if __name__ == '__main__':
    shapes: list[Shape] = [
        Point(name='A', x=3, y=4),
        Circle(name="C1", center=Point(), radius=10),
        Polygon(vertices=(
            Point(x=3, y=3),
            Point(x=3, y=7),
            Point(x=6, y=7),
        )),
        WeightedPoint(),
        Segment(
            name="EF",
            ends=(
                Point(x=3, y=3),
                Point(x=3, y=10)
        )),
    ]
    for shape in shapes:
        print("shape (str):", shape)
        print("shape (repr):", repr(shape))
        print("name:", shape.name)
        match shape:
            case Mesurable2D() as m2:
                print("Mesurable 2D: surface =", m2.surface(), "; perimeter:", m2.perimeter())
            case Mesurable1D() as m1:
                print("Mesurable 1D: length =", m1.length())
            case _:
                print("not a mesurable shape")
        print()