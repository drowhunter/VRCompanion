#****************************************************************
# Enable headtracking via mouse movement for Forza games.
# 
# This script is intended to be used with the VR-to-Mouse script.
# This script will enable mouse look when the head is turned beyond a certain threshold.
# mouse look deadzone will be reduced when mouse look is enabled, to allow smooth recentring of the view and to only move the view when user intends to look out the windows.
#
# NOTE: Forza games dont actually support pitch for mouse look, so this script only uses yaw.
#****************************************************************



bMouseLookXEnabled = False
bMouseLookYEnabled = False

class hDirection:
    global bMouseLookXEnabled
    global bMouseLookYEnabled

    def __init__(self, maxDegrees , maxValue, deadZones = [0, 0]):
        # type: (bool, int, float, List[float]) -> None
        #self.isInverted = isInverted
        self.maxDegrees = abs(maxDegrees) # Maximum degrees of head rotation
        self.maxValue = abs(maxValue)   # Maximum value for joystick axis
        self._deadZones = deadZones

        self._deadZoneIndex = 0
    
    @property
    def deadZone(self):
        # type: () -> float
        return abs(self._deadZones[self.deadZoneIndex])
    
    @property
    def deadZoneIndex(self):
        # type: () -> int        
        return 0 #1 if bMouseLookXEnabled or bMouseLookYEnabled else 0
    
    def isActive(self, headValue):
    # type: (float) -> bool
        return abs(headValue) > self.deadZone

# ADJUSTABLE SCRIPT PARAMETERS

FULLY_DISABLED = [1, 1]  # Effectivly disables deadzone when mouselook is enabled
LEFT_DIRECTION  = hDirection(40, 1, [0.9])  
RIGHT_DIRECTION = hDirection(40, 1, [0.65]) 
#UP_DIRECTION    = hDirection(40, 1, FULLY_DISABLED) 
#DOWN_DIRECTION  = hDirection(40, 1, FULLY_DISABLED) 

def afterUpdate(sender):
    # type: (VRToMouse) -> None
    global bMouseLookXEnabled
    #global bMouseLookYEnabled
    global LEFT_DIRECTION 
    global RIGHT_DIRECTION
    #global UP_DIRECTION
    #global DOWN_DIRECTION 
    
    yaw = environment.vr.headPose.yaw    
    headL = filters.ensureMapRange(yaw, -LEFT_DIRECTION.maxDegrees, 0, -LEFT_DIRECTION.maxValue, 0)
    headR = filters.ensureMapRange(yaw, 0, RIGHT_DIRECTION.maxDegrees, 0,RIGHT_DIRECTION.maxValue)
    lda = LEFT_DIRECTION.isActive(headL)
    rda = RIGHT_DIRECTION.isActive(headR)

    bMouseLookXEnabled = lda or rda 
    #if not bMouseLookXEnabled:
    sender.deltaX = 0        
    
    #pitch = environment.vr.headPose.pitch
    #headY = filters.ensureMapRange(pitch, UP_DIRECTION.maxDegrees, DOWN_DIRECTION.maxDegrees, UP_DIRECTION.maxValue, DOWN_DIRECTION.maxValue)
    #bMouseLookYEnabled = UP_DIRECTION.isActive(headY) or  DOWN_DIRECTION.isActive(headY) 
    #if not bMouseLookYEnabled:
    #sender.deltaY = 0

    # press right mouse button to enable mouse look
    environment.mouse.rightButton = bMouseLookXEnabled # or bMouseLookYEnabled

    #diagnostics.watch("{0}, {1}".format(headX, headY) , "head X,Y")
    diagnostics.watch(yaw, "head yaw")
    diagnostics.watch(headL, "head L")
    diagnostics.watch(headR, "head R")
    diagnostics.watch("{0}, {1}".format(LEFT_DIRECTION.deadZone, RIGHT_DIRECTION.deadZone) , "dzLR")
    diagnostics.watch("{0}, {1}".format(lda, rda), "LR Enabled")    
    diagnostics.watch(bMouseLookXEnabled, "bMouseLookXEnabled")
    #diagnostics.watch(bMouseLookYEnabled, "bMouseLookYEnabled")


vrToMouse.mode.current = 1
vrToMouse.enableYawPitch.current = False
vrToMouse.enableRoll.current = False
vrToMouse.mouseSensitivityX = 30
vrToMouse.mouseSensitivityY = 0
vrToMouse.afterUpdate = afterUpdate