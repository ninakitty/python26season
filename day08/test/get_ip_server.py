from urllib import request
import re
import smtplib
import email.mime.multipart
import email.mime.text
import time
import sys


def get_ip():
    url = 'http://2019.ip138.com/ic.asp'
    context = request.urlopen(url).read().decode('gbk')
    obj = re.compile(r'您的IP是：\[(?P<ip>.*?)\] 来自：(?P<address>.*?)</center>', re.S)
    res = obj.finditer(context)
    result = []
    for item in res:
        result.append(item.group('ip'))
        result.append(item.group('address'))
    return result


def sendmail(content):
    msg = email.mime.multipart.MIMEMultipart()
    msg['from'] = 'ninakitty@126.com'  # '发送者的邮箱账号'
    msg['to'] = 'ninakitty@126.com'  # '接收者的邮箱账号'
    msg['subject'] = '获取IP地址'  # 'test，这是邮件主题'
    # content = '''''
    #     你好，
    #             这是一封自动发送的邮件的内容。
    # '''
    txt = email.mime.text.MIMEText(content)
    msg.attach(txt)
    # smtp = smtplib
    smtp = smtplib.SMTP()
    smtp.connect('smtp.126.com')  # 使用的发送者邮箱的那啥来着，post
    smtp.login('ninakitty@126.com', '831107265wyl')  # ('发送者的邮箱账号', '发送者的邮箱密码')
    smtp.sendmail('ninakitty@126.com', 'ninakitty@126.com', str(msg))  # ('发送者的邮箱账号', '接收者的邮箱账号', str(msg))
    smtp.quit()


if __name__ == '__main__':
    while 1:
        format_type = '%Y-%m-%d %H:%M:%S'
        current_time = time.strftime(format_type, time.localtime())
        result = get_ip()
        sendmail(current_time + ' ' + result[0])
        wait_time = 300  # 等待多少秒
        print(current_time, '邮件已发出!')
        sys.stdout.write('>')
        sys.stdout.flush()
        for i in range(wait_time):
            time.sleep(1)
            if i == wait_time - 1:
                print(f'\r执行:!', end='')
            else:
                print(f'\r请稍等,{wait_time - 1 - i}秒后将再次执行!', end='')
