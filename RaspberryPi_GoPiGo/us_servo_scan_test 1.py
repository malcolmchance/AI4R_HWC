#!/usr/bin/env python

############################################################################################
# ! Attach Ultrasonic sensor to A1 Port.
############################################################################################
from gopigo import *
import sys
from collections import Counter
import math

def true_distance(dist):
        return(dist-5)/1.25+5

def true_angle(angle, offset_error):
        return angle - offset_error

def get_distance(dist, num_measurements):
        for i in range (num_measurements):
                d = us_dist(15)
                if d < dist:
                        dist = d
        return dist

def move_servo(angle, sweep_sleep_time):
        enable_servo()
        servo(angle)
        time.sleep(sweep_sleep_time)
        disable_servo()

def display_results(distance_list, angle_list):
        print "="*27
        print "Closest Object:",closest(distance_list, angle_list)
        print "- "*14
        for i in range(len(distance_list)-1):
                print "Angle: %3d  Distance: %5.1f"% (angle_list[i],distance_list[i])
        print "-"*27


def closest(distance_list, angle_list):
        closest = 250
        index = 0
        for i in range(len(distance_list)):
                if distance_list[i]<= closest:
                        closest = distance_list[i]
                        index = i
        return distance_list[index], angle_list[index]

def simple_scan_RL(min_distance = 5):
        max_distance            = closest_object = 250
        offset_error            = 10
        start_angle             = 30 + offset_error
        end_angle               = 150 + offset_error
        increment               = 10
        num_readings            = 1 + (end_angle - start_angle)/increment
        angle_list              = [0]*num_readings
        distance_list           = [max_distance]*num_readings
        sweep_sleep_time        = .1
        num_measurements        = 1
        
        for angle, index in zip(range(start_angle, end_angle, increment), range(0, len(distance_list), 1)):
                dist = get_distance(max_distance, num_measurements)
                t = true_distance(dist)
                if t < min_distance:
                        return wheel_speed(t, true_angle(angle, offset_error))
                distance_list[index] = t
                angle_list[index] = true_angle(angle, offset_error)  
                move_servo(angle, sweep_sleep_time)
                    
        display_results(distance_list, angle_list)
        closest_object= closest(distance_list, angle_list)   
        return  wheel_speed(closest_object[0], closest_object[1])

def simple_scan_LR(min_distance = 5):
        max_distance            = closest_object = 250
        offset_error            = 10
        start_angle             = 30 + offset_error
        end_angle               = 150 + offset_error
        increment               = 10
        num_readings            = 1 + (end_angle - start_angle)/increment
        angle_list              = [0]*num_readings
        distance_list           = [max_distance]*num_readings
        sweep_sleep_time        = .1
        num_measurements        = 1

        for angle, index in zip(range(end_angle, start_angle, -increment), range(len(distance_list)-1,0, -1)):   
                dist = get_distance(max_distance, num_measurements)    
                t = true_distance(dist)
                if t < min_distance:
                        return wheel_speed(t, true_angle(angle, offset_error))
                distance_list[index] = t
                angle_list[index] = true_angle(angle, offset_error)
                move_servo(angle, sweep_sleep_time)
                    
        display_results(distance_list, angle_list)
        closest_object= closest(distance_list, angle_list)
        return  wheel_speed(closest_object[0], closest_object[1])

def distance_index(dist):
        if dist >= 40:
                return 0
        if dist >= 30:
                return 1
        if dist >= 20:
                return 2
        if dist >= 10:
                return 3
        else:
                return 4

def angle_index(angle):
        return (angle-30)/10

def wheel_speed(distance, angle):  
        """
                        ------------------------------------------------------------------------  ANGLE  ---------------------------------------------------------------------------
        Distance              30          40         50          60          70          80          90          100          110        120         130        140           150
        40 - 250        [[1.0, 1.0], [1.0, 1.0], [1.0, 1.0], [1.0, 1.0], [1.0, 1.0], [1.0, 1.0], [1.0, 1.0], [1.0, 1.0], [1.0, 1.0], [1.0, 1.0], [1.0, 1.0], [1.0, 1.0], [1.0, 1.0]],
        30 - 40         [[0.8, 0.8], [0.8, 0.8], [0.8, 0.8], [0.8, 0.7], [0.8, 0.7], [0.8, 0.6], [0.8, 0.6], [0.6, 0.8], [0.7, 0.8], [0.7, 0.8], [0.8, 0.8], [0.8, 0.8], [0.8, 0.8]],
        20 - 30         [[0.6, 0.6], [0.6, 0.5], [0.6, 0.5], [0.6, 0.5], [0.6, 0.4], [0.6, 0.4], [0.6, 0.4], [0.4, 0.6], [0.4, 0.6], [0.5, 0.6], [0.5, 0.6], [0.5, 0.6], [0.6, 0.6]],
        10 - 20         [[0.4, 0.4], [0.4, 0.3], [0.4, 0.3], [0.4, 0.3], [0.4, 0.2], [0.4, 0.2], [0.4, 0.2], [0.2, 0.4], [0.2, 0.4], [0.3, 0.4], [0.3, 0.4], [0.3, 0.4], [0.4, 0.4]],
        0 - 10          [[0.2, 0.0], [0.2, 0.0], [0.2, 0.0], [0.2, 0.0], [0.2, 0.0], [0.2, 0.0], [0.2, 0.0], [0.0, 0.2], [0.0, 0.2], [0.0, 0.2], [0.0, 0.2], [0.0, 0.2], [0.0, 0.2]
        """
        lookup_table = [[[1.0, 1.0], [1.0, 1.0], [1.0, 1.0], [1.0, 1.0], [1.0, 1.0], [1.0, 1.0], [1.0, 1.0], [1.0, 1.0], [1.0, 1.0], [1.0, 1.0], [1.0, 1.0], [1.0, 1.0], [1.0, 1.0]],
                        [[1.0, 0.8], [1.0, 0.8], [1.0, 0.8], [1.0, 0.7], [1.0, 0.7], [1.0, 0.6], [1.0, 0.6], [0.6, 1.0], [0.7, 1.0], [0.7, 1.0], [0.8, 1.0], [0.8, 1.0], [0.8, 1.0]],
                        [[0.8, 0.8], [0.8, 0.5], [0.8, 0.5], [0.8, 0.5], [0.8, 0.4], [0.8, 0.4], [0.8, 0.4], [0.4, 0.8], [0.4, 0.8], [0.5, 0.8], [0.5, 0.8], [0.5, 0.8], [0.6, 0.8]],
                        [[0.8, 0.2], [0.8, 0.2], [0.8, 0.2], [0.8, 0.2], [0.8, 0.2], [0.8, 0.2], [0.8, 0.2], [0.2, 0.8], [0.2, 0.8], [0.2, 0.8], [0.2, 0.8], [0.2, 0.8], [0.2, 0.8]],
                        [[0.6, 0.0], [0.6, 0.0], [0.6, 0.0], [0.6, 0.0], [0.6, 0.0], [0.6, 0.0], [0.6, 0.0], [0.0, 0.6], [0.0, 0.6], [0.0, 0.6], [0.0, 0.6], [0.0, 0.6], [0.0, 0.6]]]
        return  lookup_table[distance_index(distance)][angle_index(angle)]
        

stop()

direction = 1
while True:
        #GoPiGo moves forward, stops makes a map and again moves forward
        enable_com_timeout(3000)
        enc_tgt(1,1,72) #Set encoder targetting. Stop after 4 rotations of both the wheels
        max_speed = 150
        
        # Scan surroundings
        if direction == 1:
                d = simple_scan_RL(min_distance = 3)
        else:
                d = simple_scan_LR(min_distance = 3)
        direction *=-1
        if d <= 3: #If any obstacle is closer than 3 cm, stop
                print "Too close. Obstable at ", d
                break

        # Sept speeed and direction of wheels
        print "Speed", int(d[1]*max_speed), int(d[0]*max_speed)
        if d[1] == 0:
                enc_tgt(1,1,9)
                left_rot()
        if d[0] == 0:
                enc_tgt(1,1,9)
                right_rot()
        else: 
                set_left_speed(int(d[1]*max_speed))
                set_right_speed(int(d[0]*max_speed))
                fwd()
            
        time.sleep(.1)
        while True:
                enc=read_enc_status()
                ts=read_timeout_status()
                time.sleep(.05)
                print enc,ts
                if enc == 0:    #Stop when target is reached
                        break
                if  ts==0:
                        break             
        time.sleep(1)

        
        
        

                       
