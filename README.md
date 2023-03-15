# Vahini: A Self-Driving Auto-irrigation Electric Vehicle

Watering trees is a vital but tedious task for farmers and gardeners. The idea behind _Project Vahini_ is to use a _self-driving vehicle_ to irrigate plantations. The vehicle is equipped with sensors that detect the location of the trees. It then moves along a predefined path and sprays water according to the needs of each plant.

## Working of the Project

The code runs a flask server on a Raspberry Pi device that serves as the brain of the vehicle.
It also interfaces with various sensors such as GPS, proximity sensors and magnetometers to enable accurate navigation and obstacle avoidance.
The project leverages the power of Graph Theory and shortest path algorithms to find the optimal route for the vehicle on any given map. The project utilizes the OSMX library to access high-quality map data and the NetworkX library to perform efficient graph analysis.
The project is currently under development and has great potential for improving agricultural productivity and sustainability.

### Component Diagram

<img src="./doc-assets/Vahini_Components.png"></img>

## Setup Instructions

### Pre-requistes for setup

- Python 3.7 or higher
- An idea on how to use a terminal
- Git Installed on your computer

### Setup

1. Clone the repository using the below command

```
git clone https://github.com/Blake2912/Vahini-2.0.git
```

2. Setup Virtual Environment

For MacOS/Linux Systems

```
python -m venv <your-env-name>
```

The above command will create a virtual environment in the given path

```
source ./<your-env-name>/bin/activate
```

The above command will activate the virtual environment

For Windows Systems

```
python -m venv <your-env-name>
```

The above command will create a virtual environment in the given path.
For PowerShell:

```
<your-env-name>/bin/Activate.ps1
```

For Command Prompt:

```
<your-env-name>\Scripts\activate.bat
```

<Strong>
Note:

> Don't forget to add your virtual environment folder in `.gitignore` if you have created the environment inside the repository folder

</Strong>
If you run into any issues you can refer the following link which demonstrates on how to create Virtual Environments <a href="https://docs.python.org/3/library/venv.html">venv</a>.

3. Installing the required Packages

```
pip install -r requirements.txt
```

4. Run the flask server

```
flask run app.py
```

## Architecture

<img src="./doc-assets/Architecture.jpeg"></img>

## Libraries Used

- NetworkX Library
- OSMX Library

## References

- <a href="https://networkx.org">NetworkX</a>
- <a href="https://osmnx.readthedocs.io/en/stable/">OSMNX</a>

## Contributors

- @Blake2912
- @amartyanambiar
- @healertrix
