from selenium import webdriver
# import datetime
import time
import re

driver = webdriver.Chrome()

def get_loginCookies(uname, pwd):
    url_login = "https://passport.jd.com/new/login.aspx"
    driver.get(url_login)
    driver.find_element_by_link_text("账户登录").click()
    driver.find_element_by_name("loginname").send_keys(uname)
    driver.find_element_by_name("nloginpwd").send_keys(pwd)
    driver.find_element_by_id("loginsubmit").click()
    time.sleep(3)
    # get the session cookie
    cookie = [item["name"] + "=" + item["value"] for item in driver.get_cookies()]
    cookiestr = ';'.join(item for item in cookie)
    cookies_format = {}
    for line in cookiestr.split(";"):
        name, value = line.strip().split('=', 1)
        cookies_format[name] = value  # 为字典cookies添加内容
    driver.close()
    # now = datetime.datetime.now()
    # print (now.strftime('%Y-%m-%d %H:%M:%S'))
    # print ('login success')
    # print(cookiestr)
    return cookies_format
def save_cookie():
    # fh = open(r'cookies/cookie.txt','w')
    # cookies = str(get_loginCookies("jd_6e4cafd025ac1","chenlu15432"))
    # print(cookies)
    # fh.write(cookies)
    # fh.close()
    with open("cookies/cookie.txt","wb+") as f:
        for i in range(0,2):
            cookies = str(get_loginCookies("jd_6e4cafd025ac1", "chenlu15432"))
            print(cookies)
            f.write(cookies + "\n")
            f.close()
# print(get_loginCookies("jd_6e4cafd025ac1","chenlu15432"))
if __name__ == '__main__':
    save_cookie()