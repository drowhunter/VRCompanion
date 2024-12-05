from ofisare.vr_headjoy import HeadJoystickDirection
#****************************************************************
# Enable headtracking via mouse movement for Forza games.
# 
# This script is intended to be used with the VR-to-Mouse script.
# This script will enable mouse look when the head is turned beyond a certain threshold.
# mouse look deadzone will be reduced when mouse look is enabled, to allow smooth recentring of the view and to only move the view when user intends to look out the windows.
#
# NOTE: Forza games dont actually support pitch for mouse look, so this script only uses yaw.
#****************************************************************
#easeInC = curves.create(0.2, 0.9, 0.731, 0.544)

def befupdate(sender):
    environment.diagnostics.watch(sender.headJoy.x, 'hx')
    environment.diagnostics.watch(sender.headJoy.y, 'hy')
    #tf = easeInC.getY(sender.headJoy.x)
    #enviribment.diagnostics.watch(tf, 'tf')

vrToGamepad.setController(VigemController.XBoxController)
vrToGamepad.headJoy.left  = HeadJoystickDirection(True,  1, 40, 0.1, 0.95) 
vrToGamepad.headJoy.right = HeadJoystickDirection(False, 1, 40, 0.1, 0.95) 
vrToGamepad.headJoy.up.enabled    = False #HeadJoystickDirection(True,  5, 40, 1, 0.2) 
vrToGamepad.headJoy.down.enabled  = False #HeadJoystickDirection(False, 40, 40, 0, 0.01) 
vrToGamepad.headMode.current = 2
vrToGamepad.beforeUpdate = befupdate


vrToGamepad.leftTriggerMode.current = 1
vrToGamepad.rightTriggerMode.current = 2

gestureTracker.gripLeft.enabled = True
gestureTracker.gripLeft.action = GamepadPress(VigemButton.ShoulderLeft)
gestureTracker.gripRight.enabled = True
gestureTracker.gripRight.action = GamepadPress(VigemButton.ShoulderRight)

vrToGamepad.leftStickMode.current = 1
vrToGamepad.rightStickMode.current = 0

gestureTracker.buttonLeftStick.enabled = True
gestureTracker.buttonLeftStick.action = GamepadPress(VigemButton.ThumbLeft)
gestureTracker.buttonRightStick.enabled = False
gestureTracker.buttonRightStick.action = GamepadPress(VigemButton.ThumbRight)

gestureTracker.buttonA.enabled = True
gestureTracker.buttonA.action = GamepadPress(VigemButton.A)
gestureTracker.buttonB.enabled = True
gestureTracker.buttonB.action = GamepadPress(VigemButton.B)

gestureTracker.buttonX.enabled = True
gestureTracker.buttonX.action = GamepadPress(VigemButton.X)
gestureTracker.buttonY.enabled = True
gestureTracker.buttonY.action = GamepadPress(VigemButton.Y)