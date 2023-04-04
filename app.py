from flask import Flask, render_template, jsonify, request
from drive import Drive
from automation import Automation
from coordinates import Coordinates
from geocodeTree import GeocodeTree
import test_coordinates as tc
from cmritPath import CmritField

app = Flask(__name__)

driver = Drive()
gt = GeocodeTree()
master_graph = CmritField() # This 

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
    initPoint = Coordinates('basic_science', (12.96626, 77.71211))
    finalPoint = Coordinates('ganesha_statue', (12.96598, 77.71148))
    automate_drive = Automation(initPoint, finalPoint)
    automate_drive.automate_linear()
    return "a"


@app.route("/add_tree")
def tree():
    gt.add_tree([12.96620, 77.71203])
    gt.add_tree([12.96612, 77.71179])
    gt.add_tree([12.96603, 77.71156])
    return "a"


@app.route("/save")
def save():
    gt.save_and_return()
    return "a"

@app.route("/fetch-all-nodes")
def fetch_nodes():
    return jsonify(master_graph.return_all_nodes())

@app.route("/fetch-neighbours", methods=["POST"])
def fetch_neighbours():
    current_node = request.form.get("current_node")
    return jsonify(master_graph.return_adjacent_nodes(current_node))


##########################################
# for test purposes
# basic_science to ganesha_statue

"""
def test_stretch_1():
    start = tc.basic_science.point_name
    end = tc.ganesha_statue.point_name
    gt.add_tree(tc.tree1.point_coordinate, start, end)
    gt.add_tree(tc.tree2.point_coordinate, start, end)
    gt.add_tree(tc.tree3.point_coordinate, start, end)
    gt.save_and_return()


# ganesha_statue to hostel_turn
def test_stretch_2():
    start = tc.ganesha_statue.point_name
    end = tc.hostel_turn.point_name
    gt.add_tree(tc.tree4.point_coordinate, start, end)
    gt.add_tree(tc.tree5.point_coordinate, start, end)
    gt.add_tree(tc.tree6.point_coordinate, start, end)
    gt.save_and_return()


test_stretch_1()
test_stretch_2()
##########################################
"""


# TODO::Uncomment this when deploying it in RaspberryPi
# if __name__ == "__main__":
#     print("Inside Main")
# app.run(host='0.0.0.0', debug=True)
