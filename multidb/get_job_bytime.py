#-*- coding:utf-8 -*-
import requests
import json
import re
# import test1.format_cookies
from multidb import get_ProductName
proxies = {
    "http":"http://127.0.0.1:8888"
}
#对接口的返回结果jsonp格式化成json
def loads_jsonp(_jsonp):
    try:
        return json.loads(re.match(".*?(\[.*\]).*",_jsonp,re.S).group(1))
    except:
        raise ValueError('Invalid Input')

#返回一个二维数组：
# [['16088093', 203461], ['16088668', 23461], ['16088026', 503461], ['16087908', 323461], ['16087993', 323461], ['16088221', 143461], ['16088115', 263461], ['16087636', 83461], ['16087841', 203461], ['16088551', 143461], ['16088199', 203461], ['16088012', 23461]]

def obtain_value(params):
    url_current_list = "http://dbditem.jd.com/services/currentList.action"
#    print "fetch remainTime:",params
    jobarry = []
    if len(params) < 1:
        return jobarry
    res = requests.get(url_current_list, params=params)
    a1 = res.text
    a2 = loads_jsonp(a1)
    for ii in a2:
        remainTime = ii["remainTime"]
        if remainTime > 0 and remainTime < 3600000:
            subarry = []
            subarry.append(str(ii["paimaiId"]))
            subarry.append(remainTime)
            jobarry.append(subarry)
    return jobarry

#test code
# mymap = get_ProductName.get_paramid_map()
# url = get_ProductName.get_params_by_paramid_map(mymap);
# print(obtain_value(url))
