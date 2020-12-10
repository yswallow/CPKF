import board
import busio
import adafruit_bus_device.i2c_device as i2c_device
import time

def write(device, reg, val):
    if not device:
        return
    buffer = bytearray(3)
    buffer[0] = reg
    buffer[1] = val
    with device:
        device.write(buffer, end=2)

def readkey(device):
    if(device is None):
        return 0;
    buffer = bytearray(3)
    buffer[0] = 0x12
    with device:
        #device.write(buffer, end=1)
        #device.readinto(buffer, end=2)
        device.write_then_readinto(buffer, buffer,
            out_start=0, out_end=1, in_start=0, in_end=2)
        return buffer[1] << 8 | buffer[0]


class Scan:
    def __init__(self, addresses=[]):
        i2c = busio.I2C(board.SCL, board.SDA)
        
        self.mcps = []
        for i in addresses:
            try:
                self.mcps.append( i2c_device.I2CDevice(i2c, i) )
            except ValueError:
                self.mcps.append(None)
        
        for mcp in self.mcps:
            if mcp:
                for reg in [0x0C, 0x0D, 0x02, 0x03]:
                    write(mcp, reg, 0xFF)
    
    def scan(self, kbd):
        while(True):
            t = time.monotonic()
            for mcp in self.mcps:
                j = self.mcps.index(mcp)
                k = readkey(mcp)
                for i in range(16):
                    l = 16 * j + i
                    if(k & (1<<i)):
                        kbd.physicalKeypress(l)
                    else:
                        kbd.physicalKeyrelease(l)
                    
            kbd.tick(time.monotonic())
            #print(time.monotonic()-t) //15ms程度
