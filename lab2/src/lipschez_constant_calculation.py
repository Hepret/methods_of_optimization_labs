from typing import Callable
from function import a, b, function

m = 10000


# noinspection SpellCheckingInspection
def lipschez_constant_calculation(func: Callable[[float], float], m=m, a=a, b=b) -> float:
    # finding delta u
    delta_u = (b - a) / m

    j_u = func(a)
    j_delta_u = func(a + delta_u)

    j_der = finite_difference(j_u, j_delta_u, delta_u)

    max_j_der = j_der

    for _ in range(m):
        j_u = j_delta_u
        j_delta_u = func(a + delta_u)
        j_der = finite_difference(j_u, j_delta_u, delta_u)

        max_j_der = max(j_der, max_j_der)

    return max_j_der


def finite_difference(j_u, j_delta_u, delta_u) -> float:
    return abs(j_delta_u - j_u) / delta_u


if __name__ == "__main__":
    result = lipschez_constant_calculation(function)
    print(result)
