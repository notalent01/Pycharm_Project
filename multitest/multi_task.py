#!/usr/bin/python
#coding=utf-8
# from queue import Queue
from multiprocessing import Queue
from threading import Thread
from time import ctime,sleep
import random
import threadpool
from multitest import get_job_bytime
from multitest import get_ParamIDs

global my_queue
my_queue = Queue()

global thread_running
thread_running = 1

global thread_cout
thread_cout = 10

def deal_job(url):
	print ("job:",url)

def func(L):
	while thread_running:
		get_data = my_queue.get()
		if(get_data == "exit"):
			break
		deal_job(get_data)
	print ("threak exit,id:",L)

def exit_thread():
	my_queue.put("exit")
	for i in range(1,10):
		my_queue.put("exit")

def push_back_job(url):
	my_queue.put(url)

if __name__ == '__main__':
	data = [i for i in range(10)]
	pool = threadpool.ThreadPool(10)
	requests = threadpool.makeRequests(func,data)
	[pool.putRequest(req) for req in requests]
	# print("vbbb")
	# push_back_job("aaa")
	sleep(10)
	#for test only loop two
	for ii in range(1,2):
		#fetch get remainTime url
		joburl = get_ParamIDs.get_list_url_params()
		print(joburl)
		#fetch get remainTime (0,10] job
		joinurl = get_job_bytime.obtain_value(joburl)
		for ii in joinurl:
			push_back_job(ii)
			print(ii)
		sleep(10)
	exit_thread()
	pool.wait()
