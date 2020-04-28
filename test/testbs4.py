import re

"""
BeautifulSoap将复杂的html文档转换成一个复杂的树形结构，每个结点都是Python对象，可归纳为以下四种：
-Tag
-NavigableString
-BeautifulSoap
-Comment
"""
from bs4 import BeautifulSoup

file = open("./baidu.html", "rb")  # 以读取二进制文件的方式打开文件
html = file.read().decode("utf-8")
bs = BeautifulSoup(html, "html.parser")  # BeautifulSoap()传入一个待解析文档和一个解释器parser
"""
print(bs.title)  # 返回并打印查找到的第一个标签
print(type(bs.a))  # 返回类型'bs4.element.Tag'
# 1.Tag 标签及其内容：拿到它找到的第一个内容
print(bs.title.string)  # 加入.string直接打印内容
# 2.NavigableString 标签中的内容（字符串）
print(bs.a.attrs)  # 可以用.attrs方法提取标签中的所有属性，返回{'class': ['mnav'], 'href': 'http://news.baidu.com', 'name': 'tj_trnews'}
# 3.BeautifulSoap 表示整个文档
print(bs)
# 4.Comment 是一个特殊的NavigatableString，输出的内容不包含注释符号
print(bs.a.string)
print(type(bs.a.string))  # 'bs4.element.Comment'类型
"""
"""
# 文档的遍历
print(bs.head.contents)  # contents；获取tag的所有子节点，返回一个list列表

# 文档的搜索
# 1.find_all方法
# 字符串过滤：会查找与字符串完全匹配的内容
t_list = bs.find_all("a")

# 使用正则表达式搜索
t_list = bs.find_all(re.compile("a"))  # 用正则表达式获取所有带a的标签

# 方法搜索：传入一个函数（方法），根据函数的要求来搜索
def name_is_exist(tag):
    return tag.has_attr("name")


t_list = bs.find_all(name_is_exist)
print(t_list)
"""
# 2.kwargs 传入参数来进行搜索
"""
t_list = bs.find_all(id="head")
t_list = bs.find_all(class_=True)#输出所有含有class的内容
t_list = bs.find_all(href="http://news.baidu.com")  # 输出所有包括 href="http://news.baidu.com"的内容
for item in t_list:
    print(item)
"""
#3.Text参数（文本参数）
t_list=bs.find_all(text="hao123")
for item in t_list:
    print(item)