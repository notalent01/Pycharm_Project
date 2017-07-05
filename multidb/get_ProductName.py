import requests
import re
from bs4 import BeautifulSoup
def get_paramid_map():
    url = "http://dbd.jd.com/auctionList.html"
    params = {"t":"","auctionType":"5","sortField":"2","productCateId":"2000","limit":"5","page":"1"}
    rel = requests.get(url,params=params)
    rel.encoding = rel.apparent_encoding
    html = rel.text
    soup = BeautifulSoup(html,"html.parser")
    mymap = {}

    for tag in soup.find_all("a",href=re.compile("^//dbditem.jd.com/[0-9]+")):
        herf=tag.get('href')
        key=herf[17:]
        bookname = tag.get_text()
        if (len(bookname) < 1):
            continue
        if key not in mymap :
            mymap[key] = bookname
    return mymap
# print(get_paramid_map())
def get_params_by_paramid_map(mymap):
    ret = ""
    params = ""
    i = 0
    for key in mymap:
        if( i != 0):
            params += "-"
        params += key
        i = i + 1

    if(len(params) < 1):
        return ret

    ret = {"paimaiIds": params, "callback": "showData", "t": "1498787461396", "callback": "jQuery1016440","&_": "1498787461398"}

    return ret

#test code
# mymap = get_paramid_map()
# for key in mymap:
#     print ("key:",key," value:",mymap[key])
#
# print (get_params_by_paramid_map(mymap))