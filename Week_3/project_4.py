import math
from typing import Tuple

__all__ = ["solve_cubic", "solve_monic_cubic", "solve_depressed_cubic"]


def solve_cubic(a: float, b: float, c: float, d: float) -> Tuple[float, ...]:
    """Returns the real solutions to a * x ** 3 + b * x ** 2 + c * x + d == 0"""

    return solve_monic_cubic(b / a, c / a, d / a)


def solve_monic_cubic(b: float, c: float, d: float) -> Tuple[float, ...]:
    """Returns the real solutions to x ** 3 + b * x ** 2 + c * x + d == 0"""

    p = c - b ** 2 / 3
    q = d - b * c / 3 + b ** 3 * 2 / 27

    return tuple(t - b / 3 for t in solve_depressed_cubic(p, q))


def cbrt(x: float, /) -> float:
    return math.copysign(abs(x) ** (1 / 3), x)


def solve_depressed_cubic(p: float, q: float) -> Tuple[float, ...]:
    """Returns the real solutions to x ** 3 + p * x + q == 0"""

    if p == 0:
        return (-cbrt(q),)

    d = p ** 3 / 27 + q ** 2 / 4

    if d > 0:
        r = -q / 2
        s = math.sqrt(d)

        return (cbrt(r + s) + cbrt(r - s),)

    r = 3 * q / p

    if d == 0:
        return r, -r / 2

    s = math.acos(r / 2 * math.sqrt(-3 / p)) / 3
    t = 2 * math.sqrt(-p / 3)
    u = 2 * math.pi / 3

    return tuple(t * math.cos(s - u * k) for k in range(3))