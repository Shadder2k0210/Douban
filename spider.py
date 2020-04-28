from bs4 import BeautifulSoup  # 网页解析，获取数据
import re  # 正则表达式，进行文字匹配
import urllib.request, urllib.error  # 指定URL，获取网页数据
import xlwt  # 进行excel操作
import sqlite3  # 进行sqlite数据库操作


def main():
    baseurl = "https://movie.douban.com/top250?start="  # 一定要注意防止对网址的代码格式化，不要加空格，否则没有返回数据

    # 1.爬取网页
    datalist = getData(baseurl)
    # saveData(savepath=".\\豆瓣电影top250.xls")  # 注意要用转义字符
    askURL("https://movie.douban.com/top250")


# 爬取网页
def getData(baseurl):
    datalist = []
    # 一次只能爬取一个网页中的10条数据，写for循环遍历豆瓣网站上的共250条数据，共调用10次
    for i in range(0, 10):
        url = baseurl + str(i * 25)  # 在?start=后添加页数编码
        html = askURL(url)  # 保存获取到的网页源码
        # 对获取到的网页信息进行处理
    return datalist


# 得到一个指定url的网页信息
def askURL(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                      "Chrome/81.0.4044.122 Safari/537.36 Edg/81.0.416.64 "
    }  # 用户代理，告知豆瓣服务器伪装浏览器的类型
    request = urllib.request.Request(url=url, headers=headers)  # 调用Request类，并且注意一定要加入header
    html = ""
    try:
        response = urllib.request.urlopen(request)
        html = response.read().decode("utf-8")
        print(html)
    except urllib.error.URLError as result:
        if hasattr(result, "code"):  # hasattr(object,name) 函数用于判断对象是否包含对应的属性，如果object中包含name则返回True
            print(result.code)  # 在报错信息中找code并输出（包含在URLError报错信息中）
        if hasattr(result, "reason"):
            print(result.reason)  # 在报错信息中找reason并输出（包含在URLError报错信息中）
    return html


# 保存数据
def saveData(savepath):
    print("saving...")


if __name__ == "__main__":  # 主程序入口，当程序执行时
    main()

# 从包中引入文件：import 包名称 from 文件名称，这样就可以调用其他包中的函数，格式为文件名.函数名
