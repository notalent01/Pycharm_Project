#!/usr/bin/python
#coding=utf-8
from multiprocessing import Queue
import threadpool
from multidb import get_ExpectPrice
from multidb import get_ProductName
from multidb import get_job_bytime
from multidb import auction_Product_new
from multidb import MyTimer

global my_queue
my_queue = Queue()

global thread_running
thread_running = 1

global thread_cout
thread_cout = 5

def deal_job(paramId):
    while 1:
        price_ = get_ExpectPrice.getPrice(paramId[1]) #此处的price是str类型，获取3天的最低价格
        print(paramId[1],price_)
        if int(price_) >= 500:
            print("id:", paramId[0], " price:", price_)
            auction_Product_new.run_bd(paramId[0],price_,paramId[1]) #传入三个参数：商品ID，最高期望价格（3天的），商品名称
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

def on_timer(param):
    print ("on_timer:",param)
    push_back_job(param)

if __name__ == '__main__':
    data = [i for i in range(thread_cout)]
    pool = threadpool.ThreadPool(thread_cout)
    requests = threadpool.makeRequests(test_func,data)
    [pool.putRequest(req) for req in requests]
    #创建/启动定时器
    job_timer = MyTimer.MyTimer(on_timer)
    job_timer.start()
    ##返回字典类型，比如mymap = {id1:名字1,id2:名字2....}
    mymap = get_ProductName.get_paramid_map()
    print("mymap的值为：",mymap)
    # 主要是获取'paimaiIds': '16078745-16079028-16078984-16078902' 这串参数，最终返回
    # 类似{'callback': 'jQuery1016440', 't': '1498787461396', '&_': '1498787461398', 'paimaiIds': '16078745-16079028-16078984-16078902'}
    params = get_ProductName.get_params_by_paramid_map(mymap)
    print("params的值为：",params)
    jobarry = get_job_bytime.obtain_value(params)
    print("jobarry的值为：",jobarry)
    for ii in jobarry:
        # print("ii的值为",ii)
        if ii[0] in mymap:
            # print(ii[0],ii[1])
            # ii[1] --商品的剩余时间    表示多少秒后触发回调
            # [ii[0], mymap[ii[0]]] : ii[0]表示商品的ID，mymap[ii[0]]表示根据商品的ID得出商品名称 表示回调时传出的参数
            job_timer.setTimer(ii[1]-8000, [ii[0], mymap[ii[0]]])
    while 1:
        content = input("input:")
        if content == "exit":
            break

    job_timer.exitthread()
    job_timer.join()

    exit_thread()
    pool.wait()
    print("process exit")
