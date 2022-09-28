from math import sin

alpha = 9.3300
betta = 6.9770
gamma = 7.25


def function(u: float) -> float:
    """
    :param u: float
    :return: float
    """
    return alpha * sin(betta * u) - gamma * u
