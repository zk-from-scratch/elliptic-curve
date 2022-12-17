from typing import Union


class FieldElement:
    field_modulus = 21888242871839275222246405745257275088696311157297823662689037894645226208583

    def __init__(self, val):
        self.val = val % self.field_modulus


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class BN128:
    # Curve is y**2 = x**3 + 3
    curve_order = 21888242871839275222246405745257275088548364400416034343698204186575808495617

    G = Point(FieldElement(1), FieldElement(2))

    @staticmethod
    def is_point_on_curve(point: Point):
        return point.y ** 2 == point.x ** 3 + 3

    @staticmethod
    def double(p):
        # Tangent to the curve
        slope = 3 * p.x ** 2 / (2 * p.y)
        x = slope ** 2 - 2 * p.x
        y = -slope * x + slope * p.x - p.y
        return Point(x, y)

    def add(self, p1: Point, p2: Point) -> Union[Point, None]:
        if p1.x == p2.x and p1.y == p2.y:
            # Tangent to curve
            return self.double(p1)

        elif p1.x == p2.x:
            # Vertical line
            return None

        else:
            # Line intersecting curve at exactly 3 points
            slope = (p2.y - p1.y) / (p2.x - p1.x)

            x = slope ** 2 - p1.x - p2.x
            y = -slope * x + slope * p1.x - p1.y

            return Point(x, y)

    def multiply(self, p: Point, n: int) -> Union[Point, None]:
        # Returns None if n = 0
        if n == 0:
            return None
        if n == 1:
            return p
        elif n % 2 == 0:
            return self.multiply(self.double(p), n // 2)
        else:
            return self.add(p, self.multiply(self.double(p), int(n // 2)))
