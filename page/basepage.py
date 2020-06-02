import time
from selenium import webdriver
from page.get_element_by import GetElementBy
from log import logger
from selenium.webdriver.support.select import Select


class BasePage:
    def open_browser(self, *args):
        '''
        打开浏览器
        :param browser:
        :return:
        '''
        browser = args[0]
        self.driver = None
        if browser == 'Chrome':
            self.driver = webdriver.Chrome()
        else:
            self.driver = webdriver.Firefox()
        self.logger = logger.Log()

    def get_url(self, *args):
        '''
        打开网站
        :param url:
        :return:
        '''
        url = args[0]
        self.driver.get(url)
        self.driver.maximize_window()

    def get_element(self, *args):
        '''
        获取页面元素
        :param by:
        :return:
        '''
        by = args[0]
        get = GetElementBy(self.driver)
        try:
            element = get.get_element_by(by)
            return element
        except(Exception):
            self.logger.error("定位元素失败！")


    def element_send_keys(self, *args):
        '''
        在目标元素上进行输入信息操作
        :param by:
        :param value:
        :return:
        '''
        by = args[0]
        value = args[1]
        element = self.get_element(by)
        element.send_keys(value)

    def element_click(self, *args):
        '''
        在目标元素上进行点击操作
        :param by:
        :return:
        '''
        by = args[0]
        element = self.get_element(by)
        element.click()

    def change_frame(self, *args):
        '''
        选择frameset或iframe框架并切换
        :param args: framename 框架类型
                     num 目标框架序号
        '''
        value = args[0]
        framename = value.split("=")[0]
        num = value.split("=")[1]
        self.driver.switch_to.default_content()  # 每次切换框架前先切回初始层
        if framename == 'framset':
            rf = self.driver.find_elements_by_tag_name("frame")[num] #选择指定层框架
        else:
            rf = self.driver.switch_to.frame("iframe")[num]
        self.driver.switch_to.frame(rf)

    def accept_alert(self, *args):
        '''
        处理弹窗
        :return: 
        '''
        deal = args[0]
        if deal == 'accept':
            self.driver.switch_to.alert.accept()
        else:
            self.driver.switch_to.alert.dismiss()

    def sleep_time(self):
        '''
        休眠指定时间
        :param t:
        :return:
        '''
        time.sleep(3)

    def wait(self, *args):
        '''
        隐式等待
        :param args:
        :return:
        '''
        time = args[0]
        self.driver.implicitly_wait(time)
        self.logger.info("wait for %d seconds." % time)

    def choose_selector(self, *args):
        '''
        选择下拉选项
        :param args:
        :return:
        '''
        by = args[0]
        index = args[1]
        element = self.get_element(by)
        Select(element).select_by_index(index)

    def get_attribute(self, *args):
        '''
        获取元素属性
        :param args:
        :return:
        '''
        by = args[0]
        value = args[1]
        element = self.get_element(by)
        attr = element.get_attribute(value)
        return attr

    def get_text(self, *args):
        '''
        获取元素文本值
        :param args:
        :return:
        '''
        by = args[0]
        text = self.get_element(by).text()
        return text

    def close_browser(self):
        '''
        关闭浏览器
        :return:
        '''
        self.driver.close()


if __name__ == '__main__':
    print('111')