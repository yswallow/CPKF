from adafruit_hid.keyboard import Keyboard
from adafruit_hid.mouse import Mouse
import time, usb_hid, supervisor
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
        
        usb_status = supervisor.runtime.serial_connected
        if(usb_status):
            self.adakbd = Keyboard(usb_hid.devices)
            self.mouse = Mouse(usb_hid.devices)
    
    def updateHIDdevice(self, hid_device):
        if self.adakbd:
            self.release_all()
        self.hid_device = hid_device
        self.adakbd = Keyboard(hid_device)
        self.mouse = Mouse(hid_device)

    def start(self):
        self.scan_method(self)
        
    def physicalKeypress(self, i):
        if not self.press[i]:
            k = self.keymap[self.layerHistory[-1]][i]
            if k:
                print("Button #%d Pressed" % i)
                self.press[i] = k
                self.keyPress(k)


    def keyPress(self, k):
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
