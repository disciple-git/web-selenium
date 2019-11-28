import random

class TestRerun:
    def test_login(self):
        print("正在登陆")
        assert 1

    def test_register(self):
        print("正在注册")
        assert 1

    def test_shopping(self):
        print('正在购物')
        i = random.randint(0,1)
        if i == 0:
            assert 0
        else:
            assert 1

