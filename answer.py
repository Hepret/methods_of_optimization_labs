class Answer:
    def __init__(self, minimum_point: float, minimum_value: float, iterations: int, accuracy: float,
                 function_calls: int, localization_segment_length: float):
        self.localization_segment_length = localization_segment_length
        self.function_calls = function_calls
        self.accuracy = accuracy
        self.iterations = iterations
        self.minimum_value = minimum_value
        self.minimum_point = minimum_point

