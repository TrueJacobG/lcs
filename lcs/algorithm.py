class DataPoint:
    def __init__(self, x: int, y: int, result: str):
            self.X = x
            self.Y = y
            self.result = result

class AlgorithmResult:
    def __init__(self):
        self.details: list[DataPoint] = []

    def add_measure(self, x: int, y: int, result: str):
        self.details.append(DataPoint(x, y, result))

    def clear(self):
        self.details = []

    def get_XY(self):
        X = [point.X for point in self.details]
        Y = [point.Y for point in self.details]
        return X, Y

class Algorithm:
    def __init__(self, name):
        if type(self) is Algorithm:
            raise Exception("This is an ABSTRACT CLASS and cannot be instantiated directly")

        self.name = name
        self.result = AlgorithmResult()

    def execute(self, input) -> AlgorithmResult | None:
        raise NotImplementedError("This is an ABSTRACT METHOD and must be implemented in subclass")

    def require_input_as(self, input: dict, scheme: dict) -> bool:
        for key in scheme:
            if key not in input:
                print(f"Missing key in input: {key}")
                return False
            if type(input[key]) is not scheme[key]:
                print(f"Incorrect type for key '{key}': expected {scheme[key]}, got {type(input[key])}")
                return False
        return True
        