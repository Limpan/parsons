import pytest
from parsons.core import ParsonsProblem


def fun_test():
    pass


def test_parsons():
    rv = ParsonsProblem(fun_test)
    assert rv == ['pass']
