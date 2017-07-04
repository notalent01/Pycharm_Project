#!/usr/bin/python
#coding=utf-8
import requests
from bs4 import BeautifulSoup
from multidb import get_ProductName
def get_productPrice(product_name):
    #?code=1&name=&sul=0&time1=0&time2=0&zt=&day=90
    url = "http://www.lianu.com/dbdsql3.php"
    params = {"code":"1","name":product_name,"sul":"0","time1":"0","time2":"0","zt":"","day":"90"}
    rel = requests.get(url,params=params)
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

            if (first[0:1] == '3' and len(first) == 3):
                price = second
                break

    return price

#test code
product_name = get_ProductName.get_paramid_map()[0]
print(get_productPrice(product_name))