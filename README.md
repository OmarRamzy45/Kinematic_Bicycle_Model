# Kinematic Bicycle Model
In this repository I'll be implemeting the kinematic bicycle model for the 4-Wheel vehicles with front steering and rear steering in Pyhton class Object. And I'm going to test this model by changing different parameters of the vehicle like the steering angle and speed to see how the model will behave in these cases. For the visualization of the output I'll use ROS simulator "turtlesim".

You can find the dimensions of the car (The distance between CG and front wheel, The distance between CG and back wheel) in the "data.yaml" file in config folder.

You can also find launch file for both front and rear steering cases.

So, Let's start.

- ## Front Steering
Starting with the front steering model We will consider the point to be analyzed on the vehicle is at its center of gravity.
Knowing that all point on the vehicle moves about the Instantaneous Center of Rotation ( ICR ).

![front](https://miro.medium.com/max/940/1*WKEsm54kLK2thpYlxii14g.png)

In the image above you can find the geometry of the model which I relied on to derive all the following equations.

### Model Equations:
#### $V_x$ = $vcos{(\theta + \beta)}$
#### $V_y$ = $vsin{(\theta + \beta)}$
### $\dot{\theta}$ = $v cos(\beta)tan(\delta) \over L $
### $\beta  =$ $tan^-1($ $l_r tan(\delta) \over L$ $)$
### Model Inputs:
- Steering angle $\delta$
- Vehicle velocity $v$
- time of simulation $t$
- $l_r$ from yaml file

### Simulation
- velocity = 5
- steering angle = 30 $degrees$
- simulation time = 5 $seconds$

- Video:

https://user-images.githubusercontent.com/100040470/189362904-06337fbc-dbe1-450f-bea5-3cddfe5cff1e.mp4

#### Decaing Steering angle
here I added a new feature to me model where the steering angle is not constant instead it's deacing with time until it gets to zero and the vehicle moves in straight line.

- Video:

https://user-images.githubusercontent.com/100040470/189363702-c0330d0b-358e-4cd9-bd25-b56cfb2ba21f.mp4

- ## Rear Steering
Rear steering is the same like front steering but the difference is that the rear wheels are the moving ones. 
you can notice that for the same input the front and rear steering mechanisms will behave opposite to each others.

![rear](https://github.com/OmarRamzy45/Kinematic_Bicycle_Model/blob/master/Media/Rear_Steering_crop.png?raw=true)

### Model Equations:
#### $V_x$ = $vcos{(\beta - \theta)}$
#### $V_y$ = $vsin{(\beta - \theta)}$
### $\dot{\theta}$ = $(-v cos(\beta)tan(\delta)) \over L $
#### $\beta  =$ $tan^-1($ $-l_f tan(\delta) \over L$ $)$

### Model Inputs:
- Steering angle $\delta$
- Vehicle velocity $v$
- time of simulation $t$
- $l_f$ from yaml file

### Simulation
- velocity = 5
- steering angle = 30 $degrees$
- simulation time = 5 $seconds$

-Video:

https://user-images.githubusercontent.com/100040470/189364142-e96aa4b7-e096-4215-8af4-2105ae61ed7a.mp4

#### Decaing Steering angle
- Video:

https://user-images.githubusercontent.com/100040470/189364379-425bc851-20b3-40bc-9e1a-4fb60187d52c.mp4

That's all, Hope you found this useful. Thank you for reading :)
