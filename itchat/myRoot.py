import  itchat
import requests
import time
Key = '8bbb773cc4fb466abc23ea16b8f247d9'
def get_response(msg):
    apiUrl = 'http://www.tuling123.com/openapi/api'
    data = {
        'key': '',
        'info': msg,
        'userid': 'wechat-robot',
    }
    r = requests.post(apiUrl, data=data).json()
    print(r['text'])
    return r['text']
@itchat.msg_register(itchat.content.TEXT)
def tuling_reply(msg):
    print(msg['Text'])
    # 为了保证在图灵Key出现问题的时候仍旧可以回复，这里设置一个默认回复
    defaultReply = 'I received: ' + msg['Text']
    # 如果图灵Key出现问题，那么reply将会是None
    reply = get_response(msg['Text'])
    # a or b的意思是，如果a有内容，那么返回a，否则返回b
    # 有内容一般就是指非空或者非None，你可以用`if a: print('True')`来测试

    reply =  reply or defaultReply
    # itchat.send(reply,'filehelper')
    print(reply)
    return  reply or defaultReply
# 为了让实验过程更加方便（修改程序不用多次扫码），我们使用热启动
itchat.auto_login(hotReload=True)

itchat.run()
