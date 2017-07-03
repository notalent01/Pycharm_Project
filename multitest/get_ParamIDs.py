import requests
import re
import time
from bs4 import BeautifulSoup

url = "http://dbd.jd.com/auctionList.html"
params = {"t":"","auctionType":"5","sortField":"2","productCateId":"2000","limit":"40","page":"1"}
#cookies = format_cookies.format_cookies()
rel = requests.get(url,params=params)
html = rel.text
soup = BeautifulSoup(html,"html.parser")

def get_list_url_params():
        arr = []
        urlstr = ""
        for tag in soup.find_all("a",href=re.compile("^//dbditem.jd.com/[0-9]+")):
                herf=tag.get('href')
                key=herf[17:]
                if key not in arr :
                        arr.append(key)

        for ii in arr :
                urlstr += "-"
                urlstr += ii
        if len(urlstr) > 0:
                urlstr = urlstr[1:]
                # current_localtime = round(time.time() * 1000)
                url_params = {"paimaiIds":urlstr,"callback":"showData","t":"1498787461396","callback":"jQuery1016440","&_":"1498787461398"}
        else:
                print
                "[ERROR] can not find paimaiIds"
                url = ""
        return url_params
# print(get_list_url_params())
