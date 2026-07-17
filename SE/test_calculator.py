"""
Lab: Unit Testing with PyTest
Course: Software Engineering (24PCA402)

Task: Write unit tests for the Calculator class below, covering
normal cases, edge cases, and error conditions.

Run with:  pytest test_calculator.py -v
"""

import pytest


class Calculator:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        if b == 0:
            raise ZeroDivisionError("Cannot divide by zero")
        return a / b


@pytest.fixture
def calc():
    return Calculator()


def test_add(calc):
    assert calc.add(2, 3) == 5
    assert calc.add(-2, 2) == 0


def test_subtract(calc):
    assert calc.subtract(10, 4) == 6


def test_multiply(calc):
    assert calc.multiply(3, 4) == 12
    assert calc.multiply(-3, 4) == -12


def test_divide(calc):
    assert calc.divide(10, 2) == 5


def test_divide_by_zero_raises(calc):
    with pytest.raises(ZeroDivisionError):
        calc.divide(10, 0)


@pytest.mark.parametrize("a, b, expected", [
    (0, 0, 0),
    (-1, -1, -2),
    (1_000_000, 1, 1_000_001),
])
def test_add_edge_cases(calc, a, b, expected):
    assert calc.add(a, b) == expected
