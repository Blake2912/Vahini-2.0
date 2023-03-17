import serial
import io
import time
import string
import pynmea2
port = "/dev/ttyAMA0"
ser = serial.Serial(port, baudrate=9600, timeout=0.5)
sio = io.TextIOWrapper(io.BufferedRWPair(ser, ser))
while 1:
    try:
        file1 = open("/home/pi/gps/LatLong.txt", "a")
        line = sio.readline()
        msg = pynmea2.parse(line)
        if isinstance(msg, pynmea2.GGA):

            file1.write("Latitude : "+str(msg.latitude)+" " +
                        str(msg.latitude_minutes)+" "+str(msg.latitude_seconds)+"\n")
            file1.write("Longitude : "+str(msg.longitude)+" " +
                        str(msg.longitude_minutes)+" "+str(msg.longitude_seconds)+"\n\n")

            lat_dec = float(msg.latitude) + float(msg.latitude_minutes) / \
                60 + float(msg.latitude_seconds) / 3600
            long_dec = float(msg.longitude) + float(msg.longitude_minutes) / \
                60 + float(msg.longitude_seconds) / 3600

            file1.write("{}, {}\n".format(lat_dec, long_dec))

    except serial.SerialException as e:
        print('Device error : {}'.format(e))
        break
    except pynmea2.ParseError as e:
        print("Parse error {}".format(e))
        continue
