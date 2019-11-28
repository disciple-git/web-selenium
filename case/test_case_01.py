import pytest


def inc(x):
    return x + 1


def test_01():
    print('执行test_01')
    assert inc(3) == 4


def test_02():
    print('执行test_02')
    assert inc(3) == 5


if __name__ == "__main__":
    pytest.main("-s test_case_01.py")