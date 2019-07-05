#!/usr/bin/python
# robotbykeys.py
# App to control a malplin robotic arm
# Auther Kevin Tatum 9/24/2016

import curses
import time
import usb.core, usb.util

'''Set usb values for robot model'''
RoboArm = usb.core.find(idVendor=0x1267, idProduct=0x000)

'''Set default movement duration'''
DURATION = 0.1

'''Check for arm connectivity and error if not found.'''
if RoboArm is None:
    raise ValueError("Arm not found")


screen = curses.initscr()
# screen.border(0)

box1 = curses.newwin(20, 20, 5, 5)
box1.immedok(True)
box1.box()


def MoveArm(DURATION, ArmCmd):
    RoboArm.ctrl_transfer(0x40, 6, 0x100, 0, ArmCmd, 3)
    time.sleep(DURATION)
    ArmCmd = [0, 0, 0]
    RoboArm.ctrl_transfer(0x40, 6, 0x100, 0, ArmCmd, 3)


def main(stdscr):
    '''Use keyboard inputs for calling specific joint movements.'''
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
            if c == 113:  # Letter q
                MoveArm(0.1, [0, 0, 1])  # Light on
            if c == 97:  # letter a
                MoveArm(0.1, [0, 0, 0])  # Light off
            if c == 115:  # letter w
                MoveArm(0.1, [2, 0, 0])  # Grip open
            if c == 119:  # letter s
                MoveArm(0.1, [1, 0, 0])  # Grip close
            if c == 101:  # letter e
                MoveArm(0.1, [4, 0, 0])  # Wrist up
            if c == 100:  # letter d
                MoveArm(0.1, [8, 0, 0])  # Wrist down
            if c == 104:  # letter r
                MoveArm(0.1, [16, 0, 0])  # Elbow up
            if c == 102:  # letter f
                MoveArm(0.1, [32, 0, 0])  # Elbow down
            if c == 116:  # letter t
                MoveArm(0.1, [64, 0, 0])  # Shoulder up
            if c == 103:  # letter g
                MoveArm(1, [128, 0, 0])  # Shoulder down
            if c == 121:  # letter y
                MoveArm(0.1, [0, 1, 0])  # Rotate base anti-clockwise
            if c == 104:  # letter h
                MoveArm(0.1, [0, 2, 0])  # Rotate base clockwise

    # else:
    # stdscr.addstr(Header)
    # stdscr.refresh()
    # stdscr.move(1,0)


if __name__ == '__main__':
    curses.wrapper(main)
