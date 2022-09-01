from function import function
from bisection_method import bisection_method


def test_bisection_method():
    answer = bisection_method(function)

    print(f"Point of minimum: {answer.point_of_minimum}")
    print(f"Minimum value: {answer.minimum_value}")
    print(f"Total iterations: {answer.iterations}")
    print(f"Total function calls: {answer.function_calls}")
    print(f"Accuracy: {answer.accuracy}")
    print(f"Last localization segment length: {answer.localization_segment_length}")


def main():
    test_bisection_method()


if __name__ == "__main__":
    main()
