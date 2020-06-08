from PIL import Image
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import cv2
import numpy as np
from io import BytesIO
import time
import requests


class CrackSlider():
    """
    通过浏览器截图，识别验证码中缺口位置，获取需要滑动距离，并模仿人类行为破解滑动验证码
    """
    def __init__(self):
        self.url = 'http://cc.163.com/'
        self.driver = webdriver.Chrome()
        self.wait = WebDriverWait(self.driver, 10)
        self.zoom = 1

    def open(self):
        self.driver.maximize_window()
        self.driver.get("http://cc.163.com/")
        self.driver.implicitly_wait(10)
        if self.driver.find_element_by_id("login"):
            self.driver.find_element_by_xpath("//*[@id='login']/a[1]/span").click()
        rf = self.driver.find_elements_by_tag_name("iframe")[0] # 选择指定层框架
        self.driver.switch_to.frame(rf)
        self.driver.implicitly_wait(10)
        self.driver.find_element_by_name("email").clear()
        self.driver.find_element_by_name("email").send_keys("m13530658357@163.com")
        self.driver.find_element_by_name("password").send_keys("nlf3141592653")

    def get_pic(self):
        time.sleep(2)
        target = self.wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'yidun_bg-img')))
        template = self.wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'yidun_jigsaw')))
        target_link = target.get_attribute('src')
        template_link = template.get_attribute('src')
        target_img = Image.open(BytesIO(requests.get(target_link).content))
        template_img = Image.open(BytesIO(requests.get(template_link).content))
        target_img.save('target.jpg')
        template_img.save('template.png')
        local_img = Image.open('target.jpg')
        size_loc = local_img.size
        print(int(size_loc[0]))
        self.zoom = 320 / int(size_loc[0])

    def get_tracks(self, distance):
        """
        拿到移动轨迹，模仿人的滑动行为，先匀加速后均减速
        匀变速运动基本公式：
        ①：v=v0+at
        ②：s=v0t+½at²
        ③：v²-v0²=2as
        :param distance:需要移动的距离
        :return:存放每0.3秒移动的距离
        """
        distance += 20  # 先滑过一点，最后再反着滑动回来
        # 初速度
        v = 0
        # 单位时间为0.3s来统计轨迹，轨迹即0.3s内的位移
        t = 0.3
        # 位移/轨迹列表，列表内的一个元素代表0.3s的位移
        forward_tracks = []
        # 当前位移
        current = 0
        # 到达mid值开始减速
        mid = distance * 4 / 5
        while current < distance:
            if current < mid:
                # 加速度越小，单位时间的位移越小，模拟的轨迹就越多越详细
                a = 2
            else:
                a = -3
            # 初速度
            v0 = v
            # 0.3秒时间内的位移
            s = v0 * t + 0.5 * a * (t ** 2)
            # 当前的位置
            current += s
            # 添加到轨迹列表,round()为保留一位小数且该小数要进行四舍五入
            forward_tracks.append(round(s))
            # 速度已经达到v，该速度作为下次的初速度
            v = v0 + a * t

        # 反着滑动到准确位置
        back_tracks = [-3, -3, -2, -2, -2, -2, -2, -1, -1, -1]  # 总共等于-20
        return {'forward_tracks': forward_tracks, 'back_tracks': back_tracks}

    def match(self, target, template):
        '''
        核对 target和 template的像素颜色
        :param target:
        :param template:
        :return:
        '''
        img_rgb = cv2.imread(target)  # 读取图片默认为BGR颜色空间
        img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)  # 转换颜色空间为灰度图
        template = cv2.imread(template, 0)
        w, h = template.shape[::-1]
        print(w, h)
        res = cv2.matchTemplate(img_gray, template, cv2.TM_CCOEFF_NORMED)
        run = 1

        # 使用二分法查找阈值的精确值
        L = 0
        R = 1
        while run < 20:
            run += 1
            threshold = (R + L) / 2
            print(threshold)
            if threshold < 0:
                print('Error')
                return None
            print(res, "第n次", run-1)
            loc = np.where(res >= threshold)
            print(len(loc[1]))
            if len(loc[1]) > 1:
                L += (R - L) / 2
            elif len(loc[1]) == 1:
                print('目标区域起点x坐标为：%d' % loc[1][0])
                break
            elif len(loc[1]) < 1:
                R -= (R - L) / 2
        return loc[1][0]

    def crack_slider(self):
        '''
        移动滑块并点击登录
        :return:
        '''
        slider = self.wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'yidun_slider')))
        ActionChains(self.driver).click_and_hold(slider).perform()

        for track in tracks['forward_tracks']:
            ActionChains(self.driver).move_by_offset(xoffset=track, yoffset=0).perform()

        time.sleep(0.5)
        for back_tracks in tracks['back_tracks']:
            ActionChains(self.driver).move_by_offset(xoffset=back_tracks, yoffset=0).perform()

        ActionChains(self.driver).move_by_offset(xoffset=-4, yoffset=0).perform()
        ActionChains(self.driver).move_by_offset(xoffset=4, yoffset=0).perform()
        time.sleep(0.5)

        ActionChains(self.driver).release().perform()


if __name__ == '__main__':
    cs = CrackSlider()
    cs.open()
    target = 'target.jpg'
    template = 'template.png'
    cs.driver.switch_to.default_content()  # 切回初始层
    cs.driver.find_element_by_xpath('//*[@id="agreecheck_login"]').click()  # 勾选用户协议
    rf = cs.driver.find_elements_by_tag_name("iframe")[0]  # 选择指定层框架
    time.sleep(1)
    cs.driver.switch_to.frame(rf)
    login = "u-loginbtn btncolor tabfocus"
    login_class = ''
    # 判断登录按钮是否可点击
    while login != login_class:
        print("登录按钮不可点击，开始移动滑块")
        cs.get_pic()
        distance = cs.match(target, template)
        tracks = cs.get_tracks((distance + 7) * 0.66)  # 对位移的缩放计算，*0.66本来应该是*cs.zoom的，不知道什么原因，比例总是错误
        cs.crack_slider()
        login_class = cs.driver.find_element_by_id("dologin").get_attribute("class")
    print("滑块移动结束")
    time.sleep(1)
    cs.driver.find_element_by_id("dologin").click()