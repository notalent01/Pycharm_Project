import requests
import json
import re
import time
from test1 import format_cookies
# from test1 import db_jingpai
# from test1 import db_jingpai
proxies = {
    "http":"http://127.0.0.1:8888"
}
db_paimaiIds = "15804459"
expect_price = 1400
# a2 = json.dumps(a1)
# print ("a1是:" + str(a1))
# print ("a2是" + a2)
def loads_jsonp(_jsonp):
    try:
        return json.loads(re.match(".*?({.*}).*",_jsonp,re.S).group(1))
    except:
        raise ValueError('Invalid Input')

def obtain_value(str):
    url1 = 'http://dbditem.jd.com/services/currentList.action'
    current_localtime = round(time.time() * 1000)
    next_localtime = current_localtime + 1
    callback_str = "%s%s" % ("jsonp_ ", current_localtime)
    url1_params = {"paimaiIds": db_paimaiIds, "curPaimaiId": db_paimaiIds, "callback": callback_str,
                   "_": next_localtime}
    cookies = format_cookies.format_cookies()
    res1 = requests.get(url1, params=url1_params, cookies=cookies, proxies=proxies)
    a1 = res1.text
    a2 = loads_jsonp(a1)
    # print(a2)
    current_value = a2[str]
    return current_value
# b1 = "currentPrice"
# b2 = "remainTime"
# print("该商品当前的价格是：" + str(obtain_value(b1)))
# print("该商品当前剩余时间：" + str(obtain_value(b2)))
# print(type(obtain_value(b2)),obtain_value(b2))
# if __name__ == '__main__':
#     remain_time = obtain_value(b2)
#     if obtain_value(b2) > 0:
#         hours = int((remain_time % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60))
#         minutes = int((remain_time % (1000 * 60 * 60)) / (1000 * 60))
#         seconds = int((remain_time % (1000 * 60)) / 1000)
#         # print(obtain_value(b2))
#         print("当前商品还剩余： " + str(hours) + "小时",str(minutes) + "分",str(seconds) + "秒")
#         print("当前的商品价格：" + str(obtain_value(b1)))
#         # if remain_time <= 42000:
# else:
#         print("当前商品已结束")

