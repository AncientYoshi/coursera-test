import y57
import pytest


def test_add():
    assert y57.addition(1, 2) == 3


def test_subtract():
    assert y57.subtraction(1, 2) == -1


def test_multiply():
    assert y57.multiplication(1, 2) == 2


def test_divide():
    assert y57.division(1, 2) == 0.5


def test_power():
    assert y57.power(1, 2) == 1
    assert y57.power(2, 2) == 4
    assert y57.power(3, 2) == 9


def test_modulus():
    assert y57.modulo(1, 2) == 1
