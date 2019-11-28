import pytest


class TestSkip:
    @pytest.mark.skipif(2 > 1, reason='条件为真跳过测试')
    def test_skip_01(self):
        print('测试跳过方法')
        assert 2 > 1

    @pytest.mark.skipif(2 < 1, reason='条件为真跳过测试')
    def test_skip_02(self):
        print('跳过测试方法')
        assert 1












