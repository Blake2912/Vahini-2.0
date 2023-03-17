import serial
import io
import time
import string
import pynmea2
port="/dev/ttyAMA0"
ser=serial.Serial(port,baudrate=9600,timeout=0.5)
sio  = io.TextIOWrapper(io.BufferedRWPair(ser,ser))
while 1:
    try:
        file1 = open("/home/pi/gps/LatLong.txt","a")
        line = sio.readline()
        msg = pynmea2.parse(line)
        if isinstance(msg,pynmea2.GGA):
            
            print(str(msg.lat))
            print(str(msg.latitude)+""+str(msg.latitude_minutes)+""+str(msg.latitude_seconds))
            #print(str(msg.long))
            #print(str(msg.longitude)+""+str(msg.longitude_minutes)+""+str(msg.longitude_seconds))
            file1.write("Latitude : "+str(msg.latitude)+" "+str(msg.latitude_minutes)+" "+str(msg.latitude_seconds)+"\n")
            file1.write("Longitude : "+str(msg.longitude)+" "+str(msg.longitude_minutes)+" "+str(msg.longitude_seconds)+"\n\n")
    except serial.SerialException as e:
        print('Device error : {}'.format(e))
        break
    except pynmea2.ParseError as e:
        print("Parse error {}".format(e))
        continue
