__author__ = 'jlu69'
from socket import *
from time import ctime
import threading
from time import sleep

PORT=21567
BUFSIZE=1024

class serverThread(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)

    def run(self):
        global PORT, BUFSIZE
        ADDR=('',PORT)
        tcpSerSock=socket(AF_INET, SOCK_STREAM)
        tcpSerSock.bind(ADDR)
        tcpSerSock.listen(5)
        while True:
            print 'waiting for connection ...'
            tcpCliSock,addr = tcpSerSock.accept()
            print '...connected from:',addr

            while True:
                data = tcpCliSock.recv(BUFSIZE)
                if not data:
                    break
                tcpCliSock.send('[%s] %s' % (ctime(),data))
        tcpSerSock.close()

class clientThread(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)

    def run(self):
        global PORT, BUFSIZE
        ADDR=('localhost',PORT)
        tcpCliSock=socket(AF_INET, SOCK_STREAM)
        tcpCliSock.connect(ADDR)

        while True:
            data = raw_input('> ')
            if not data:
                break;
            tcpCliSock.send(data)
            data = tcpCliSock.recv(BUFSIZE)
            if not data:
                break
            print data
        tcpCliSock.close()

if __name__ == '__main__':
    st = serverThread()
    st.start()
    sleep(1)
    sc = clientThread()
    sc.start()
    while True:
        if st.join() and  sc.join():
            break

