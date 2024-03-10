import requests # 导入三方包 requests

url = 'https://3w.huanqiu.com/a/c36dc8/4FlmfeQIJSm?agt=128' # 给出访问地址
response = requests.get(url=url) # 利用requests包进行请求访问
print(response.status_code) # 返回请求状态码，200代表访问成功，可以直接答应response查看一下整体效果
print(response.text)
