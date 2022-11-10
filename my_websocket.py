from time import sleep
from config import SERVER
from drinker import user_touch, user_drink, get_token,init,clear
import requests
import socketio
import multiprocessing
def debug(s):
    print("[debug]",s,"\n")

def dispenser_proc(q):
    token = get_token()
    init()
    request_body = {'dispenserToken' : token}
    mode = 0 
    while(True):

        userid = user_touch()
        debug(str(userid))

        if q.qsize() > 0:
            mode = q.get()

        debug("mode: "+str(mode))
        if mode == '0':

            url = SERVER + '/drinker/' + str(userid)
            print(url, request_body)
            res = requests.post(url, data = request_body)
            print(res.text)

        elif mode == '1':
            user_drink()
            url = SERVER + '/drinker/' + str(userid) + '/drink'
            print(url, request_body)
            res = requests.patch(url, data = request_body)
            print(res.text)
            sleep(3)


sio = socketio.Client()
q = multiprocessing.Queue()

@sio.event
def connect():
    print("I'm connected!")

@sio.event
def connect_error(data):
    print("The connection failed!")

@sio.event
def disconnect():
    print("I'm disconnected!")

@sio.on('start')
def start_dispenser():
    q.put('1')
    print("start dispenser")

@sio.on('stop')
def end_dispenser():
    q.put('0')
    print("end dispenser")

def main():

# 'https://api.soju.tk:443
    q.put('0')
    p = multiprocessing.Process(target = dispenser_proc, args =(q,))
    
    sio.connect(SERVER + '?dispenserToken=1234', socketio_path='/socket/dispenser')

    p.start()
    p.join()
# while True:
#
#     sio.wait()


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        clear()
