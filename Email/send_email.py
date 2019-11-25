import smtplib # smtplib 用于邮件的发信动作
from email.mime.text import MIMEText # email 用于构建邮件内容
from email.header import Header # 用于构建邮件头
from common.read_config import ReadConfig


class SendEmail:
    def __init__(self):
        rc = ReadConfig()
        self.to_addr = rc.get_db("sendemail", "to_addr") #收信方
        self.from_addr = rc.get_db("sendemail", "from_addr") #发信方
        self.password = rc.get_db("sendemail", "password") #发信密码
        self.email_type = self.to_addr.split("@")[1]
        self.smtp_server = "smtp."+ self.email_type
        if self.email_type=="qq.com":
            self.port = 465
        elif self.email_type=="163.com":
            self.port = 25
        else:
            print("请配置目标邮箱类型的端口号！")

    def make_email(self, content):
        # 邮箱正文内容，第一个参数为内容，第二个参数为格式(plain 为纯文本)，第三个参数为编码
        msg = MIMEText(content, 'plain', 'utf-8')
        # 邮件头信息
        msg['From'] = Header(self.from_addr)
        msg['To'] = Header(self.to_addr)
        msg['Subject'] = Header('python test')
        return msg

    def send_mail(self, msg):
        if self.email_type=="qq.com":
            # 开启发信服务，这里使用的是加密传输
            server = smtplib.SMTP_SSL(self.smtp_server, self.port)
        elif self.email_type=="163.com":
            server = smtplib.SMTP(self.smtp_server, self.port)
        else:
            print("请配置目标邮箱类型的连接方式！")
        # server.connect("localhost", self.smtp_server, self.port)
        # server.set_debuglevel(1)  # 这句话，可以打印出和SMTP交互的所有信息
        # 登录发信邮箱
        server.login(self.from_addr, self.password)
        # 发送邮件
        server.sendmail(self.from_addr, self.to_addr, msg.as_string())
        # 关闭服务器
        server.quit()
        print("邮件已发送！")


if __name__ == "__main__":
    se = SendEmail()
    msg = se.make_email("发送内容")
    se.send_mail(msg)















