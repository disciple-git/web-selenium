import logging
import time
import os


class WriteLog:
    def __init__(self):
        self.logger = logging.getLogger()  # 实例化logger对象
        self.logger.setLevel(logging.DEBUG)
        # 设置存储日志的文件名
        date = time.strftime('%Y-%m-%d')
        self.filename = os.path.dirname(os.path.abspath('.')) + '\\log\\' + date + '.log'
        # 定义handler的输出格式
        self.formatter = logging.Formatter('%(asctime)s - %(levelname)s -%(pathname)s-%(lineno)d'+'行'+'- %(message)s')

    def getlogger(self):
        fh = logging.FileHandler(self.filename, encoding='utf-8')
        fh.setFormatter(self.formatter)
        # 将handlers 添加到 logger
        self.logger.addHandler(fh)
        return self.logger


if __name__ == '__main__':
    logger = WriteLog().getlogger()
    logger.info('测试info日志')
    logger.error('这里是一个ERROR')