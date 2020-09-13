from adafruit_hid.keycode import Keycode as KC
from config import TAPPING_TERM


def _withModifier(modifier, keycode):
    return KC.modifier_bit(modifier) << 8 | keycode

def C(keycode):
    return _withModifier(KC.LEFT_CONTROL, keycode)

def Alt(keycode):
    return _withModifier(KC.LEFT_ALT, keycode)

def CtrlAlt(keycode):
    return _withModifier(KC.LEFT_CONTROL, withModifier(KC.LEFT_ALT, keycode))

def S(keycode):
    return _withModifier(KC.LEFT_SHIFT, keycode)


class KeyObject:
    def __init__(self):
        pass

    def press(self, kbd, time):
        pass

    def release(self, kbd, time):
        pass

    def tick(self, kbd, time):
        pass

class TapPress(KeyObject):
    pass


class LT(TapPress):
    def __init__(self, layer, kc):
        self.layer = layer
        self.kc = kc
        self.executed = False
        
    def press(self, kbd, time):
        self.t = time
        self.executed = False
        
    def release(self, kbd, time):
        if( self.executed ):
            kbd.backLayer(self.layer)
        else:
            kbd.keyPress(self.kc)
            kbd.keyRelease(self.kc)
        
    def tick(self, kbd, time):
        if( not self.executed and time-self.t > TAPPING_TERM ):
            kbd.changeLayer(self.layer)
            self.executed = True

class LO(TapPress):
    def __init__(self, kc1, kc2):
        self.kc1 = kc1 #tap
        self.kc2 = kc2 #press
        
    def press(self, kbd, time):
        self.t = time
        self.executed = False
        
    def release(self, kbd, time):
        if( self.executed ):
            kbd.keyRelease(self.kc2)
        else:
            kbd.send(self.kc1)
            
    def tick(self, kbd, time):
        if( not self.executed and time-self.t > TAPPING_TERM ):
            kbd.keyPress(self.kc2)
            self.executed = True

class MO(KeyObject):
    def __init__(self, layer):
        self.layer = layer
        
    def press(self, kbd, time):
        kbd.changeLayer(self.layer)
        
    def release(self, kbd, time):
        kbd.backLayer(self.layer)
        
    def tick(self, kbd, time):
        pass

