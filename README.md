# Welcome to Project Vahini

Project Vahini is a project that is used to automatically move a watering vehicle on the farmland or argricultural plantations and water the trees.

## About
@amartyanambiar @healertrix write something here

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

>Don't forget to add your virtual environment folder in `.gitignore` if you have created the environment inside the repository folder

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
