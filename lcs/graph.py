from matplotlib import pyplot as plt
from random import choices
from string import ascii_uppercase
from .algorithm import Algorithm

class Graph:
    def __init__(self, algorithms: list[Algorithm]):
        self.algorithms = algorithms
    
    def add_algorithm(self, algorithm: Algorithm):
        self.algorithms.append(algorithm)

    def draw(self, linestyle = "solid", marker = None):
        for algo in self.algorithms:
            algo_result = algo.result
            X, Y = algo_result.get_XY()
            plt.plot(X, Y, label=algo.name, linestyle=linestyle, marker=marker)
            plt.xlabel("X")
            plt.ylabel("Complexity (Y)")
        
    def show(self, title = "Plot ox X | Y", save = False):
        plt.title(title)
        plt.legend()
        if save:
            plt.savefig(''.join(choices(ascii_uppercase, k=10)))
        plt.show()