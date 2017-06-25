import http.client
import time
import os


def get_webservertime(host):
    conn = http.client.HTTPConnection(host)
    conn.request("GET", "/")
    r = conn.getresponse()
    # r.getheaders() #获取所有的http头
    ts = r.getheader('date')  # 获取http头date部分
    print(ts)

    # 将GMT时间转换成北京时间
    ltime = time.strptime(ts[5:25], "%d %b %Y %H:%M:%S")
    # print(ltime)
    ttime = time.localtime(time.mktime(ltime) + 8 * 60 * 60)
    # print(ttime)
    server_dat = "%u-%02u-%02u" % (ttime.tm_year, ttime.tm_mon, ttime.tm_mday)
    server_tm = "%02u:%02u:%02u" % (ttime.tm_hour, ttime.tm_min, ttime.tm_sec)
    print("京东服务器时间是： " + server_dat,server_tm)
    local_time1 = time.localtime(time.time())
    # print(local_time1)
    local_dat = "%u-%02u-%02u" % (local_time1.tm_year,local_time1.tm_mon, local_time1.tm_mday)
    local_tm = "%02u:%02u:%02u" % (local_time1.tm_hour, local_time1.tm_min, local_time1.tm_sec)
    print("我本机的时间是： " + local_dat,local_tm)
    #将时间转化为时间戳
    local_time = local_dat + " " + local_tm
    server_time = server_dat + " " + server_tm
    print(type(local_time))
    print(server_time)
    local_timestamp = time.mktime(time.strptime(local_time, '%Y-%m-%d %H:%M:%S'))
    print(local_timestamp)
    # server_timestampArray = time.mktime(time.strptime(server_time, '%Y-%m-%d %H:%M:%S'))
    # local_timestamp = time.mktime(local_timestampArray)
    # server_timestamp = time.mktime(server_timestampArray)
    # print(server_timestamp)
    # print(local_timestamp)
get_webservertime('dbditem.jd.com')
