def sendError():

    from email.header import Header

    from email.mime.text import MIMEText

    from email.utils import parseaddr,formataddr

    import smtplib

    def _format_addr(s):    

        name,addr = parseaddr(s)    

        return formataddr((Header(name,'utf-8').encode(),addr))

    #发件人地址

    from_addr = 'tan137310853@163.com'

    #密码刚才复制的邮箱的授权码

    password = 'tan137310853'

    #收件人地址

    to_addr =  '137310853@qq.com'

    #邮箱服务器地址

    smtp_server = 'smtp.163.com'

    #设置邮件信息

    msg = MIMEText('Python替班提醒程序异常，请检查！','plain','utf-8')

    msg['From'] = _format_addr('替班提醒<%s>'%from_addr)

    msg['To'] = _format_addr('管理员<%s>'%to_addr)

    msg['Subject'] = Header('替班提醒程序异常.','utf-8').encode()

    #发送邮件

    server = smtplib.SMTP_SSL(smtp_server,465)

    #打印出和SMTP服务器交互的所有信息

    server.set_debuglevel(1)

    #登录SMTP服务器

    server.login(from_addr,password)

    #sendmail():发送邮件，由于可以一次发给多个人，所以传入一个list邮件正文是一个str，as_string()把MIMEText对象变成str。

    server.sendmail(from_addr,to_addr,msg.as_string())
    server.quit()
    print('邮件发送成功！')


sendError()
