from .vr_headjoy import HeadJoystick, HeadJoystickDirection
from .environment import environment
from .mode_based_actions import Mode

class VRToOpenTrack:
    """ 
    Sends vr head tracking data to Opentrack via udp.
    Download and run OpenTrack for input select UDP over Network and set the port to 4242.
    Set the output to Freetrack 2.0 Enhanced.

    In settings ensure that Center at Start is unchecked and that all curves are set to linear
    (that means input is the same as output)

    Attributes:
    -----------
    beforeUpdate : function
        A callback function to be called before updating the head tracking data.
    Methods:
    --------
    
    """
    def __init__(self):
                
        self.mode = Mode()
        
        self.__pose = environment.vr.headPose
        self.__headJoy = HeadJoystick()
        self.beforeUpdate = None


    def config_left(self, minDegrees, maxDegrees, minDegreesOut, maxDegreesOut, curve = None):
        #type: (float, float, float, float, CurveGlobal) -> None
        self.__headJoy.left = HeadJoystickDirection(True, minDegrees, maxDegrees, minDegreesOut/180.0, maxDegreesOut/180.0, curve)

    def config_right(self, minDegrees, maxDegrees, minDegreesOut, maxDegreesOut, curve = None):
        #type: (float, float, float, float, CurveGlobal) -> None        
        self.__headJoy.right = HeadJoystickDirection(False, minDegrees, maxDegrees, minDegreesOut/180.0, maxDegreesOut/180.0, curve)

    def config_up(self, minDegrees, maxDegrees, minDegreesOut, maxDegreesOut, curve = None):
        #type: (float, float, float, float, CurveGlobal) -> None        
        self.__headJoy.up = HeadJoystickDirection(True, minDegrees, maxDegrees, minDegreesOut/180.0, maxDegreesOut/180.0, curve)

    def config_down(self, minDegrees, maxDegrees, minDegreesOut, maxDegreesOut, curve = None):
        #type: (float, float, float, float, CurveGlobal) -> None        
        self.__headJoy.down = HeadJoystickDirection(False, minDegrees, maxDegrees, minDegreesOut/180.0, maxDegreesOut/180.0, curve)
    
    
    
    def update(self, currentTime, deltaTime):

        if(self.mode.current == 1):
            self.__headJoy.update()  
            if self.beforeUpdate is not None:
                self.beforeUpdate(self)

            
            environment.openTrack.yaw =  environment.vr.headPose.yaw
            environment.openTrack.pitch = -environment.vr.headPose.pitch
            environment.openTrack.roll = -environment.vr.headPose.roll
            environment.openTrack.x = -environment.vr.headPose.x
            environment.openTrack.y = environment.vr.headPose.y
            environment.openTrack.z = environment.vr.headPose.z