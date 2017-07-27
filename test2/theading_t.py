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
    price = ""
    for tag in soup.find_all('font'):
        str = tag.get_text()
        arr = str.split(':')

        if (len(arr) < 2):
            continue

        first = arr[0]

        if (not arr[1].find("|")):
            continue

        second = arr[1].split('|')[0]

        if (len(second) < 1):
            continue

        if (first.find("3天")):
            price = second
            # elapsed = timeit.default_timer() - start
            # print("程序运行所使用时间：", elapsed)
            break

    return price

#test code
name = "联想 ZUK Z2 Pro手机（Z2121）尊享版 6G+128G 陶瓷白 移动联通电信4G手机 双卡双待"
print(getPrice(name))