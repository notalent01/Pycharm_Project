# coding:utf-8
import requests
import json
import time
import logging
from test1 import format_cookies
from test1 import request_test
url_bid = "http://dbditem.jd.com/services/bid.action"
proxies = {
    "http":"http://127.0.0.1:8888"
}
db_paimaiId = request_test.db_paimaiIds
headers = {"Accept":"application/json, text/javascript, */*; q=0.01",
           "User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64; rv:53.0) Gecko/20100101 Firefox/53.0",
           "X-Requested-With":"XMLHttpRequest",
           "Referer":"http://dbditem.jd.com/" + db_paimaiId
           }
# print(format_cookies())
cookies = format_cookies.format_cookies()
# res = relbid.text
# print(res)
# res_json = json.loads(res)
# print(res_json)
db_result = "result"
# def db_start():
def db_price():
    db_price = 0
    db_currentPrice = int(request_test.obtain_value("currentPrice"))
    logging.info('当前的价格：%s',db_currentPrice)
    if db_currentPrice > db_price:
        print('当前的价格：%s'%db_currentPrice)
        db_price = int(request_test.obtain_value("currentPrice") + request_test.obtain_value("priceLowerOffset"))
        print('我出的价格：%s'%db_price)
        urlbid_params = {"t": "054488", "paimaiId": db_paimaiId, "price": db_price, "proxyFlag": "0", "bidSource": "0"}
        relbid = requests.get(url_bid, params=urlbid_params, headers=headers, cookies=cookies, proxies=proxies)
        res = relbid.text
        res_json = json.loads(res)
        print(res_json)
        if res_json[db_result] == 200:
            jp_result = "我出价成功了" + res_json["message"]
        else :
            jp_result = "没有竞拍成功，原因是：" + res_json["message"]
    else :
            jp_result = "大于当前价格"
    return jp_result
if __name__ == '__main__':
    while request_test.obtain_value("remainTime") > 0:
        try:
            # db_price()
            print(db_price())
            time.sleep(2)
        except Exception as e:
            print(e)
