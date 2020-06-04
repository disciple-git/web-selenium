import os
import logging
import time


class Logger:
    def __init__(self):
        self.logname = "mylog"

    def setMSG(self, level, msg):
        logger = logging.getLogger()

        # 创建日志名称。
        rq = time.strftime('%Y%m%d', time.localtime(time.time()))

        # os.getcwd()获取当前文件的路径，os.path.dirname()获取指定文件路径的上级路径
        path_dir = os.path.dirname(__file__)
        log_path = os.path.abspath(os.path.dirname(path_dir)) + '/log'
        log_name = os.path.join(log_path, rq + '.log')

        # 定义Handler输出到文件和控制台
        fh = logging.FileHandler(log_name)
        ch = logging.StreamHandler()
        # 定义日志输出格式
        formater = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        fh.setFormatter(formater)
        ch.setFormatter(formater)
        # 添加Handler
        logger.addHandler(fh)
        logger.addHandler(ch)
        # 添加日志信息，输出INFO级别的信息
        logger.setLevel(logging.INFO)

        if level == 'debug':
            logger.debug(msg)
        elif level == 'info':
            logger.info(msg)
        elif level == 'warning':
            logger.warning(msg)
        elif level == 'error':
            logger.error(msg)

        # 移除句柄，否则日志会重复输出
        logger.removeHandler(fh)
        logger.removeHandler(ch)
        fh.close()

    def debug(self, msg):
        self.setMSG('debug', msg)

    def info(self, msg):
        self.setMSG('info', msg)

    def warning(self, msg):
        self.setMSG('warning', msg)

    def error(self, msg):
        self.setMSG('error', msg)


if __name__ == '__main__':
    Logger().info("这是一条信息")
