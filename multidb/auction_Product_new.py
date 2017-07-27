import requests
import json
import time
import random
from multidb import format_cookies
from multidb import request_test
from multidb import bid_list
from multidb import MyTimer
url_bid = "http://dbditem.jd.com/services/bid.action"
proxies = {
    "http":"http://127.0.0.1:8888"
}

db_result = "result"

def db_pmprice(db_paimaiId,db_price,i):
    (my_bid_username_tu, my_bd_nick_tu) = format_cookies.get_cookieUser(i) #返回的是元组
    my_bid_username = str(my_bid_username_tu) #需要把元组数据转化成字符串
    db_price = int(db_price)  #将商品的价格转化为int类型
    db_paimaiId = str(db_paimaiId) #将商品的ID转化为str类型
    headers = {"Accept": "application/json, text/javascript, */*; q=0.01",
               "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:53.0) Gecko/20100101 Firefox/53.0",
               "X-Requested-With": "XMLHttpRequest",
               "Referer": "http://dbditem.jd.com/" + db_paimaiId
               }
    db_currentPrice = int(request_test.obtain_value(db_paimaiId,"currentPrice"))
    jp_result = ""
    cookies = format_cookies.format_cookies(i)
        # print('当前的价格：%s'%db_currentPrice)
    print('我出的价格：%s'%db_price + "   出价的账户是：" + my_bid_username )
    urlbid_params = {"t": "054488", "paimaiId": db_paimaiId, "price": db_price, "proxyFlag": "0", "bidSource": "0"}
    relbid = requests.get(url_bid, params=urlbid_params, headers=headers, cookies=cookies, proxies=proxies)
    res = relbid.text
    res_json = json.loads(res)
    if res_json[db_result] == 200:
        current_bid_price = bid_list.bid_result("price",db_paimaiId)
        jp_result = my_bid_username +  "  \033[1;35m出价成功了 \033[0m" + res_json["message"]   +  "   当前的价格是 " + str(current_bid_price)
    else :
        current_bid_price = bid_list.bid_result("price",db_paimaiId)
        current_bid_username = bid_list.bid_result("username",db_paimaiId)
        jp_result = "没有竞拍成功，原因是：" + res_json["message"] + "   当前领先的人是：" + current_bid_username + "   当前的价格是 " + str(current_bid_price)
    return jp_result
def run_bd(db_paimaiId,db_price,db_productName):
    with open("cookies/cookie.txt", "r") as f:
        i = random.randint(0, len(f.readlines()) - 1)
    remainTime = request_test.obtain_value(db_paimaiId,"remainTime")
    print("\033[1;32m开始竞拍流程，当前剩余竞拍时间：\033[0m",remainTime)
    while request_test.obtain_value(db_paimaiId,"remainTime" ) > 0:
        db_currentPrice = int(request_test.obtain_value(db_paimaiId, "currentPrice"))
        db_price = int(db_price) - 200
        if db_currentPrice < db_price:
            try:
                hours = int((remainTime % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60))
                minutes = int((remainTime % (1000 * 60 * 60)) / (1000 * 60))
                seconds = int((remainTime % (1000 * 60)) / 1000)
                print(db_pmprice(db_paimaiId, db_price,i) + " :" + db_productName + "  时间还剩下：" + str(hours) + "小时", str(minutes) + "分", str(seconds) + "秒")
                time.sleep(10)
            except Exception as e:
                print(e)
        else:
            break
    else:
        current_bid_price = bid_list.bid_result("price",db_paimaiId)
        current_bid_username = bid_list.bid_result("username",db_paimaiId) #获取最终竞拍成功的用户名
        (my_bid_username_tu,my_bd_nick_tu) = format_cookies.get_cookieUser(i)
        my_bd_nick = str(my_bid_username_tu)
        my_bd_nick_last4 = "****" +  my_bd_nick[-4:]
        print("\033[1;33;44m竞拍已结束 !\033[0m")
        print("竞拍成功的人是：" + current_bid_username + "  : " + db_productName + "当前的价格是 " + str(current_bid_price))
        f = open("cookies/jingpai1.txt","w")
        if current_bid_username == my_bd_nick_last4:
            # print("\033[1;35m我终于买到了！！！ \033[0m" + "  " + db_productName +":" + db_paimaiId )
            print("\033[1;35m我终于买到了！！！ \033[0m" + "  " + db_productName +":" + db_paimaiId,file = f )
        else:
            print("又被人抢走了")
