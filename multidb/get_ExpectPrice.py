#!/usr/bin/python
#coding=utf-8

import requests
from bs4 import BeautifulSoup

def getPrice(name,day):
    url = "http://www.lianu.com/dbdsql3.php?code=1&name="
    url += name
    url += "&sul=0&time1=0&time2=0&zt=&day=90"
    # print ("url:",url)
    rel = requests.get(url)
    rel.encoding = rel.apparent_encoding
    html = rel.text
    soup = BeautifulSoup(html,"html.parser")
    price = ""
    for tag in soup.find_all('font'):
            str = tag.get_text()
            arr  = str.split(':')

            if (len(arr) < 2):
                    continue

            first  = arr[0]

            if(not arr[1].find("|")):
                 continue

            second = arr[1].split('|')[0]

            if(len(second) < 1):
                    continue

            if(first.find(day)):
                price = second
                break

    return price