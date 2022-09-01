from typing import Callable

from answer import Answer


def bisection_method(func: Callable[[float], float], a=-100, b=100, epsilon=0.0001) -> Answer:
    """
    Метод деления пополам
    :param func: Callable[[float], float]
    :param a: float or int
    :param b: float or int
    :param epsilon: real
    :return: Answer
    """
    delta = epsilon

    iterations = 0

    while b - a < epsilon:
        u1 = (b - a - delta) / 2
        u2 = (b - a + delta) / 2

        if func(u1) > func(u2):
            b = u2
        else:
            a = u1

        iterations += 1

    minimum_point = (b + a) / 2
    minimum_value = func(minimum_point)
    func_calls = iterations * 2 + 1
    localization_segment_length = b - a

    return Answer(minimum_point, minimum_value, iterations, epsilon, func_calls, localization_segment_length)