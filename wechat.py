import itchat

@itchat.msg_register(itchat.content.TEXT, False, True, False)
def tuling_reply(msg):
    message = msg["Text"]
    nickName = msg["User"]["NickName"]
    if nickName.find("电教中心") == -1:
        #不是电教群的信息
        return
    if message.find("替") != -1:
        #收到替班的信息
        #先秒回
        #itchat.send("我", toUserName=msg["FromUserName"])
        #再给微信支付公众号发信息，然后让它回复信息，手机就会收到提醒
        wxzf = itchat.search_mps(name='微信支付')[0]
        itchat.send('1', toUserName=wxzf["UserName"])
        return

itchat.auto_login(hotReload=True, enableCmdQR=-1)
itchat.run()
print("itchat退出，发送提醒邮件！")
import sendError
