from flask import Flask, render_template, jsonify, request
from drive import Drive
from automation import Automation
from coordinates import Coordinates
from geocodeTree import GeocodeTree
import test_module.test_coordinates as tc
from cmritPath import CmritField
from test_module.test import TestTree

app = Flask(__name__)

driver = Drive()
gt = GeocodeTree()
master_graph = CmritField()  # This


@app.route("/")
def render():
    return render_template("render.html")


@app.route('/tree')
def map():
    return render_template('tree.html')

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


@app.route("/add_tree", methods=["POST"])
def tree():
    start_node = request.get_json().get("start_node")
    end_node = request.get_json().get("end_node")
    TestTree(gt, start_node, end_node)
    return 'a'


@app.route("/save")
def save():
    gt.save_and_return()
    return "a"


@app.route("/fetch-all-nodes")
def fetch_nodes():
    return jsonify(master_graph.return_all_nodes())


@app.route("/fetch-neighbours", methods=["POST"])
def fetch_neighbours():
    current_node = request.get_json().get("current_node")
    return jsonify(master_graph.return_adjacent_nodes(current_node))


# TODO::Uncomment this when deploying it in RaspberryPi
# if __name__ == "__main__":
#     print("Inside Main")
# app.run(host='0.0.0.0', debug=True)
