import time
from selenium import webdriver
from PIL import Image
import pytesseract
from log import log


class ScreenShot:
    def __init__(self, driver):
        self.driver = driver
        self.logger = log.Log()

    def screenshot_window(self):
        t = time.strftime("%Y%m%d.%H%M%S", time.localtime())
        name = str(t)+'.png'
        try:
            self.driver.save_screenshot('D:/program/web-selenium/log/'+name)
        except:
            self.logger.error("截图失败：" + name)

    # def screenshot_element(self, element):


if __name__ == '__main__':
    '''
    driver = webdriver.Chrome()
    driver.get("http://www.baidu.com")
    ScreenShot(driver).screenshot_window()
    '''
    image = Image.open("D:\\1576164918(1).jpg")
    s = pytesseract.image_to_string(image, lang="chi_sim")
    print(s)