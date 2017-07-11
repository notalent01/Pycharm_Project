#!/usr/bin/python
#coding=utf-8
from threading import Thread
from multiprocessing import Queue
from time import ctime,sleep
import threadpool
from multidb import get_ExpectPrice
from multidb import get_ProductName
from multidb import get_job_bytime
from multidb import auction_Product

global my_queue
my_queue = Queue()

global thread_running
thread_running = 1

global thread_cout
thread_cout = 5

def deal_job(paramId):
    while 1:
        price_ = get_ExpectPrice.getPrice(paramId[1], u"3天")
        print("id:", paramId[0], " price:", price_)
        auction_Product.run_bd(paramId[0],price_)
        # auction_Product.run_bd(paramId[0],price_)
        break


def test_func(L):
    while thread_running:
        get_data = my_queue.get()
        if(get_data[0] == "exit"):
            break;
        deal_job(get_data)
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

    for i in range(0,1):
        mymap = get_ProductName.get_paramid_map()
        params = get_ProductName.get_params_by_paramid_map(mymap)
        jobarry = get_job_bytime.obtain_value(params)
        for ii in jobarry:
            if ii in mymap:
                push_back_job([ii,mymap[ii]])
        sleep(10)

    exit_thread()
    pool.wait()
    print("process exit")
