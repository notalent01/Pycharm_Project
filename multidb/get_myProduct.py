import requests
from multidb import format_cookies
import re
from bs4 import BeautifulSoup

def my_getProduct(i):
    mybook = {}
    login_status = ""
    url = "https://dbd.jd.com/myAuctionList.html"
    cookies = format_cookies.format_cookies(i)
    my_name = format_cookies.get_cookieUser(i)
    rel = requests.get(url,cookies = cookies)
    html = rel.text
    soup = BeautifulSoup(html,"html.parser")
    for tag in soup.find_all("input",id="loginname"):
        login_status = tag.get('placeholder')
    if len(login_status) > 1:
        return (my_name,login_status)
    for tag in soup.find_all("a",href=re.compile("^//dbditem.jd.com/[0-9]+")):
        herf = tag.get('href')
        key = herf[17:]
        bookname = tag.get_text()
        if not tag.get("target"):
            continue
        if (len(bookname) < 1):
            continue
        if key not in mybook:
            mybook[key] = bookname
    return (my_name,mybook)

with open("cookies/cookie.txt","r") as f:
    for i in range(0,len(f.readlines())):
        (mybook_name,my_book) = my_getProduct(i)
        if type(my_book) == str:
            print(mybook_name,my_book,"需要重新登录")
        if type(my_book) == dict:
            if len(my_book) < 1:
                print(mybook_name,my_book,"我没买到任何商品")
            else:
                print(mybook_name,"\033[1;35m{}\033[0m".format(my_book))
