from abc import abstractmethod
import math

class OperatorBase:
    @abstractmethod
    def eval(num_1: float, num_2: float) -> float: raise NotImplementedError

class Plus:
    pass

def plus(num_1: float, num_2: float) -> float:
    return num_1 + num_2

def minus(num_1: float, num_2: float) -> float:
    return num_1 - num_2

def product(num_1: float, num_2: float) -> float:
    return num_1 * num_2

def power(num_1: float, num_2: float) -> float:
    return num_1 ** num_2

def root(num_1: float, num_2: float) -> float:
    return num_1 ** (1 / num_2)

def log(num_1: float, num_2: float) -> float:
    return math.log(num_1, num_2)