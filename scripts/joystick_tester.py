if starting:
    #myjoy = joystick["SideWinder Force Feedback 2 Joystick"]
    myjoy = joystick["DualSense Wireless Controller"]
    #diagnostics.debug(myjoy.info())

diagnostics.watch(myjoy.sliders[0])
diagnostics.watch(myjoy.pov[0])

diagnostics.multiWatch(myjoy)
#diagnostics.multiWatch(myjoy, "JoystickName", "buttons", "ButtonCount","AxesCount","PovCount", "x","y","z","rotationX","rotationY","rotationZ")

