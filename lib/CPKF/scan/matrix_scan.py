import board
import time
import digitalio

class Scan:
    def __init__(self, row_pins=[], col_pins=[], row2col=True):
        self.row_pins = []
        self.col_pins = []
        self.row2col = row2col
    
        for p in row_pins:
            pin = digitalio.DigitalInOut(p)
            pin.direction = digitalio.Direction.INPUT if row2col else digitalio.Direction.OUTPUT
            if row2col :
                pin.pull = digitalio.Pull.UP
            else:
                pin.value = True
            self.row_pins.append(pin)
        
        for p in col_pins:
            pin = digitalio.DigitalInOut(p)
            pin.direction = digitalio.Direction.OUTPUT if row2col else digitalio.Direction.INPUT
            if row2col :
                pin.value = True
            else:
                pin.pull = digitalio.Pull.UP
            self.col_pins.append(pin)
        
        self.col_length = len(self.col_pins);
        self.row_length = len(self.row_pins);

    def scan(self, kbd):
        while(True):
            t = time.monotonic()
            
            if self.row2col:
                for i in range(self.col_length):
                    col = self.col_pins[i]
                    col.value = False
                    time.sleep(0.01)
                    print("col is low")
                    for j in range(self.row_length):
                        row = self.row_pins[j]
                        l = self.col_length*j+i
                        if row.value:
                            kbd.physicalKeyrelease(l)
                        else:
                            kbd.physicalKeypress(l)
                    
                    col.value = True
            else:
                for j in range(self.row_length):
                    row = self.row_pins[j]
                    row.value = False
                    time.sleep(0.01)
                    for i in range(self.col_length):
                        col = self.col_pins[i]
                        l = self.col_length*j+i
                        if col.value:
                            kbd.physicalKeyrelease(l)
                        else:
                            kbd.physicalKeypress(l)
                    
                    row.value = True
            kbd.tick(time.monotonic())
