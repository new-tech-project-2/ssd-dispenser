import socketio

sio = socketio.Client()

@sio.event
def connect():
    print("I'm connected!")

@sio.event
def connect_error(data):
    print("The connection failed!")

@sio.event
def disconnect():
    print("I'm disconnected!")

@sio.on('startDispenser')
def start_dispenser(data):
    pass

@sio.on('endDispenser')
def end_dispenser(data):
    pass

sio.connect('https://api.soju.tk:443', auth='1234' , socketio_path='/socket/dispenser')
sio.wait()