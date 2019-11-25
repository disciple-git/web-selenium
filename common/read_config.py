from configparser import ConfigParser
import os


class ReadConfig:
    def __init__(self, filename='path.ini'):
        root_path = os.path.abspath('..')+'/config/'
        self.cp = ConfigParser()
        self.cp.read(root_path+filename)

    def get_db(self, section, key):
        '''
        获取配置文件对应键的值
        :param section: section名字
        :param key: 键名
        :return: 目标值
        '''
        value = self.cp.get(section, key)
        return value


if __name__ == '__main__':
    print('1111')
