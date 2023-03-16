# TODO::Uncomment this when deploying it in RaspberryPi
# import RPi.GPIO as GPIO


class Drive:
    def __init__(self):
        print("Inside Drive Class")
        # Add any attributes required
        # TODO::Uncomment the below lines of code
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
    
    def forward(self):
        print("forward")
        # set direction via main motor using relay pin 23 to relay
        # TODO::Uncomment this when deploying it in RaspberryPi
        # GPIO.output(in1, GPIO.LOW)
        # GPIO.output(in2, GPIO.LOW)
    
    def reverse(self):
        print("reverse")
        # TODO::Uncomment this when deploying it in RaspberryPi
        # GPIO.output(in1, GPIO.LOW)
        # GPIO.output(in2, GPIO.HIGH)
        # set direction via of main motor using relay 23 to relay
        # Low means short... High means open
    
    def stop(self):
        print("stop")
        # set pwm speed to zero pin 27
        # Cutting in1 i.e. power/enable
        # TODO::Uncomment this when deploying it in RaspberryPi
        # GPIO.output(in1, GPIO.HIGH)
        # GPIO.output(pow, GPIO.HIGH)
    
    def left(self):
        # set direction via servo pin 24 via relay
        # TODO::Uncomment this when deploying it in RaspberryPi
        # GPIO.output(pow, GPIO.LOW)  # LOW means ON Here...
        # GPIO.output(dir, GPIO.LOW)
        print("left triggered")
    
    def right(self):
        # set direction via servo pin 24 via relay
        # TODO::Uncomment this when deploying it in RaspberryPi
        # GPIO.output(pow, GPIO.LOW)
        # GPIO.output(dir, GPIO.HIGH)
        print("right triggered")
