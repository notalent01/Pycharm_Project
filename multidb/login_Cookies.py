from selenium import webdriver
import time
from multidb import get_userPwd
from multiprocessing import Queue
from time import ctime,sleep

def get_loginCookies(uname, pwd):
    driver = webdriver.Chrome()
    url_login = "https://passport.jd.com/new/login.aspx"
    driver.get(url_login)
    driver.find_element_by_link_text("账户登录").click()
    driver.find_element_by_name("loginname").clear()
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
    return cookies_format
def save_cookie(username,password):
    with open("cookies/cookie.txt","a") as f:
        cookies = str(get_loginCookies(username, password))
        print(cookies)
        f.write(cookies + "\n")
        f.close()
# print(get_loginCookies("jd_6e4cafd025ac1","chenlu15432"))
if __name__ == '__main__':
    userPwd = get_userPwd.get_user()
    for key in userPwd:
        save_cookie(key,userPwd[key])
    # driver.close()