from adafruit_hid.keyboard import Keyboard
from adafruit_hid.mouse import Mouse
import time, usb_hid, supervisor
from cpkf.key_object import KeyObject
try:
    from config import TAPPING_TERM_FORCE_HOLD
except:
    print("TAPPING_TERM_FORCE_HOLD not found.")
    TAPPING_TERM_FORCE_HOLD = False
    

class CPKFKeyboard:
    def __init__(self, keymap, scan_method):
        self.scan_method = scan_method
        self.keymap = keymap
        self.currentLayer = 0
        self.layerHistory = [self.currentLayer]
        
        self.press = []
        for i in range(len(keymap[0])):
            self.press.append(None)
        
        usb_status = len(usb_hid.devices)
        try:
            if(usb_status):
                self.adakbd = Keyboard(usb_hid.devices)
                self.mouse = Mouse(usb_hid.devices)
            else:
                self.adakbd = None
                self.mouse = None
        except OSError:
            self.adakbd = None
            self.mouse = None
    def updateHIDdevice(self, hid_device=None):
        if self.adakbd:
            try:
                self.release_all()
            except OSError:
                pass
        
        if hid_device :
            self.hid_device = hid_device
        elif supervisor.runtime.serial_connected:
            self.hid_device = usb_hid.devices
        
        print(self.hid_device)
        if self.hid_device :
            self.adakbd = Keyboard(self.hid_device)
            self.mouse = Mouse(self.hid_device)
            
            
    def start(self):
        print( TAPPING_TERM_FORCE_HOLD if "TTFH is True" else "TTFH is False" )
        self.scan_method(self)
        
    def physicalKeypress(self, i):
        if not self.press[i]:
            if TAPPING_TERM_FORCE_HOLD :
                for k in self.press:
                    if isinstance(k, KeyObject):
                        k.force_tick(self)
            
            k = self.keymap[self.layerHistory[-1]][i]
            if k:
                print("Button #%d Pressed" % i)
                self.press[i] = k
                self.keyPress(k)


    def keyPress(self, k):
        if (self.adakbd is None) and supervisor.runtime.serial_connected:
            self.adakbd = Keyboard(usb_hid.devices)
            self.mouse = Mouse(usb_hid.devices)
        
        if type(k) is int:
            modifier_bit = k>>8
            if modifier_bit:
                self.adakbd.report_modifier[0] |= modifier_bit
            self.adakbd.press(k&0xFF)

        elif isinstance(k,KeyObject):
            k.press(self, time.monotonic())
    

    def physicalKeyrelease(self, i):
        if self.press[i]:
            print("Button #%d released" % i)
            
            k = self.press[i]
            if k:
                self.keyRelease(k)
                self.press[i] = None

    def keyRelease(self, k):
        if type(k) is int:
            modifier_bit = k>>8
            if modifier_bit:
                self.adakbd.report_modifier[0] &= ~modifier_bit
            self.adakbd.release(k&0xFF)
        elif isinstance(k,KeyObject):
            k.release(self, time.monotonic())

    def send(self, kc):
        # kbd.send()だとmodifierの情報が消える
        self.adakbd.press(kc)
        self.adakbd.release(kc)
    
    def release_all(self):
        self.adakbd.release_all()
    
    def tick(self, t):
        for k in self.press:
            if isinstance(k,KeyObject):
                k.tick(self, t)

    def changeLayer(self, to):
        self.layerHistory.append(to)
    
    def backLayer(self, current):
        self.layerHistory.remove(current)
