from py_ecc.bn128 import bn128_curve
from curves.BN128 import BN128, Point

curve = BN128()

p = curve.multiply(Point(1, 2), 3)
print(
    p.x, p.y
)


print(bn128_curve.multiply((1, 2), 3))
