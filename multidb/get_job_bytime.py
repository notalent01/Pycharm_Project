#-*- coding:utf-8 -*-
import requests
import json
import re
# import test1.format_cookies
from multidb import get_ProductName
proxies = {
    "http":"http://127.0.0.1:8888"
}

def loads_jsonp(_jsonp):
    try:
        return json.loads(re.match(".*?(\[.*\]).*",_jsonp,re.S).group(1))
    except:
        raise ValueError('Invalid Input')

def obtain_value(params):
    url_current_list = "http://dbditem.jd.com/services/currentList.action"
    # print ("fetch remainTime:",params)
    jobarry = []
    if len(params) < 1:
        return jobarry
    res = requests.get(url_current_list, params=params,proxies=proxies)
    a1 = res.text
    a2 = loads_jsonp(a1)
    for ii in a2:
        remainTime = ii["remainTime"]
        print("第一次拿到的商品剩余时间：%s" %remainTime)
        if 0<remainTime < 30000:
            jobarry.append(str(ii["paimaiId"]))
        else:
             print("没有满足规定剩余时间的商品！！！")
    return jobarry

#test code
mymap = get_ProductName.get_paramid_map()
url = get_ProductName.get_params_by_paramid_map(mymap);
print(obtain_value(url))
