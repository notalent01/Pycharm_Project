from selenium import webdriver
import time
# from multidb import get_userPwd
# from multiprocessing import Queue
# from time import ctime,sleep

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
    url_home = "https://home.jd.com/"
    driver.get(url_home)
    jingdou = driver.find_element_by_xpath("//*[@id='JingdouCount']/em").text
    print(jingdou)
    print(type(jingdou))
    driver.close()
get_loginCookies("jd_55425be715341","jd123456")