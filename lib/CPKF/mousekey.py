from cpkf.key_object import KeyObject
from config import MOUSEKEY_CONFIG

class MOUSEU(KeyObject):
    def __init__(self):
        pass
    
    def press(self, kbd, time):
        self.t = time
    
    def release(self, kbd, time):
        pass
    
    def tick(self, kbd, time):
        if(time-self.t > MOUSEKEY_CONFIG["INTERVAL"]):
            kbd.mouse.move(x=0, y=-MOUSEKEY_CONFIG["MAX_SPEED"])
            self.t = time

class MOUSED(KeyObject):
    def __init__(self):
        pass
    
    def press(self, kbd, time):
        self.t = time
    
    def release(self, kbd, time):
        pass
    
    def tick(self, kbd, time):
        if(time-self.t > MOUSEKEY_CONFIG["INTERVAL"]):
            kbd.mouse.move(x=0, y=MOUSEKEY_CONFIG["MAX_SPEED"])
            self.t = time

class MOUSEL(KeyObject):
    def __init__(self):
        pass
    
    def press(self, kbd, time):
        self.t = time
    
    def release(self, kbd, time):
        pass
    
    def tick(self, kbd, time):
        if(time-self.t > MOUSEKEY_CONFIG["INTERVAL"]):
            kbd.mouse.move(x=-MOUSEKEY_CONFIG["MAX_SPEED"], y=0)
            self.t = time

class MOUSER(KeyObject):
    def __init__(self):
        pass
    
    def press(self, kbd, time):
        self.t = time
    
    def release(self, kbd, time):
        pass
    
    def tick(self, kbd, time):
        if(time-self.t > MOUSEKEY_CONFIG["INTERVAL"]):
            kbd.mouse.move(x=MOUSEKEY_CONFIG["MAX_SPEED"], y=0)
            self.t = time

class WHEELU(KeyObject):
    def __init__(self):
        pass
    
    def press(self, kbd, time):
        self.t = time
    
    def release(self, kbd, time):
        pass
    
    def tick(self, kbd, time):
        if(time-self.t > MOUSEKEY_CONFIG["INTERVAL"]):
            kbd.mouse.move(wheel=MOUSEKEY_CONFIG["WHEEL_MAX_SPEED"])
            self.t = time

class WHEELD(KeyObject):
    def __init__(self):
        pass
    
    def press(self, kbd, time):
        self.t = time
    
    def release(self, kbd, time):
        pass
    
    def tick(self, kbd, time):
        if(time-self.t > MOUSEKEY_CONFIG["INTERVAL"]):
            kbd.mouse.move(wheel=-MOUSEKEY_CONFIG["WHEEL_MAX_SPEED"])
            self.t = time

class MOUSELB(KeyObject):
    def __init__(self):
        pass

    def press(self, kbd, time):
        kbd.mouse.press(kbd.mouse.LEFT_BUTTON)
    
    def release(self, kbd, time):
        kbd.mouse.release(kbd.mouse.LEFT_BUTTON)
    
    def tick(self, kbd, time):
        pass