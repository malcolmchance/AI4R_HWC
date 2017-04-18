#!/usr/bin/env python

############################################################################################
# ! Attach Ultrasonic sensor to A1 Port.
############################################################################################
from gopigo import *
import sys
from collections import Counter
import math

def sensor_calibration(dist):
        return(dist-5)/1.25+5

def get_sensor_distance(min_dist = 250, num_measurements = 3):
        for i in range (num_measurements):
                d = us_dist(15)
                if d < min_dist:
                        min_dist = d
        return sensor_calibration(min_dist)

def move_sensor_servo(angle, sleep_time = 0.1):
        enable_servo()     
        servo(angle)
        time.sleep(sleep_time)
        disable_servo()
        
        
        
def move_robot(steer = 0, move_speed = 20, move_distance = 8):

        # Check steer: -100 <= steer <= 100
        steer /= 2.
        if abs(steer) > 25:
                steer = steer/abs(steer)*25
                
        # Check speed: 0 <= speed <= 100
        if move_speed > 100:
                move_speed  = 100
        if move_speed < 0:
                move_speed = 0
        
        # Check distance: 0 <= distance <= 36 (two wheel revolutions)
        if move_distance < 0:
                move_distance = 0
        if move_distance > 36: 
                move_distance = 36
                
                # Set left and right wheels speeds
        set_left_speed(int((100 + steer) * move_speed/10))
        set_right_speed(int((100 - steer) * move_speed/10))
        
        #GoPiGo moves forward, stops makes a map and again moves forward
        #enable_com_timeout(1000)
        
        #Set wheel rotation distance (using encoder targeting)
        enc_tgt(1,1,move_distance) 
        
        print "Steer:", steer, "Speed:", move_speed, "Distance:", move_distance
        
        # Move wheels
        fwd()
        time.sleep(.5)

def robot_position(target_wall_distance = 25):
        return (get_sensor_distance() - target_wall_distance)
        
################################################################                

stop()                                  # Emergency stop  to prevent run-away.

def run_robot(p, i, d, steps):
        stop()                          # Emergency stop  to prevent run-away.
        move_sensor_servo(1)            # Turn sensor 90 degrees to right.

        # Initialize Variables
        crosstrack_error = robot_position()
        croscheck_error_sum = 0
        

        for _ in range(steps):
                #Determine robot actual distance relative to intended distance from wall    
                robot_loc = robot_position()
                delta_cross_track_error = robot_loc - crosstrack_error 
                cross_track_error = robot_loc
                croscheck_error_sum += crosstrack_error
                print "Location", robot_loc, "CTE", cross_track_error, "CTE-Error",delta_cross_track_error,  "CTE-SUM", croscheck_error_sum

                # Set PID Parameters
                proportional    = p * cross_track_error
                integral        = i * croscheck_error_sum
                delta           = d * delta_cross_track_error
                steer           = proportional + integral + delta
                print p, i, d
                print "proportional", proportional, "integral", integral, "delta",delta

                # Move Robot
                move_robot(steer, move_speed = 10, move_distance = 8)
                time.sleep(.9)

                while True:
                        enc=read_enc_status()
                        ts=read_timeout_status()
                        time.sleep(.001)
                        print enc,ts
                        if enc == 0:    #Stop when target is reached
                                break
                        if  ts==0:
                                break
                time.sleep(.1)
        stop()

time.sleep(3)      
run_robot(p=10, i=0, d=10, steps = 30)

stop()
        
        
        

                       
