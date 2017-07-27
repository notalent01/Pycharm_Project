import requests
import re
from bs4 import BeautifulSoup
from multidb import get_ExpectPrice
#返回字典类型，比如mymap = {id1:名字1,id2:名字2....}
def get_paramid_map():
    url = "http://dbd.jd.com/auctionList.html"
    #取limit的值商品数量
    params = {"t":"","auctionType":"5","sortField":"2","productCateId":"2000","limit":"30","page":"1"}
    rel = requests.get(url,params=params)
    rel.encoding = rel.apparent_encoding
    html = rel.text
    soup = BeautifulSoup(html,"html.parser")
    mymap = {}

    for tag in soup.find_all("a",href=re.compile("^//dbditem.jd.com/[0-9]+")):
        herf=tag.get('href')
        # 取出商品的Id
        key=herf[17:]
        # 取出商品的名字
        bookname = tag.get_text()
        # 根据商品的名字描述，获取商品的价格（此方法默认取最小天数3天，如果没有3天，则依次往高天数）
        # db_price = get_ExpectPrice.getPrice(bookname)
        if not tag.get("target"):
            continue
        if (len(bookname) < 1):
            continue
        #过滤关键词
        if re.search(u"(壳|背包|数据线|转接头|支架|保护套|自拍杆|相纸|充电宝|充电器|耳机)", bookname):
            print("\033[1;35m过滤掉的数据：\033[0m" + bookname)
            continue
        # if len(db_price) < 1:
        #     continue
        #取价格少于500元的，取商品价格的接口存在性能问题，可能会导致程序运行时间较慢
        # if int(db_price) >= 500:
        if key not in mymap :
            mymap[key] = bookname
    return mymap
# print(get_paramid_map())

#主要是获取'paimaiIds': '16078745-16079028-16078984-16078902' 这串参数，最终返回
# 类似{'callback': 'jQuery1016440', 't': '1498787461396', '&_': '1498787461398', 'paimaiIds': '16078745-16079028-16078984-16078902'}
def get_params_by_paramid_map(mymap): #返回一个url钟的参数，参见阐述ret
    ret = ""
    params = ""
    i = 0
    #遍历mymap的key，取出key，并且用"-"将其连接起来
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
# print(mymap)
# for key in mymap:
#     print ("key:",key," value:",mymap[key])
#
# print (get_params_by_paramid_map(mymap))