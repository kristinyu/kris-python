import threading
import time

tag=0

threadLock=threading.Lock()

class krisThread(threading.Thread):
    def __init__(self,threadId,name,counter):
        threading.Thread.__init__(self)
        self.name=name
        self.counter=counter
        self.threadId=threadId
    def run(self):
        print("thread start"+self.name)
        # get lock
        threadLock.acquire()
        print_time(self.name,self.counter,6)
        print("退出线程"+self.name)
        threadLock.release()

def print_time(threadName,delay,counter):
    while counter:
        if tag:
            threadName.exit()
        time.sleep(delay)
        print("%s:%s" % (threadName,time.ctime(time.time())))
        counter-=1

threadOne=krisThread(1,"one",1)
threadTwo=krisThread(2,"two",1)

threadOne.start()
threadTwo.start()
threadOne.join()
threadTwo.join()

print("end")




