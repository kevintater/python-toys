#!/usr/bin/python

import time
import usb.core
import usb.util

# Allocate the name 'RoboArm' to the USB device
RoboArm = usb.core.find(idVendor=0x1267, idProduct=0x000)

# Check if the arm is detected and warn if not
if RoboArm is None:
    raise ValueError("Arm not found")

'''Create a variable for duration'''
DURATION = 1

# Define a procedure to execute each movement
def move_arm(DURATION, ArmCmd):
    # Start the movement
    RoboArm.ctrl_transfer(0x40, 6, 0x100, 0, ArmCmd, 3)
    # Stop the movement after waiting a specified duration
    time.sleep(DURATION)
    ArmCmd = [0, 0, 0]
    RoboArm.ctrl_transfer(0x40, 6, 0x100, 0, ArmCmd, 3)


def wave():
    '''Move robot arm in a waving motion'''

    move_arm(1, [16, 0, 0])  # Elbow up
    move_arm(1, [4, 0, 0])  # Wrist up
    move_arm(1, [8, 0, 0])  # Wrist down
    move_arm(1, [32, 0, 0])  # Elbow down


if __name__ == '__main__':
    '''Currently only waves'''
    wave()
