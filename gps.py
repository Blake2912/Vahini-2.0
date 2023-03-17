# This module will have the function which will get the gps coordinates from the GPS Module
import serial
import io
import time
import string
import pynmea2

class Gps:
    def __init__(self):
        self.port = "/dev/ttyAMA0"
        self.ser = serial.Serial(self.port, baudrate=9600, timeout=0.5)
        self.sio = io.TextIOWrapper(io.BufferedRWPair(self.ser, self.ser))
    
    def get_gps_coordinates(self):
        """
        Params: None
        Returns: (Lat: float, Lng: float) 
        """
        try:
            file1 = open("/home/pi/gps/LatLong.txt", "a")
            line = self.sio.readline()
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
                return (lat_dec,long_dec)

        except serial.SerialException as e:
            print('Device error : {}'.format(e))
            return (-9999,-9999) # Signifies error 

        except pynmea2.ParseError as e:
            print("Parse error {}".format(e))
            return (-9999,-9999) # Signifies error
