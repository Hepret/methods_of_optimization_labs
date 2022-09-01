from math import pow, atan

a = -0.9
b = 2.5


def function(u: float) -> float:
    """
    :param u: float
    :return: float
    """
    return pow(u, 4) + a * atan(b * u)
