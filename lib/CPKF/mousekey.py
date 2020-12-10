from cpkf.key_object import KeyObject
from config import MOUSEKEY_CONFIG

class MOUSEKey(KeyObject):
    def press(self, kbd, time):
        if kbd.mouse is None:
            kbd.updateHIDdevice()
        self.t = time

class MOUSEU(MOUSEKey):
    def tick(self, kbd, time):
        if(time-self.t > MOUSEKEY_CONFIG["INTERVAL"]):
            kbd.mouse.move(x=0, y=-MOUSEKEY_CONFIG["MAX_SPEED"])
            self.t = time

class MOUSED(MOUSEKey):
    def tick(self, kbd, time):
        if(time-self.t > MOUSEKEY_CONFIG["INTERVAL"]):
            kbd.mouse.move(x=0, y=MOUSEKEY_CONFIG["MAX_SPEED"])
            self.t = time

class MOUSEL(MOUSEKey):
    def tick(self, kbd, time):
        if(time-self.t > MOUSEKEY_CONFIG["INTERVAL"]):
            kbd.mouse.move(x=-MOUSEKEY_CONFIG["MAX_SPEED"], y=0)
            self.t = time

class MOUSER(MOUSEKey):
    def tick(self, kbd, time):
        if(time-self.t > MOUSEKEY_CONFIG["INTERVAL"]):
            kbd.mouse.move(x=MOUSEKEY_CONFIG["MAX_SPEED"], y=0)
            self.t = time

class WHEELU(MOUSEKey):
    def tick(self, kbd, time):
        if(time-self.t > MOUSEKEY_CONFIG["INTERVAL"]):
            kbd.mouse.move(wheel=MOUSEKEY_CONFIG["WHEEL_MAX_SPEED"])
            self.t = time

class WHEELD(MOUSEKey):
    def tick(self, kbd, time):
        if(time-self.t > MOUSEKEY_CONFIG["INTERVAL"]):
            kbd.mouse.move(wheel=-MOUSEKEY_CONFIG["WHEEL_MAX_SPEED"])
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