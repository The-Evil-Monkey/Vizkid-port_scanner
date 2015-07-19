import threading
import Queue
import socket


q = Queue.Queue()

target = 'youtube.com'

def pscan(port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        con = s.connect((target, port))
        print ("Port ", port, 'is open')
        con.close()
    except:
        pass

def threaded():
    while True:
        w = q.get()
        pscan(w)
        q.task_done()

for x in range(100):
    t = threading.Thread(target= threaded)
    t.daemon = True
    t.start()


for w in range(1,201):
    q.put(w)

q.join()

__author__ = 'vishket.shriwas'
