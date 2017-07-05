import requests
import json
import time
from multidb import format_cookies
from multidb import request_test
from multidb import bid_list
url_bid = "http://dbditem.jd.com/services/bid.action"
proxies = {
    "http":"http://127.0.0.1:8888"
}
cookies = format_cookies.format_cookies()
db_result = "result"
def db_pmprice(db_paimaiId,db_price):
    headers = {"Accept": "application/json, text/javascript, */*; q=0.01",
               "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:53.0) Gecko/20100101 Firefox/53.0",
               "X-Requested-With": "XMLHttpRequest",
               "Referer": "http://dbditem.jd.com/" + db_paimaiId
               }
    db_currentPrice = int(request_test.obtain_value(db_paimaiId,"currentPrice"))
    if db_currentPrice < db_price:
        print('当前的价格：%s'%db_currentPrice)
        # db_price = int(request_test.obtain_value("currentPrice") + request_test.obtain_value("priceLowerOffset"))
        print('我出的价格：%s'%db_price)
        urlbid_params = {"t": "054488", "paimaiId": db_paimaiId, "price": db_price, "proxyFlag": "0", "bidSource": "0"}
        relbid = requests.get(url_bid, params=urlbid_params, headers=headers, cookies=cookies, proxies=proxies)
        res = relbid.text
        res_json = json.loads(res)
        if res_json[db_result] == 200:
            current_bid_price = bid_list.bid_result("price")
            jp_result = "\033[1;35m我出价成功了 \033[0m" + res_json["message"] + "   当前的价格是 " + str(current_bid_price)
        else :
            current_bid_price = bid_list.bid_result("price")
            current_bid_username = bid_list.bid_result("username")
            jp_result = "没有竞拍成功，原因是：" + res_json["message"] + "   当前领先的人是：" + current_bid_username + "   当前的价格是 " + str(current_bid_price)
    elif db_currentPrice > db_price:
        jp_result = "不买了！当前的价格是%s"%db_currentPrice + "我的理想价格是%s"%db_price
    return jp_result
def run_bd(db_paimaiId,db_price):
    while request_test.obtain_value(db_paimaiId,"remainTime") > 0:
        try:
            remainTime = request_test.obtain_value(db_paimaiId,"remainTime")
            hours = int((remainTime % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60))
            minutes = int((remainTime % (1000 * 60 * 60)) / (1000 * 60))
            seconds = int((remainTime % (1000 * 60)) / 1000)
            print(db_pmprice(db_paimaiId,db_price) + "  时间还剩下：" + str(hours) + "小时", str(minutes) + "分", str(seconds) + "秒")
            time.sleep(2)
        except Exception as e:
            print(e)
    else:
        current_bid_price = bid_list.bid_result("price")
        current_bid_username = bid_list.bid_result("username")
        print("\033[1;33;44m竞拍已结束 !\033[0m")
        print("竞拍成功的人是：" + current_bid_username + "当前的价格是 " + str(current_bid_price))
        if current_bid_username == "****ujzz":
            print("\033[1;35m我终于买到了！！！ \033[0m")
        else:
            print("又被人抢走了")
# run_bd(15876485,500)