import pytest

from app.calc import Calculator

class TestCalc:
    def setup(self):
         self.calc = Calculator
    def test_adding_success(self):
        assert self.calc.adding(self, 1, 1) == 2

    def test_adding_success(self):
        assert self.calc.adding(self, 5, 5) == 10

    def test_subtraction(self):
        assert self.calc.subtraction(self, 10, 10) == 0

    def test_division(self):
        assert self.calc.division(self, 25, 5) == 5

    def test_multiply(self):
        assert self.calc.multiply(self, 3, 3) == 9

    def test_adding_unseccess(self):
        assert self.calc.adding(self, 1, 1) == 3

    def test_zero_devision(self):
        with pytest.raises(ZeroDivisionError):
            self.calc.division(self, 1, 0)

    def teardown(self):
        print('Выполнение метода Teardown')




