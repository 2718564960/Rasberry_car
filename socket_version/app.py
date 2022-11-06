#!/usr/bin/env python
from flask import Flask, render_template, Response, request
# from BasicMove_ import BasicMove
from car import BasicMove as CarMove
import  RPi.GPIO as GPIO
import cv2
from flask_socketio import SocketIO
import socket

app = Flask(__name__)
app.config['SECRET_KEY'] = 'test'
socketio = SocketIO(app)

carmove = CarMove()
carmove.start()

@app.route('/')
def index():
    return render_template('index.html', host_ip = get_host_ip())

def gen(camera):
    while True:
        ## frame = camera.get_frame()
        ret, frame = camera.read()
        ret, jpeg = cv2.imencode('.jpg', frame)
        bb = jpeg.tobytes()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + bb + b'\r\n')
        
def get_host_ip():
    try:
        serverSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        serverSocket.connect(("8.8.8.8", 80))
        localIP = serverSocket.getsockname()[0]
        print("localIP" + str(localIP))
    finally:
        return "5c8bdc9b.r3.vip.cpolar.cn"
        #return localIP

@app.route('/video_feed')
def video_feed():
    return Response(gen(cv2.VideoCapture(0)),
                    mimetype='multipart/x-mixed-replace; boundary=frame')
    
@app.route('/dbd', methods = ['GET', 'POST'])
def deal():
    
    print("123")
    print(request.data)
    # if request.data == "F":
        # BasicMove().t_up(50,3)
    return render_template("index.html")

@app.route('/dbu', methods = ['GET', 'POST'])
def deal2():
    print("abcd")
    # BasicMove().t_stop(3)
    return render_template("index.html")

@socketio.on('action')
def handle_message(msg):
    print('received message: ' + str(msg))
    action =msg['action']
    print(action) 

    if action == 'F':
        carmove.t_up(50)
    if action == 'R':
        carmove.t_right(50)
    if action == 'L':
        carmove.t_left(50)
    if action == 'B':
        carmove.t_down(50)
    if action == 'stop':
        carmove.t_stop()


if __name__ == '__main__':
    try :
        socketio.run(app,host='0.0.0.0')
    except KeyboardInterrupt:
        GPIO.cleanup()
    # app.run(host='0.0.0.0', threaded=True)