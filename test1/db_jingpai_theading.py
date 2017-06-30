# coding:utf-8
import requests
import json
import time
import threading
from test1 import format_cookies
from test1 import request_test
from test1 import bid_list
# expect_price = 60
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
cookies = format_cookies.format_cookies()
db_result = "result"
def db_pmprice(db_price):
    # db_price = 0
    db_currentPrice = int(request_test.obtain_value("currentPrice"))
    expect_price = request_test.expect_price
    if db_currentPrice > db_price and db_currentPrice <= expect_price:
        print('当前的价格：%s'%db_currentPrice)
        db_price = int(request_test.obtain_value("currentPrice") + request_test.obtain_value("priceLowerOffset"))
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
    elif db_currentPrice > expect_price:
        jp_result = "不买了！当前的价格是%s"%db_currentPrice + "我的理想价格是%s"%expect_price
        return jp_result
    else:
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

    return jp_result
def run_bd():
    while request_test.obtain_value("remainTime") > 0:
        try:
            remainTime = request_test.obtain_value("remainTime")
            hours = int((remainTime % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60))
            minutes = int((remainTime % (1000 * 60 * 60)) / (1000 * 60))
            seconds = int((remainTime % (1000 * 60)) / 1000)
            if remainTime > 45000:
                print("先别竞拍，当前商品还剩余： " + str(hours) + "小时", str(minutes) + "分", str(seconds) + "秒")
                time.sleep(5)
            else:
                if remainTime > 1000:
                    print(db_pmprice(0) + "  时间还剩下：" + str(hours) + "小时", str(minutes) + "分", str(seconds) + "秒")
                    time.sleep(2)
                else:
                    db_price = int(
                        request_test.obtain_value("currentPrice") + request_test.obtain_value("priceHigherOffset"))
                    print("我输入的最高价格是%s" % db_price)
                    expect_price = request_test.expect_price
                    print("我输入的期望价格是%s" % expect_price)
                    if db_price < expect_price:
                        print(db_pmprice(db_price) + "  时间还剩下：" + str(hours) + "小时", str(minutes) + "分",
                              str(seconds) + "秒")
                        time.sleep(2)
                    else:
                        expect_price = request_test.expect_price
                        print(db_pmprice(expect_price) + "  时间还剩下：" + str(hours) + "小时", str(minutes) + "分",
                              str(seconds) + "秒")
                        time.sleep(2)
        except Exception as e:
            print(e)
    else:
        current_bid_price = bid_list.bid_result("price")
        current_bid_username = bid_list.bid_result("username")
        print("\033[1;33;44m竞拍已结束 !\033[0m")
        print("竞拍成功的人是：" + current_bid_username + "当前的价格是 " + str(current_bid_price))
        if current_bid_username == "****1wgj":
            print("\033[1;35m我终于买到了！！！ \033[0m")
        else:
            print("又被人抢走了")
threads = []
if __name__ == '__main__':
    run_bd()


