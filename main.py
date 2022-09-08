from function import function
from bisection_method import bisection_method
from golden_ratio_method import golden_ratio_method

def test_bisection_method():
    answer = bisection_method(function)
    print("Метод деления пополам")
    print("=============================================")
    print(answer)
    print("=============================================")


def test_golden_ratio_method():
    answer = golden_ratio_method(function)
    print("Метод золотого сечения")
    print("=============================================")
    print(answer)
    print("=============================================")

def main():
    test_bisection_method()
    test_golden_ratio_method()


if __name__ == "__main__":
    main()
