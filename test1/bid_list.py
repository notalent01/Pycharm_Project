import requests
import time
from test1 import request_test
from test1 import format_cookies
import json
import re
import json
proxies = {
    "http":"http://127.0.0.1:8888"
}
def bid_result(key):
    db_paimaiIds = request_test.db_paimaiIds
    url1 = 'http://bid.jd.com/json/current/englishquery'
    db_paimaiIds = request_test.db_paimaiIds
    url1_params = {"skuId": 0, "start": 0, "end": 0,
               "paimaiId": db_paimaiIds}
    cookies = format_cookies.format_cookies()
    res1 = requests.get(url1, params=url1_params, cookies=cookies, proxies=proxies)
    bid_result_text = res1.text
    print(bid_result_text)
    bid_result_re = re.match(".*?bidList\":\[({.*})].*?",bid_result_text,re.S).group(1)
    bid_result_json = json.loads(bid_result_re)
    testkey_value = bid_result_json[key]
    return testkey_value
print(bid_result("price"))