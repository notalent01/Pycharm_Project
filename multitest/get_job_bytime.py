#-*- coding:utf-8 -*-
import requests
import json
import re
import test1.format_cookies

from multitest import get_ParamIDs
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
    print ("fetch remainTime:",params)
    jobarry = []
    if len(params) < 1:
        return jobarry
    res = requests.get(url_current_list, params=params,proxies=proxies)
    a1 = res.text
    a2 = loads_jsonp(a1)
    # print(a2)
    # print(len(a2))
    for ii in a2:
        remainTime = ii["remainTime"]
        print(ii)
        if remainTime < 500000:
            jobarry.append(ii["paimaiId"])
    return jobarry

#test code
# url = get_ParamIDs.get_list_url_params();
# print(obtain_value(url))
