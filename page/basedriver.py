import time
from selenium import webdriver
from page.get_element_by import GetElementBy


class BaseDriver:
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
        element = get.get_element_by(by)
        return element

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

    def close_browser(self):
        '''
        关闭浏览器
        :return:
        '''
        self.driver.close()


if __name__ == '__main__':
    print('111')