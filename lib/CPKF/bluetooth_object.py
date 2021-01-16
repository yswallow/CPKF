import adafruit_ble
from adafruit_ble.advertising import Advertisement
from adafruit_ble.advertising.standard import ProvideServicesAdvertisement
from adafruit_ble.services.standard import BatteryService
from adafruit_ble.services.standard.hid import HIDService as bleHIDService
from adafruit_ble.services.standard.device_info import DeviceInfoService
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode as KC

from cpkf.key_object import KeyObject
import usb_hid
import supervisor
import analogio
import board
import _bleio
import microcontroller
import time
import neopixel


if hasattr(board, "VOLTAGE_MONITOR"):
    batPin = analogio.AnalogIn(board.VOLTAGE_MONITOR)
else:
    batPin = None


def getBatRemain():
    if batPin:
        voltage = batPin.value * 3.3 / 65536 * 2
        percentage = int( (voltage - 3.7) * 200 )
        if percentage > 100 :
            percentage = 100
        elif percentage < 0 :
            percentage = 0
        return percentage
    else:
        return 0
        
bleHID = bleHIDService()
batteryService = BatteryService()
 
device_info = DeviceInfoService(
                                software_revision=adafruit_ble.__version__,
                                manufacturer="Adafruit Industries",
                                hardware_revision="0.0.1",
                                )
advertisement = ProvideServicesAdvertisement(device_info, bleHID, batteryService)
advertisement.appearance = 961
scan_response = Advertisement()
scan_response.complete_name = "CP Keyboard"
 
ble = adafruit_ble.BLERadio()
ble.name = "CircuitPython Keyboard"
#ble._adapter.enabled = False

np = neopixel.NeoPixel(board.NEOPIXEL,1)

def disconnectAll():
    if ble.connected:
        for connection in ble.connections:
            connection.disconnect()


class BT(KeyObject):
    def __init__(self, i):
        super().__init__()
        self.id = i

        address_bytes = bytearray()
        with open("/bt_addresses/BT{}.txt".format(i)) as file:
            line = file.readline()
            for hex in line.split(":"):
                address_bytes.append(int("0x"+hex))
            
        self.address = _bleio.Address(address_bytes, _bleio.Address.PUBLIC);
    
    def press(self, kbd, time):
        ble._adapter.enabled = True
        disconnectAll()
        ble._adapter.connect(self.address, timeout=10)

class BT_EN(KeyObject):
    def __init__(self):
        super().__init__()
        self.disconnected = True
        
    def press(self, kbd, t):
        if not ble._adapter.enabled:
            ble._adapter.enabled = True
            time.sleep(0.5)
        
        if ble.connected:
            print("already connected")
            print(ble.connections)
            self.disconnected = False
            np[0] = 0x0000FF
        elif ble.advertising:
            print("already advertising")
        else:
            print("advertising")
            ble.start_advertising(advertisement, scan_response=scan_response)
            self.disconnected = True
        
        kbd.updateHIDdevice(bleHID.devices)
        
        
    def release(self, kbd, time):
        print(ble.connections)
        
        if ble.connected and self.disconnected:
            batteryService.level = getBatRemain()
            
            np[0] = 0x0000FF
            self.disconnected = False

    def tick(self, kbd, time):
        pass

class BT_CONNECT(KeyObject):
    def press(self, kbd, t):
        if not ble._adapter.enabled:
            ble._adapter.enabled = True
            time.sleep(0.5)
        
        if ble.connected:
            for connection in ble.connections:
                connection.disconnect()
            print("searching new pair...")
            ble.start_advertising(advertisement, scan_response=scan_response)
    
class USB_EN(KeyObject):
    def press(self, kbd, time):
        if(supervisor.runtime.serial_connected):
            kbd.updateHIDdevice(usb_hid.devices)
        
        if ble._adapter.enabled:
            disconnectAll()
            ble.stop_advertising()
            #ble._adapter.enabled = False
            
        np[0] = 0xFF0000

