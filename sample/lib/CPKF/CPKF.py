from adafruit_hid.keyboard import Keyboard
import time
from cpkf.key_object import KeyObject

class CPKFKeyboard:
    def __init__(self, keymap, scan_method):
        self.scan_method = scan_method
        self.keymap = keymap
        self.currentLayer = 0
        self.layerHistory = [self.currentLayer]
        
        self.press = []
        for i in range(len(keymap[0])):
            self.press.append(None)
        
        self.adakbd = Keyboard()
    
    def start(self):
        self.scan_method(self)
        
    def keypress(self, i):
        if not self.press[i]:
            k = self.keymap[self.layerHistory[-1]][i]
            if k:
                print("Button #%d Pressed" % i)
                self.press[i] = k
                
                if type(k) is int:
                    self.adakbd.press(k)
                elif isinstance(k,KeyObject):
                    k.press(self, time.monotonic())
            
            
    def keyrelease(self, i):
        if self.press[i]:
            print("Button #%d released" % i)
            
            k = self.press[i]
            if k:

                if type(k) is int:
                    self.adakbd.release(k)
                elif isinstance(k,KeyObject):
                    k.release(self, time.monotonic())
                
                self.press[i] = None
            
    def superpress(self, kc):
        self.adakbd.press(kc)
        
    def superrelease(self, kc):
        self.adakbd.release(kc)
        
    def send(self, kc):
        # kbd.send()だとmodifierの情報が消える
        self.adakbd.press(kc)
        self.adakbd.release(kc)
        
    def tick(self, t):
        for k in self.press:
            if isinstance(k,KeyObject):
                k.tick(self, t)
                 
    def changeLayer(self, to):
        self.layerHistory.append(to)
    
    def backLayer(self, current):
        self.layerHistory.remove(current)
