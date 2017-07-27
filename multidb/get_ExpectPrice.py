#coding=utf-8
import requests
import re
import timeit
from bs4 import BeautifulSoup

start = timeit.default_timer()
def getPrice(name):
    url = "http://www.lianu.com/dbdsql3.php?code=1&name="
    url += name
    url += "&sul=0&time1=0&time2=0&zt=&day=90"
    # print ("url:",url)
    rel = requests.get(url)
    # print("接口响应时间：",rel.elapsed.microseconds)
    rel.encoding = rel.apparent_encoding
    html = rel.text
    soup = BeautifulSoup(html,"html.parser")
    #定义一个字典类型的字段，用来存储值
    dest = {}
    price = ""
    for tag in soup.find_all('font'):
            str = tag.get_text()
            arr  = str.split(':')

            if (len(arr) < 2):
                    continue
            #遍历第一个first的值，一般第一次值为“90天均价”：第一个first 90天均价
            first  = arr[0]
            # print("第一个first",first)

            #根据"|"来进行过滤，比如：90天均价:1349|最低:1109 ☆30天:1339|15天:1352|5天:1367|3天:1349|昨天:1415
            if(not arr[1].find("|")):
                 continue
            #遍历第一个second的值，一般第一次为90天均价的价格：第一个second 1349
            second = arr[1].split('|')[0]
            # print("第一个second", second)
            if(len(second) < 1):
                    continue
            #将first取到的值为，返回类似
            #ret = <_sre.SRE_Match object; span=(0, 2), match='90'>
            ret = re.match(u"(\d+)", first)
            # print("ret的值",ret)
            if not ret:
                continue
            dest[int(ret.group(1))] = second
            # print("第二个second,dest过滤的",second)
    if len(dest) > 0 :
        #用sorted函数进行排序，取最小的值
        key = sorted(dest.items())[0]
        # print("key的值",key)
        price = key[1]
        # print("price的值",price)
        # elapsed = timeit.default_timer() - start
        # print("程序运行所使用时间：", elapsed)
    return price


#test code
# name = "联想 ZUK Z2 Pro手机（Z2121）尊享版 6G+128G 陶瓷白 移动联通电信4G手机 双卡双待"
# print(getPrice(name))