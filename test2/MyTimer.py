# -*- coding: UTF-8 -*-
import time
import  threading

class MyTimer(threading.Thread):
    jobs_ = []
    running_ = True
    callback_ = {}
    threadLock = threading.Lock()
    def __init__(self, callback):
        threading.Thread.__init__(self)
        self.callback_ = callback

    def run(self):
        while self.running_:
            cur_time = time.time()
            self.threadLock.acquire()
            while len(self.jobs_) > 0:
                if self.jobs_[0]["key"] > cur_time:
                    break
                self.callback_(self.jobs_[0]["param"])
                del self.jobs_[0]
            self.threadLock.release()
            time.sleep(0.01)


#sec     表示多少秒后触发回调
#param  表示回调时传出的参数
    def setTimer(self, milsec, param):
        expire = time.time()
        expire += float(milsec)/1000
        desc = {}
        desc["key"] = expire
        desc["param"] = param
        self.threadLock.acquire()
        self.jobs_.append(desc)
        self.jobs_ = sorted(self.jobs_, key=lambda x:x['key'])
        self.threadLock.release()

    def exitthread(self):
        print ("exitthread")
        self.running_ = False

#test code
def on_timer(param):
    print ("on_timer:",param)

print ("test begin")
#创建定时器对象
jobTimer = MyTimer(on_timer)
#启动定时器
jobTimer.start()

#添加定时器任务
jobTimer.setTimer(5030,"5030")
jobTimer.setTimer(4400, "4400")
jobTimer.setTimer(6070, "6070")
jobTimer.setTimer(2900, "2900")
jobTimer.setTimer(6200, "6200")
time.sleep(10)

#退出定时器
jobTimer.exitthread()
jobTimer.join()