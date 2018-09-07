import requests
apiUrl = "http://www.tuling123.com/openapi/api"
data = {
    'key'    : '', # 如果这个Tuling Key不能用，那就换一个
    'info'   : 'hi', # 这是我们发出去的消息
    'userid' : 'wechat-robot', # 这里你想改什么都可以
}
r = requests.post(apiUrl,data = data).json()
print(r)