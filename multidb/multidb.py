#coding=utf-8
# from queue import Queue
from multiprocessing import Queue
from threading import Thread
from time import ctime,sleep
import random
import threadpool
from multidb import *

global my_queue
my_queue = Queue()

global thread_running
thread_running = 1

global thread_cout
thread_cout = 20

def deal_job(paramId):
    while 1:
        print ("id:", paramId[0]," name:",paramId[1])
        break


def test_func(L):
    while thread_running:
        get_data = my_queue.get()
        if(get_data == "exit"):
            break;
        deal_job(get_data)
    print ("threak exit,id:",L)
    return ""

def exit_thread():
    for i in range(0,thread_cout):
        push_back_job(["exit","exit"])

def push_back_job(url):
    my_queue.put(url)

if __name__ == '__main__':
    data = [i for i in range(thread_cout)]
    pool = threadpool.ThreadPool(thread_cout)
    requests = threadpool.makeRequests(test_func,data)
    [pool.putRequest(req) for req in requests]

    for i in range(1,2):
        # 获取拍卖页面的商品IDs
        mymap = get_ProductName.get_paramid_map()
        # 获取参数
        params = get_ProductName.get_params_by_paramid_map(mymap)
        #将参数带到查询时间页面，查询剩余时间少于规定时间，返回符合条件的商品ID数组
        jobarry = get_job_bytime.obtain_value(params)
        #遍历符合条件的商品ID，分别push到各个任务中
        for ii in jobarry:
            push_back_job([ii,mymap[ii]])

    exit_thread()
    pool.wait()
