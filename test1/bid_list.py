import requests
import time
from test1 import request_test
from test1 import format_cookies
import json
import re
proxies = {
    "http":"http://127.0.0.1:8888"
}
db_paimaiIds = request_test.db_paimaiIds
url1 = 'http://bid.jd.com/json/current/englishquery'
db_paimaiIds = request_test.db_paimaiIds
url1_params = {"skuId": 0, "start": 0, "end": 9,
               "paimaiId": db_paimaiIds}
cookies = format_cookies.format_cookies()
res1 = requests.get(url1, params=url1_params, cookies=cookies, proxies=proxies)
a1 = res1.text
print(a1)
testre = re.match(".*?{{.*}}.*",a1,re.S).group()
print(testre)