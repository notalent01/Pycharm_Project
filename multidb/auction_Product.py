import requests
import json
import time
from multidb import format_cookies
from multidb import get_ProductName
from multidb import get_job_bytime
url_bid = "http://dbditem.jd.com/services/bid.action"
proxies = {
    "http":"http://127.0.0.1:8888"
}
# db_paimaiId = get_job_bytime.obtain_value(url)
# expect_price = request_test.expect_price
# headers = {"Accept":"application/json, text/javascript, */*; q=0.01",
#            "User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64; rv:53.0) Gecko/20100101 Firefox/53.0",
#            "X-Requested-With":"XMLHttpRequest",
#            "Referer":"http://dbditem.jd.com/" + db_paimaiId
#            }
# cookies = format_cookies.format_cookies()
# def db_pmprice(db_price):