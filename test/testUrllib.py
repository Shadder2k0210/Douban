import urllib.request

'''
# 获取一个get请求
response = urllib.request.urlopen("http://www.baidu.com")  # urlopen对一个网址进行解析，返回给response
print(response.read().decode("utf-8"))  # 使用read()对封装起来的数据进行读取，decode("utf-8")转化成中文格式
'''
'''
# 获取一个post请求(httpbin.org)：模拟用户真实登录时使用
import urllib.parse  # 用于解析

data = bytes(urllib.parse.urlencode({"hello": "world"}),encoding="utf-8")  # 其中放的是字典,并说明按照什么方式来解码
response = urllib.request.urlopen("http://httpbin.org/post", data=data)
print(response.read().decode("utf-8"))#同样用decode()函数进行解码
'''
'''
# 超时处理：需要有计划性的准备，采用异常处理机制
try:
    response = urllib.request.urlopen("http://httpbin.org/get", timeout=0.01)  # 执行一次get请求,超过0.01秒即为超时
    print(response.read().decode("utf-8"))
except urllib.error.URLError as result:
    print("网站请求超时！")
'''
'''
response1 = urllib.request.urlopen("http://httpbin.org/get")
print(response1.status)  # response.status表示返回数据的类型，200即为成功访问该网站
response2 = urllib.request.urlopen("http://www.baidu.com")
print(response2.getheader("Server"))  # 获取header中的属性
'''
'''
# 将爬虫伪装成浏览器获取网页信息——测试案例
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/81.0.4044.122 Safari/537.36 Edg/81.0.416.64 "
}  # 将headers伪装成正常浏览器
url = "http://httpbin.org/post"
data = bytes(urllib.parse.urlencode({"hello": "world"}), encoding="utf-8")
req = urllib.request.Request(url=url, data=data, headers=headers, method="POST")
response = urllib.request.urlopen(req)  # 在此处传入封装好的请求类型req
print(response.read().decode("utf-8"))
'''
#爬取豆瓣
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/81.0.4044.122 Safari/537.36 Edg/81.0.416.64 "
}  # 将headers伪装成正常浏览器
url = "https://movie.douban.com/top250"
data = bytes(urllib.parse.urlencode({"hello": "world"}), encoding="utf-8")
req = urllib.request.Request(url=url,  headers=headers)
response = urllib.request.urlopen(req)  # 在此处传入封装好的请求类型req
print(response.read().decode("utf-8"))