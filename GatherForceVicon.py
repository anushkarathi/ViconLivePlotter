from Vicon import ViconSDK_Wrapper
from ZMQ_PubSub import Publisher 
from SoftRTloop import FlexibleTimer 
import time
import numpy as np

'''
Python script to communicate between Vicon computer and RPi using a publisher/subscriber. 
Can be used to pull data from any device listed in Vicon system.
Anushka Rathi 2024. 
'''

vicon = ViconSDK_Wrapper('localhost','801') 
loopFreq = 1000 # frequency measured in Hz
softRTloop = FlexibleTimer(target_freq=loopFreq) #instantiate soft real-time loop

# Get force data from bertec 
pub = Publisher()
 
while True: 
    '''
    This converts the z-force data into positive values. 
    Make sure to both hardware zero and software zero force plates prior to running this script for best perforamnce.
    '''
    z_forces = [f*-1 for f in vicon.get_latest_device_values(["RightForcePlate", "LeftForcePlate"], ["Force"], ["Fz"])] 
    print(z_forces) # Optional -- to make sure values read are reasonable
    pub.publish('fz_right','% f' %z_forces[0] )
    pub.publish('fz_left', '%f' %z_forces[1])
    
    #soft real-time loop
    softRTloop.pause()
