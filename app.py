from flask import Flask, render_template
from drive import Drive
from automation import Automation
from coordinates import Coordinates
from geocodeTree import GeocodeTree

app = Flask(__name__)

driver = Drive()
gt = GeocodeTree()


@app.route("/")
def render():
    return render_template("render.html")

@app.route('/map')
def map():
    return render_template('map.html')

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
    initPoint = Coordinates('basic_science', (12.96626, 77.71211))
    finalPoint = Coordinates('ganesha_statue', (12.96598, 77.71148))
    automate_drive = Automation(initPoint, finalPoint)
    automate_drive.automate_linear()
    return "a"


@app.route("/add_tree")
def tree():
    gt.add_tree([12.96691, 77.71112])
    return "a"


@app.route("/save")
def save():
    gt.save_and_return()
    return "a"


# TODO::Uncomment this when deploying it in RaspberryPi
if __name__ == "__main__":
    print("Inside Main")
    # app.run(host='0.0.0.0', debug=True)
