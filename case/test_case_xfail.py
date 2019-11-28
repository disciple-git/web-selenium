import pytest
'''
预期失败，结果失败
预期失败，结果成功
预期成功，结果成功
预期成功，结果失败
'''


class TestXfail:
    #预期失败，结果失败
    @pytest.mark.xfail(1 > 2, reason='预期失败')
    def test_case_01(self):
        print('预期失败，结果失败')
        assert 0

    #预期失败，结果成功
    @pytest.mark.xfail(1 > 2, reason='预期失败')
    def test_case_02(self):
        print('预期失败，结果成功')
        assert 1

    #预期成功，结果成功
    @pytest.mark.xfail(1 < 2, reason='预期成功')
    def test_case_03(self):
        print('预期成功，结果成功')
        assert 1

    #预期成功，结果失败
    @pytest.mark.xfail(1 < 2, reason='预期成功')
    def test_case_04(self):
        print('预期成功，结果失败')
        assert 0

    def test_case_05(self):
        print('执行成功的用例')
        assert 1

    def test_case_06(self):
        print('执行失败的用例')
        assert 0