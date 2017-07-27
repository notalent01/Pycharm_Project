import requests
import json
import re
import time
import random
from multidb import format_cookies

proxies = {
    "http":"http://127.0.0.1:8888"
}
with open ("cookies/cookie.txt","r") as f :
    i = random.randint(0, len(f.readlines())-1)
def loads_jsonp(_jsonp):
    try:
        return json.loads(re.match(".*?({.*}).*",_jsonp,re.S).group(1))
    except:
        raise ValueError('Invalid Input')

def obtain_value(db_paimaiId,value):
    url1 = 'http://dbditem.jd.com/services/currentList.action'
    current_localtime = round(time.time() * 1000)
    next_localtime = current_localtime + 1
    callback_str = "%s%s" % ("jsonp_ ", current_localtime)
    url1_params = {"paimaiIds": db_paimaiId, "curPaimaiId": db_paimaiId, "callback": callback_str,
                   "_": next_localtime}
    cookies = format_cookies.format_cookies(i)
    res1 = requests.get(url1, params=url1_params, cookies=cookies, proxies=proxies)
    a1 = res1.text
    a2 = loads_jsonp(a1)
    current_value = a2[value]
    return current_value
# print(obtain_value(15956384,"currentPrice"))

