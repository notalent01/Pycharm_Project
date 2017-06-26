import time
import requests
import json
import re
import time
from test1 import format_cookies
from test1 import request_test
def loads_jsonp(_jsonp):
    try:
        return json.loads(re.match(".*?({.*}).*",_jsonp,re.S).group(1))
    except:
        raise ValueError('Invalid Input')
def obtain_value(str):
    url1 = 'http://dbditem.jd.com/services/currentList.action'
    db_paimaiIds = "15756910"
    current_localtime = round(time.time() * 1000)
    print(current_localtime)
    print(type(current_localtime))
    next_localtime = current_localtime + 1
    # current_localtime_str = str(current_localtime)
    callback_str = "%s%s"%("jsonp_ ",current_localtime)
    print(callback_str)
    url1_params = {"paimaiIds": db_paimaiIds, "curPaimaiId": db_paimaiIds, "callback": callback_str,
                   "_": next_localtime}
    cookies = format_cookies.format_cookies()
    res1 = requests.get(url1, params=url1_params, cookies=cookies)
    a1 = res1.text
    a2 = loads_jsonp(a1)
    print(a2)
    current_value = a2[str]
    return current_value
print(obtain_value("remainTime"))