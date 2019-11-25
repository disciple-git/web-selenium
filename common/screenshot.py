import time
from selenium import webdriver


class ScreenShot:
    def __init__(self, driver):
        self.driver = driver

    def screenshot_window(self):
        t = time.strftime("%Y%m%d.%H%M%S", time.localtime())
        name = str(t)+'.png'
        self.driver.save_screenshot('D:/program/web-selenium/log/'+name)


if __name__ == '__main__':
    driver = webdriver.Chrome()
    driver.get("http://www.baidu.com")
    ScreenShot(driver).screenshot_window()