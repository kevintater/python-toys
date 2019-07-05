 python-toys
A fun little place for random python. Let's start with robots!

robotbynumbers.py is a utility app to manually move a robot arm
by individual keypresses mapped to specific actuators in the arm.
The best use for this is to manually adjust the position of the arm
to a base initial position.

robot.py is intended to be a base class to import for arm functions.
It is currently a script to wave the arm. The arm must be in the most
collapsed position to start.

Here are some examples for moving the individual joints.

move_arm(1,[16,0,0]) #Elbow up
move_arm(1,[4,0,0]) #Wrist up
move_arm(1,[8,0,0]) # Wrist down
move_arm(1,[32,0,0]) #Elbow down
move_arm(1,[0,0,1]) #Light on
move_arm(1,[0,0,0]) #Light off
time.sleep(1)
move_arm(1,[0,1,0]) #Rotate base anti-clockwise
move_arm(1,[0,2,0]) #Rotate base clockwise
move_arm(1,[0,1,0]) #Rotate base anti-clockwise
move_arm(1,[64,0,0]) #Shoulder up
time.sleep(1)
move_arm(1,[0,1,0]) #Rotate base anti-clockwise
time.sleep(1)
move_arm(1,[0,1,0]) #Rotate base anti-clockwise
move_arm(1,[128,0,0]) #Shoulder down
time.sleep(1)
move_arm(1,[0,1,0]) #Rotate base anti-clockwise
move_arm(1,[32,0,0]) #Elbow down
move_arm(1,[1,0,0]) #Grip close
move_arm(1,[4,0,0]) #Wrist up
