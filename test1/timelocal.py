import time
import requests
from test1 import format_cookies
proxies = {
    "http":"http://127.0.0.1:8888"
}
db_paimaiIds = "15738678"
url1 = 'http://dbditem.jd.com/services/currentList.action'
current_localtime = int(round(time.time() * 1000))
next_localtime = str(current_localtime + 1)
callback = "jsonp_" + str(current_localtime)
url1_params = {"paimaiIds": db_paimaiIds, "curPaimaiId": db_paimaiIds, "callback": callback,
               "_": next_localtime}
cookies = format_cookies.format_cookies()
res1 = requests.get(url1, params=url1_params, cookies=cookies,proxies=proxies)
print(res1.text)