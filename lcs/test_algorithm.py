from .algorithm import Algorithm, AlgorithmResult

def test_cannot_instantiate_algorithm_class():
    try:
        alg = Algorithm("Test Algorithm")
        assert False
    except Exception as e:
        assert str(e) == "This is an ABSTRACT CLASS and cannot be instantiated directly"

class ExampleAlgorithm(Algorithm):
    def __init__(self):
        super().__init__("Test Algorithm")

    def execute_naive_implementation(self, input) -> AlgorithmResult | None:
        if not self.require_input_as(input, {"a": int, "b": str}):
            return None
        
        result = AlgorithmResult()
        result.add_measure(1, 2, input["b"])
        return result
    
def test_require_input_as():
    algorithm = ExampleAlgorithm()

    assert not algorithm.require_input_as({}, {"a": int})
    assert not algorithm.require_input_as({"a": 1}, {"a": str})
    assert algorithm.require_input_as({"a": 1}, {"a": int})
    assert algorithm.require_input_as({"a": 1, "b": "test"}, {"a": int, "b": str})

def test_execute():
    algorithm = ExampleAlgorithm()

    assert algorithm.execute_naive_implementation({}) is None
    assert algorithm.execute_naive_implementation({"a": 1}) is None
    expected_result = AlgorithmResult()
    expected_result.add_measure(1, 2, "test")
    result = algorithm.execute_naive_implementation({"a": 1, "b": "test"})
    assert result is not None
    assert len(result.details) == len(expected_result.details)
    for res_point, exp_point in zip(result.details, expected_result.details):
        assert (res_point.X, res_point.Y, res_point.result) == (exp_point.X, exp_point.Y, exp_point.result)

# test for AlgorithmResult class

def test_add_measure():
    result = AlgorithmResult()
    result.add_measure(1, 2, "test1")
    result.add_measure(3, 4, "test2")

    assert len(result.details) == 2
    assert (result.details[0].X, result.details[0].Y, result.details[0].result) == (1, 2, "test1")
    assert (result.details[1].X, result.details[1].Y, result.details[1].result) == (3, 4, "test2")

def test_get_XY():
    result = AlgorithmResult()
    result.add_measure(1, 2, "test1")
    result.add_measure(3, 4, "test2")

    X, Y = result.get_XY()
    assert X == [1, 3]
    assert Y == [2, 4]

def test_clear():
    result = AlgorithmResult()
    result.add_measure(1, 2, "test1")
    result.add_measure(3, 4, "test2")

    result.clear()
    assert len(result.details) == 0