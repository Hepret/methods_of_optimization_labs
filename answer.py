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

        return f'''Point of minimum: {self.point_of_minimum}
Minimum value: {self.minimum_value}
Total iterations: {self.iterations}
Total function calls: {self.function_calls}
Accuracy: {self.accuracy}
Last localization segment length: {self.localization_segment_length}
        '''