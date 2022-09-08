class Answer:
    def __init__(self, point_of_minimum: float, minimum_value: float, iterations: int, accuracy: float,
                 function_calls: int, localization_segment_length: float):
        self.localization_segment_length = localization_segment_length
        self.function_calls = function_calls
        self.accuracy = accuracy
        self.iterations = iterations
        self.minimum_value = minimum_value
        self.point_of_minimum = point_of_minimum

    def __str__(self):

        return f'''u* = {self.point_of_minimum}
J* = {self.minimum_value}
Количество итераций: {self.iterations}
Количество вызовов функции: { self.function_calls}
Точность вычислений: {"{:.20f}".format(self.accuracy)}
Длина последнего отрезка локализации точки минимума: {"{:.20f}".format(self.localization_segment_length)}'''