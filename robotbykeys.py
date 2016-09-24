#!/usr/bin/python
# robotbykeys.py
# App to control a malplin robotic arm
# Auther Kevin Tatum 9/24/2016

import curses
import usb.core, usb.util
import time


RoboArm = usb.core.find(idVendor=0x1267, idProduct=0x000) 


if RoboArm is None:
    raise ValueError("Arm not found")

Duration = .1

screen = curses.initscr()
#screen.border(0)

box1 = curses.newwin(20, 20, 5, 5)
box1.immedok(True)
box1.box()    



def MoveArm(Duration, ArmCmd):
    RoboArm.ctrl_transfer(0x40,6,0x100,0,ArmCmd,3)
    time.sleep(Duration)
    ArmCmd=[0,0,0]
    RoboArm.ctrl_transfer(0x40,6,0x100,0,ArmCmd,3)

def main(stdscr):
    # do not wait for input when calling getch
    stdscr.nodelay(1)
    stdscr.refresh()
    while True:
        # get keyboard input, returns -1 if none available
        c = stdscr.getch()
        box1.immedok(True)
        box1.box()
        if c != -1:
            # print numeric value
            stdscr.addstr(str(c) + ' ')
            stdscr.refresh()
            # return curser to start position
            stdscr.move(0, 0)
            if c == 113: # Letter q
               MoveArm(.1,[0,0,1]) #Light on
               pass
            if c == 97: # letter a
               MoveArm(.1,[0,0,0] #Light off)
               pass
            if c == 115: # letter w
               MoveArm(.1,[2,0,0]) #Grip open
               pass
            if c == 119: # letter s 
               MoveArm(.1,[1,0,0]) #Grip close
               pass
            if c == 101: # letter e
               MoveArm(.1,[4,0,0]) #Wrist up
               pass
            if c == 100: # letter d
               MoveArm(.1,[8,0,0]) # Wrist down
               pass
            if c == 104: # letter r
               MoveArm(.1,[16,0,0]) #Elbow up
               pass
            if c == 102: # letter f
               MoveArm(.1,[32,0,0]) #Elbow down
               pass
            if c == 116: # letter t
               MoveArm(.1,[64,0,0]) #Shoulder up
               pass
            if c == 103: # letter g
               MoveArm(1,[128,0,0]) #Shoulder down
               pass
            if c == 121: # letter y
               MoveArm(.1,[0,1,0]) #Rotate base anti-clockwise
               pass
            if c == 104: # letter h
               MoveArm(.1,[0,2,0]) #Rotate base clockwise
               pass
            
       # else: 
           #stdscr.addstr(Header)
           #stdscr.refresh()
           #stdscr.move(1,0)

if __name__ == '__main__':
    curses.wrapper(main)
