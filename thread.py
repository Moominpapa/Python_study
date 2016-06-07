__author__ = 'jlu69'

import threading
from time import sleep
thread_count = 10000
threads = []

class myThread(threading.Thread):
    def __init__(self, id):
        threading.Thread.__init__(self)
        self.id = id

    def run(self):
        print "thread id %d" % self.id
        sleep(1)


if __name__ == '__main__':
    for i in range(0, thread_count):
        t = myThread(i)
        threads.append(t)

    for i in range(0, thread_count):
        threads[i].start()

    print threading.active_count()
    for i in range(0, thread_count):
        threads[i].join()

    print 'all thread done'