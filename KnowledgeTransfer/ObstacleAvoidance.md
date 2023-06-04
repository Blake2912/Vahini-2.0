# Knowledge Transfer - Unity Simulations
## Points to be noted
- Pre-requisite knowledge of Unity
- Pre-requisite knowledge of C# and Unity IDE
- Some understanding of Vehicle Physics

## Transcript
In this recording I will be explaining the Obstacle Avoidance simulations performed using Unity.
To Start with let us look into the high level flow of obstacle avoidance module in our project.

The following flow chart shows the flow of obstacle avoidance present in our project.

The first state in our flow, is when the vehicle is moving and if an obstacle is detected by the sensor we will check on which sensor is detecting the obstacle and take appropriate action.

The following cases are considered with respect to the sensor that detects the obstacle.

1. Right-Angle Sensor: This is the sensor which is placed at the right side of the vehicle which is at the angle of 30 degrees directed away from the vehicle. If this sensor detects the obstacle then we will have to move the vehicle towards the left and the turn angle of the vehicle will be 75 percent of the maximum steer angle.
2. Right Side Sensor: This is the sensor which is placed at the right side of the vehicle which at the angle of 0 degrees i.e. it is in line with the vehicle. If this sensor detects the obstacle then we will have to move the vehicle towards the left and the turn angle of the vehicle will be the maximum steer angle.
3. Left-Angle Sensor: This is the sensor which is placed at the left side of the vehicle which is at the angle of 30 degrees directed away from the vehicle. If this sensor detects the obstacle then we will have to move the vehicle towards the right and the turn angle of the vehicle will be 75 percent of the maximum steer angle.
4. Left Side Sensor: This is the sensor which is placed at the left side of the vehicle which at the angle of 0 degrees i.e. it is in line with the vehicle. If this sensor detects the obstacle then we will have to move the vehicle towards the right and the turn angle of the vehicle will be the maximum steer angle.
5. Center Sensor: This is the sensor that is placed at the center of the vehicle which will help us detect the obstacles that is present right in front of the vehicle here we will be looking on the direction of normal of the vehicle where if the obstacle is oriented towards the left then we would turn the vehicle towards the left as shown and If the obstacle is oriented towards the right then we would turn the vehicle towards the right as shown

So this is the overall high level flow for obstacle avoidance now let us proceed to the setup of the project.

## Setup
In the Setup we will first look into the requirements for setting up the project. In order for the project to run you must download Unity Hub and install Unity IDE, the version must be greater than 2020, Git and GitHub is also required for cloning the repository from GitHub.

The procedure for setup is as follows:
Clone the repository, open Unity Hub and click on Open => Add Project From Disk, Navigate to the project, go inside Unity/Vahini Simulations, Click on Add Project.
After opening the project If you can see the interface as shown then you have successfully opened the project.

This is the setup procedure now let’s go for In-depth explanation of the code implemented.

## Code Explanation
The code has the following modules:
* Path Module
* Wheel Motion Module
* Vehicle Movement Module

### Path Module
In the path module we have code which creates the path and shows it in the interface. the code draws meshes on the checkpoints and lines between these checkpoints that helps us define the path that the vehicle needs to follow. In the IDE I had to setup the checkpoints manually and the code will take all those checkpoints and connect them to show the path to be followed by the vehicle.

### Wheel Motion Module
In the Wheel Motion module we have code which performs the functions to show the movement of the vehicle, this module helps us in making the simulation more realistic. We have a specific colliders for each functionality in Unity, in that list we have something called the Wheel Collider which would help us give suspension for the vehicle and show the animation for the movement of the wheels.

### Vehicle Movement Module
In the Vehicle movement module we can subdivide it as functions and I will explain each every function in detail by parts:
* *Start Function:*
		The Start function which does initialisation of various functionalities for our simulation, this function is called before the first frame of update. In our case we are initialising the path for the vehicle to move.
* *Fixed Update Function:*
		The Fixed Update function is the function which does the main work of our simulation where all the logical functions are called. This function is a standard functions in Unity which is called once per frame.
* *Drive Function:*
		 The Drive function is used to apply motor torque for the vehicle’s back wheels which will help the vehicle to move, in our case we have the maximum speed of 80 kph where torque is applied till the vehicle reaches 80 in order to maintain the speed of the vehicle. The maximum motor torque that is applied on the wheels are 100 Newton-meter.
* *Apply Steer Function:*
		The Apply Steer function sets the steer angle for the vehicle where we get the relative vector of the vehicle, and then we find the angle by dividing the x component of the vector by its magnitude and then multiplying it by the maximum steering angle set by the user, in our case the maximum steer angle is 45 degrees.
* *Stop Function:*
		The Stop function is a simple function which performs braking for the vehicle where we set the braking torque for the vehicle’s wheels. The state of the vehicle is also changed from “Move” to “Stopped”.
* *Check waypoint Distance Function:*
		The check waypoint function is a function which is used to check if the vehicle has reached the currently set checkpoint and if yes then the checkpoint is shifted to the next point and the vehicle can continue movement. If the vehicle reaches the last point then we call the stop function to stop the vehicle.
* *Sensor Function:*
		The sensor function contains the main logic for obstacle avoidance. The function sets the sensors in the pre-decided position in the vehicle and this will perform the turning of vehicle according to the sensor which detects the obstacle.
If the obstacle is detected in the Front Right Angle / Right Side Sensor then we turn the vehicle towards the left, avoidMultiple is negated which makes it less than zero therefore this implies that the vehicle should move towards the left, and the turn angle varies for the angled and Side sensor.
If the obstacle is detected in the Front Left Angle / Left Side Sensor then we turn the vehicle towards the Right, avoidMultiple is added which makes it more than zero therefore it implies that the vehicle should turn towards the right, and the turn angle varies for the angled and Side sensor.
If the sensor detected is the Front center sensor, then we calculate the normal of the sensor ray to the Object and if the object is oriented towards the left then we turn it towards the left and If the object is Oriented towards the right then we turn the vehicle towards the right.
* *Lerp to Steer Angle Function*:
		This function is used to smoothen the turning of the wheels, the lerp function simulates the step by step turn of the vehicle and thereby giving it a realistic simulation

So this is the overall working and the code explanation for Obstacle Avoidance simulation using unity. 
### Thank you 