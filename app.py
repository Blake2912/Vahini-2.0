from flask import Flask, render_template
from drive import Drive
from automation import Automation
from coordinates import Coordinates

app = Flask(__name__)

driver = Drive()


@app.route("/")
def render():
    return render_template("render.html")

# background process happening without any refreshing
@app.route('/forward')
def forward():
    driver.forward()
    return "a"


@app.route('/reverse')
def reverse():
    driver.reverse()
    return "a"


@app.route('/stop')
def stop():
    driver.stop()
    return "a"


@app.route('/left')
def left():
    driver.left()
    return "a"


@app.route('/right')
def right():
    driver.right()
    return "a"


@app.route("/automate_vehicle")
def automate_vehicle():
    # TODO:: Instantiate the class and call required functions
    finalPoint = Coordinates('basic_science',(12.96626,77.71211))
    initPoint = Coordinates('ganesha_statue',(12.96598,77.71148))
    automate_drive = Automation(initPoint,finalPoint)
    automate_drive.automate_linear()
    return "a"


# TODO::Uncomment this when deploying it in RaspberryPi
if __name__ == "__main__":
    current_coord = [0, 0]
    destination_coord = [12.964224333333334, 77.70739866666666]
#     app.run(host='0.0.0.0', debug=True)
