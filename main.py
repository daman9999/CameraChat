from vidstream import CameraClient
from vidstream import StreamingServer

import threading
import time

threadLock = threading.Lock()
#using "ifconfig" when running on local machine to find out addresss

#write
CLIENT_ADDRESS= "192.168.245.1"
#write
SERVER_ADDRESS =   "192.168.245.1"
PORT = 9999
c_PORT =9998

#server will recieve
RECIEVING_SERVER =  StreamingServer(SERVER_ADDRESS,PORT)
#client will send data to server
CLIENT_SENDING = CameraClient(CLIENT_ADDRESS,c_PORT)

t1 = threading.Thread(target = RECIEVING_SERVER.start_server)
t2 = threading.Thread(target = CLIENT_SENDING.start_stream)

threadLock.acquire()      
t1.start();      
threadLock.release()

threadLock.acquire()      
t2.start();      
threadLock.release()


while input("") != "STOP":
    continue


RECIEVING_SERVER.stop_server()
CLIENT_SENDING.stop_stream()
