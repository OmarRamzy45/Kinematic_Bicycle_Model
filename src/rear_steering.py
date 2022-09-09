#!/usr/bin/env python3
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import math
import rospy
from turtlesim.msg import Pose
from geometry_msgs.msg import Twist
import time
import numpy as np

class TurtleBicycleModel:
  
    def __init__(self):

        self.x = 0
        self.y = 0
        self.theta = 0
        self.lr = rospy.get_param("/rear_length")
        self.lf = rospy.get_param("/front_length")
        self.L = self.lr + self.lf
        self.v=0
        self.delta=0
        self.sample_time=0
        self.beta=0
        self.pose = Pose()
        self.vel_msg = Twist()

        rospy.init_node('turtle_bicycle', anonymous=True)
        self.velocity_publisher = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)
        self.pose_subscriber = rospy.Subscriber('/turtle1/pose', Pose, self.update_pose)
        self.rate = rospy.Rate(10)

    def set_paramters(self):

        print("Welcome! :) \n")
        self.v = float(input("enter your speed: "))
        self.delta = np.deg2rad(float(input("enter the steering angle in (degrees): ")))
        self.sample_time = float(input("enter the time of simulation (seconds): "))
        self.flag = input("Do you want a decaying steering angle? (y/n) \n")
        self.beta = math.atan2(-1* (self.lf * math.tan(self.delta)) , self.L)
        
    def update_pose(self, pose):
        global X
        global Y
        global yaw
        X = self.pose.x
        Y = self.pose.y
        yaw=self.pose.theta  
  
    def move(self):

        t_end = time.time() + self.sample_time
    
        while time.time() < t_end :

            if (self.flag == 'y' and self.delta >0):
                self.steering_decay = -0.001
                print("steering angle is: ", round(np.rad2deg(self.delta),4), "Degrees")
            elif (self.flag == 'n'):
                self.steering_decay = 0


            
            self.delta += self.steering_decay
            
            x_dot =  self.v * math.cos(self.pose.theta - self.beta)
            y_dot = self.v * math.sin(self.pose.theta - self.beta)
            theta_dot = -1 * (self.v / self.L) * (math.cos(self.beta) * math.tan(self.delta))  

            self.vel_msg.linear.x = x_dot
            self.vel_msg.linear.y = y_dot
            self.vel_msg.linear.y = 0

            self.vel_msg.angular.x =0 
            self.vel_msg.angular.y =0
            self.vel_msg.angular.z = theta_dot
              
            self.velocity_publisher.publish(self.vel_msg)
            self.rate.sleep()

        self.vel_msg.linear.x = 0
        self.vel_msg.linear.y = 0
        self.vel_msg.angular.z = 0
        self.velocity_publisher.publish(self.vel_msg)




if __name__ == '__main__':
    
    model = TurtleBicycleModel()
    model.set_paramters()
    model.move()
    print("Time is over!!")
    
