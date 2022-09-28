from math import sqrt
from typing import Callable

from answer import Answer


def golden_ratio_method(func: Callable[[float], float], a=-100, b=100, epsilon=0.0001) -> Answer:
    """
    Реализация метода
    :param func: Callable[[float], float]
    :param a: float or int
    :param b: float or int
    :param epsilon: real
    :return: Answer
    """
    u1 = a + (3 - sqrt(5)) * (b - a) / 2
    u2 = a + b - u1

    res_u1 = func(u1)
    res_u2 = func(u2)

    if res_u1 > res_u2:
        u_eval = u1
        res_u_eval = res_u1
        b = u2

    else:
        u_eval = u2
        res_u_eval = res_u2
        a = u1

    #  кол-во итераций
    iterations = 1

    # кол-во вызовов функций
    func_calls = 2

    while b - a > epsilon:

        # Вторая точка золотого сечения
        j = b + a - u_eval

        # Новые точки золотого сечения
        if (u_eval < j):
            u1 = u_eval
            res_u1 = res_u_eval
            u2 = j
            res_u2 = func(u2)

        else:
            u2 = u_eval
            res_u2 = res_u_eval
            u1 = j
            res_u1 = func(u1)

        if res_u1 < res_u2:
            u_eval = u1
            res_u_eval = res_u1
            b = u2

        else:
            u_eval = u2
            res_u_eval = res_u2
            a = u1

        iterations += 1
        func_calls += 1
    minimum_point = (b + a) / 2
    minimum_value = func(minimum_point)
    localization_segment_length = b - a
    accuracy = (3-sqrt(5)) * (b - a) / (2 ** iterations)
    return Answer(minimum_point, minimum_value, iterations, accuracy, func_calls, localization_segment_length)



