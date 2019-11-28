import smtplib # smtplib 用于邮件的发信动作
from email.mime.text import MIMEText # email 用于构建邮件内容
from email.header import Header # 用于构建邮件头
from common.read_config import ReadConfig
from email.mime.multipart import MIMEMultipart #带多个部分的邮件
from email.mime.application import MIMEApplication  #主要类型的MIME消息对象应用


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

    def make_email(self, content, files=None):
        # 邮箱正文内容，第一个参数为内容，第二个参数为格式(plain 为纯文本)，第三个参数为编码
        msg = MIMEText(content, 'plain', 'utf-8')
        msg.add_header()
        if files is 'None':
            pass
        else:
            for tmp in files:
                with open(tmp, 'rb') as f:
                    attachfiles = MIMEApplication(f.read())
                    attachfiles.add_header('Content-Disposition', 'attachment', filename=tmp)
                    msg.attach(attachfiles)

        # 邮件头信息
        msg['From'] = Header(self.from_addr)
        msg['To'] = Header(self.to_addr)
        msg['Subject'] = Header('python test')
        return msg

    def send_mail(self, msg):
        try:
            if self.email_type == "qq.com":
                # 开启发信服务，这里使用的是加密传输
                server = smtplib.SMTP_SSL(self.smtp_server, self.port)
            elif self.email_type == "163.com":
                server = smtplib.SMTP(self.smtp_server, self.port)
            else:
                print("请配置目标邮箱类型的连接方式！")
            # 登录发信邮箱
            server.login(self.from_addr, self.password)
            # 发送邮件
            server.sendmail(self.from_addr, self.to_addr, msg.as_string())
            # 关闭服务器
            server.quit()
            print("邮件已发送！")
        except smtplib.SMTPConnectError as e:
            print('邮件发送失败，连接失败:', e.smtp_code, e.smtp_error)
        except smtplib.SMTPAuthenticationError as e:
            print('邮件发送失败，认证错误:', e.smtp_code, e.smtp_error)
        except smtplib.SMTPSenderRefused as e:
            print('邮件发送失败，发件人被拒绝:', e.smtp_code, e.smtp_error)
        except smtplib.SMTPRecipientsRefused as e:
            print('邮件发送失败，收件人被拒绝:', e.recipients)
        except smtplib.SMTPDataError as e:
            print('邮件发送失败，数据接收拒绝:', e.smtp_code, e.smtp_error)
        except smtplib.SMTPException as e:
            print('邮件发送失败, ', e.filename)
        except Exception as e:
            print('邮件发送异常, ', str(e))


if __name__ == "__main__":
    se = SendEmail()
    msg = se.make_email("发送内容")
    se.send_mail(msg)















