from cpkf.key_object import KeyObject
from config import MOUSEKEY_CONFIG

class MOUSEKey(KeyObject):
    def press(self, kbd, time):
        if kbd.mouse is None:
            kbd.updateHIDdevice()
        self.count = 0
        self.t = time
    
    def getSpeed(self):
        if(self.count < MOUSEKEY_CONFIG["TIME_TO_MAX"]):
            self.count += 1
            return int(self.count*MOUSEKEY_CONFIG["MAX_SPEED"]/MOUSEKEY_CONFIG["TIME_TO_MAX"])
        else:
            return MOUSEKEY_CONFIG["MAX_SPEED"]

class WHEELKey(MOUSEKey):
    def getSpeed(self):
        if(self.count < MOUSEKEY_CONFIG["WHEEL_TIME_TO_MAX"]):
            self.count += 1
            return int(self.count*MOUSEKEY_CONFIG["WHEEL_MAX_SPEED"]/MOUSEKEY_CONFIG["WHEEL_TIME_TO_MAX"])
        else:
            return MOUSEKEY_CONFIG["WHEEL_MAX_SPEED"]
            
class MOUSEU(MOUSEKey):
    def tick(self, kbd, time):
        if(time-self.t > MOUSEKEY_CONFIG["INTERVAL"]):
            kbd.mouse.move(x=0, y=-self.getSpeed())
            self.t = time

class MOUSED(MOUSEKey):
    def tick(self, kbd, time):
        if(time-self.t > MOUSEKEY_CONFIG["INTERVAL"]):
            kbd.mouse.move(x=0, y=self.getSpeed())
            self.t = time

class MOUSEL(MOUSEKey):
    def tick(self, kbd, time):
        if(time-self.t > MOUSEKEY_CONFIG["INTERVAL"]):
            kbd.mouse.move(x=-self.getSpeed(), y=0)
            self.t = time

class MOUSER(MOUSEKey):
    def tick(self, kbd, time):
        if(time-self.t > MOUSEKEY_CONFIG["INTERVAL"]):
            kbd.mouse.move(x=self.getSpeed(), y=0)
            self.t = time

class WHEELU(WHEELKey):
    def tick(self, kbd, time):
        if(time-self.t > MOUSEKEY_CONFIG["INTERVAL"]):
            kbd.mouse.move(wheel=self.getSpeed())
            self.t = time

class WHEELD(WHEELKey):
    def tick(self, kbd, time):
        if(time-self.t > MOUSEKEY_CONFIG["INTERVAL"]):
            kbd.mouse.move(wheel=-self.getSpeed())
            self.t = time

class MOUSELB(MOUSEKey):
    def press(self, kbd, time):
        super().press(kbd, time)
        kbd.mouse.press(kbd.mouse.LEFT_BUTTON)
    
    def release(self, kbd, time):
        kbd.mouse.release(kbd.mouse.LEFT_BUTTON)


class MOUSERB(MOUSEKey):
    def press(self, kbd, time):
        super().press(kbd, time)
        kbd.mouse.press(kbd.mouse.RIGHT_BUTTON)
    
    def release(self, kbd, time):
        kbd.mouse.release(kbd.mouse.RIGHT_BUTTON)
