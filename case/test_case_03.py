import pytest


class TestCase:
    # 类级别的setup/teardown
    def setup_class(self):
        print('----在类执行前执行一次')

    def teardown_class(self):
        print('----在类执行后执行一次')

    # 方法级别的setup/teardown
    def setup_method(self):
        print('----在测试方法执行前执行一次')

    def teardown_method(self):
        print('----在测试方法执行后执行一次')
        print('------------------------------------------------------------------------------------------------------------')
        print('------------------------------------------------------------------------------------------------------------')
        print('------------------------------------------------------------------------------------------------------------')


    #测试方法
    def test_a(self):
        print('执行测试用例a')
        assert 1

    def test_b(self):
        print('执行测试用例b')
        assert 1


if __name__ == '__main__':
    pytest.main('-s test_case_03')