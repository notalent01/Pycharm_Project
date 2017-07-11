from selenium import webdriver
import time
# from pyvirtualdisplay import Display

driver = webdriver.Chrome()

def get_loginCookies(uname, pwd):
    url_login = "https://passport.jd.com/new/login.aspx"
    # with Display(backend="xvfb", size=(1440, 900)):
    driver.get(url_login)
    # driver.find_element_by_link_text("你好，请登录").click()
    # time.sleep(3)
    driver.find_element_by_link_text("账户登录").click()
    driver.find_element_by_name("loginname").send_keys(uname)
    driver.find_element_by_name("nloginpwd").send_keys(pwd)
    driver.find_element_by_id("loginsubmit").click()
    time.sleep(3)
    # get the session cookie
    cookie = [item["name"] + "=" + item["value"] for item in driver.get_cookies()]
    cookiestr = ';'.join(item for item in cookie)
    driver.close()
    # now = datetime.datetime.now()
    # print (now.strftime('%Y-%m-%d %H:%M:%S'))
    # print ('login success')
    # print(cookiestr)
    return cookiestr

print(get_loginCookies("jd_6e4cafd025ac1","chenlu15432"))
