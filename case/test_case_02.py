import pytest


#函数级别的setup/teardown
def setup_function():
    print('在测试用例前执行')

def teardown_function():
    print('在测试用例后执行')


#模块级别的setup/teardown
def setup_module():
    print('。。。。。在模块运行前执行')


def teardown_module():
    print('。。。。。在模块运行后执行')


def inc(x):
    return x + 1


def test_01():
    print('执行test_01')
    assert inc(3) == 4


def test_02():
    print('执行test_02')
    assert inc(3) == 5


if __name__ == '__main__':
    pytest.main('-s test_case_02.py')









