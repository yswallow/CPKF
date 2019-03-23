# isinstance(obj,key_object.KeyObject)

from adafruit_hid.keycode import Keycode as KC
from config import TAPPING_TERM

class KeyObject:
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
            kbd.superpress(self.kc)
            kbd.superrelease(self.kc)
        
    def tick(self, kbd, time):
        if( not self.executed and time-self.t > TAPPING_TERM ):
            kbd.changeLayer(self.layer)
            self.executed = True

class LO(TapPress):
    def __init__(self, kc1, kc2):
        self.kc1 = kc1 #tap
        self.kc2 = kc2 #press
        
    def press(self, kbd, t):
        self.t = t
        self.executed = False
        
    def release(self, kbd, time):
        if( self.executed ):
            kbd.superrelease(self.kc2)
        else:
            kbd.send(self.kc1)
            
    def tick(self, kbd, time):
        if( not self.executed and time-self.t > TAPPING_TERM ):
            kbd.superpress(self.kc2)
            self.executed = True


class MD(KeyObject):
    def __init__(self, mod, k):
        self.mod = mod
        self.k = k
        
    def press(self, kbd, t):
        kbd.superpress(self.mod)
        kbd.superpress(self.k)
        
    def release(self, kbd, time):
        kbd.superrelease(self.k)
        kbd.superrelease(self.mod)
        
    def tick(self, kbd, time):
        pass


class S(MD):
    def __init__(self, kc1):
        super().__init__(KC.SHIFT, kc1)

        
class TD(KeyObject): # (Press)-> ko1, (Tap, Press)-> ko2
    def __init__(self, ko1, ko2):
        self.previousPress = 0.0
        self.pressedKey = None
        self.ko1 = ko1
        self.ko2 = ko2
        
    def press(self, kbd, time):
        if time - self.previousPress < TAPPING_TERM :
            kbd.superpress(self.ko2)
            self.pressedKey = self.ko2
        
        self.previousPress = time
    
    def release(self, kbd, time):
        k = self.pressedKey
        if k:
            kbd.superrelease(k)
            self.pressedKey = None
            
    def tick(self, kbd, time):
        if not self.pressedKey and time - self.previousPress > TAPPING_TERM :
            kbd.superpress(self.ko1)
            self.pressedKey = self.ko1
        
    def nextKeyPress(self, kbd, time):
         if not self.pressedKey:
            kbd.superpress(self.ko1)
            self.pressedKey = self.ko1

class MO(KeyObject):
    def __init__(self, layer):
        self.layer = layer
        
    def press(self, kbd, time):
        kbd.changeLayer(self.layer)
        
    def release(self, kbd, time):
        kbd.backLayer(self.layer)
        
    def tick(self, kbd, time):
        pass
