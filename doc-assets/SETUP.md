## Setup Instructions

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
flask run
```
