from math import pow, atan

a = -1.1
b = 2.0


def function(u: float) -> float:
    """
    :param u: float
    :return: float
    """
    return pow(u, 4) + a * atan(b * u)
