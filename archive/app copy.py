"""
The following parts are implemented in this code
 - Setting up of Flask Server (DONE)
 - Util functions for defining the car direction
 - Importing the QLearning model
 - Getting the damn thing running just by printing statements for now
"""
import random

from flask import Flask, render_template
from nn import neural_net
from math import pi, asin, cos, sqrt, atan2

import serial
import pynmea2
import numpy as np

# TODO::Uncomment this when deploying it in RaspberryPi
# import RPi.GPIO as GPIO

# TODO::Uncomment this when deploying it in RaspberryPi
"""
in1 = 24
in2 = 23
dir = 27 # 
pow = 17 # Running of stepper motor
GPIO.setmode(GPIO.BCM)
GPIO.setup(in1,GPIO.OUT)
GPIO.setup(in2,GPIO.OUT)
GPIO.setup(pow,GPIO.OUT)
GPIO.setup(dir,GPIO.OUT)

GPIO.output(in1,GPIO.LOW)
GPIO.output(in2,GPIO.LOW)
GPIO.output(dir,GPIO.LOW)
GPIO.output(pow,GPIO.HIGH)
"""

app = Flask(__name__)
NUM_SENSORS = 2  # Change the number of sensors according to the requirements while deploying
destination_coord = [0, 0]
current_coord = [0, 0]
cur_north = 0.0

t_stop_called = False


# UTIL FUNCTIONS
def ref():
    global cur_north
    # message = request.get_json(force=True)
    # direction = message['direction']
    f = open("./dir.txt", "r")
    cn = f.read()
    try:
        cur_north = float(cn)
    except:
        print("Current Location is taken as 0")
        cur_north = 90.0
        pass
    #    print("cur"+str(cur_north))
    return cur_north


def get_cur():
    global current_coord
    try:
        port = "/dev/ttyAMA0"
        ser = serial.Serial(port, baudrate=9600, timeout=0.5)
        data_out = pynmea2.NMEAStreamReader()
        new_data = ser.readline()
        new_data = str(new_data)

        new_data = new_data[6:len(new_data) - 9]
        if new_data[0:6] == "$GPRMC":
            new_msg = pynmea2.parse(new_data)
            lat = new_msg.latitude
            lng = new_msg.longitude
            current_coord[0] = lat
            current_coord[1] = lng
    except:
        print("Hardware not found so emulating the hardware")
        # TODO:: Write code to negate the coordinates
        if current_coord[0] > destination_coord[0]:
            current_coord[0] -= random.randint(0, 10)
        if current_coord[1] > destination_coord[1]:
            current_coord[1] -= random.randint(0, 6)
        current_coord[0] += random.randint(0, 6)
        current_coord[1] += random.randint(0, 6)
        print("Current coordinates x:{0} y:{1}".format(current_coord[0],current_coord[1]))


def distance(lat1, lon1, lat2, lon2):
    p = pi / 180
    a = 0.5 - cos((lat2 - lat1) * p) / 2 + cos(lat1 * p) * cos(lat2 * p) * (1 - cos((lon2 - lon1) * p)) / 2
    return 12742 * asin(sqrt(a))


def frame_step(action):
    global destination_coord
    global current_coord
    global cur_north
    global t_stop_called

    get_cur()
    if action == 0:  # Turn left.
        left()
    elif action == 1:  # Turn right
        right()

    dx = destination_coord[1] - current_coord[1]
    dy = destination_coord[0] - current_coord[0]
    rad = atan2(dy, dx)
    deg = rad * (180 / 3.141592)
    # LOK-US
    # correction_angle = deg + cur_north
    if deg < 0:
        deg += 360

    cur_north = ref()
    print("mobile " + str(cur_north) + "co-incline " + str(deg))
    correction_angle = abs(deg - cur_north)
    print("correct_angle:{0}".format(correction_angle))
    # correction_angle = (abs(correction_angle))
    dis = distance(destination_coord[0], destination_coord[1], current_coord[0], current_coord[1])
    print("dis" + str(dis))
    normalized_readings = []
    dis = dis * 1000
    normalized_readings.append(dis / 20)
    normalized_readings.append((correction_angle))
    state = np.array([normalized_readings])

    if int(dis) < 0.15:
        reward = 200
        t_stop_called = True
        stop()
    else:
        if correction_angle > 30:
            reward = -1 * int(dis / 20) - (int(abs(correction_angle) / 2))
            reward = int(reward / 10)
        else:
            reward = 20 - 1 * int(dis / 20) - (int(abs(correction_angle))) + 30
            reward = int(reward / 10)

    print("Reward", reward)
    return reward, state


@app.route("/")
def render():
    return render_template("render.html")


# background process happening without any refreshing
@app.route('/forward')
def forward():
    print("forward")
    # set direction via main motor using relay pin 23 to relay
    # TODO::Uncomment this when deploying it in RaspberryPi
    # GPIO.output(in1, GPIO.LOW)
    # GPIO.output(in2, GPIO.LOW)
    return "a"


@app.route('/reverse')
def back():
    print("backward")
    # TODO::Uncomment this when deploying it in RaspberryPi
    # GPIO.output(in1, GPIO.LOW)
    # GPIO.output(in2, GPIO.HIGH)
    # set direction via of main motor using relay 23 to relay
    # Low means short... High means open
    return "a"


@app.route('/stop')
def stop():
    print("stop")
    # set pwm speed to zero pin 27
    # Cutting in1 i.e. power/enable
    # TODO::Uncomment this when deploying it in RaspberryPi
    # GPIO.output(in1, GPIO.HIGH)
    # GPIO.output(pow, GPIO.HIGH)
    return "a"


@app.route('/left')
def left():
    # set direction via servo pin 24 via relay
    # TODO::Uncomment this when deploying it in RaspberryPi
    # GPIO.output(pow, GPIO.LOW)  # LOW means ON Here...
    # GPIO.output(dir, GPIO.LOW)
    print("left triggered")
    return "a"


@app.route('/right')
def right():
    # set direction via servo pin 24 via relay
    # TODO::Uncomment this when deploying it in RaspberryPi
    # GPIO.output(pow, GPIO.LOW)
    # GPIO.output(dir, GPIO.HIGH)
    print("right triggered")
    return "a"


@app.route("/automate_vehicle")
def automate_vehicle():
    global t_stop_called
    # TODO:: Write code to orient the vehicle first and then move the vehicle
    # Do nothing to get initial.
    _, state = frame_step((2))
    saved_model = 'saved-models/128-128-64-50000-100000.h5'
    model = neural_net(NUM_SENSORS, [128, 128], saved_model)
    while True:
        # Choose action.
        action = (np.argmax(model.predict(state, batch_size=1)))
        # Take action.
        _, state = frame_step(action)

        if t_stop_called:
            break

    return "a"


# TODO::Uncomment this when deploying it in RaspberryPi
if __name__ == "__main__":

    current_coord = [0, 0]
    destination_coord = [12.964224333333334, 77.70739866666666]
#     app.run(host='0.0.0.0', debug=True)
