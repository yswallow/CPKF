import adafruit_ble
from adafruit_ble.advertising import Advertisement
from adafruit_ble.advertising.standard import ProvideServicesAdvertisement
from adafruit_ble.services.standard import BatteryService
from adafruit_ble.services.standard.hid import HIDService as bleHIDService
from adafruit_ble.services.standard.device_info import DeviceInfoService
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode as KC

from cpkf.key_object import KeyObject
import usb_hid, supervisor

bleHID = bleHIDService()
 
device_info = DeviceInfoService(software_revision=adafruit_ble.__version__,
                                manufacturer="Adafruit Industries")
advertisement = ProvideServicesAdvertisement(bleHID)
advertisement.appearance = 961
scan_response = Advertisement()
scan_response.complete_name = "CircuitPython Keyboard"
 
ble = adafruit_ble.BLERadio()

class BT_EN(KeyObject):
    def press(self, kbd, time):
        if not ble.connected:
            print("advertising")
            ble.start_advertising(advertisement, scan_response)
        else:
            print("already connected")
            print(ble.connections)
        
        kbd.updateHIDdevice(bleHID.devices)

    def release(self, kbd, time):
        pass

    def tick(self, kbd, time):
        pass


class USB_EN(KeyObject):
    def press(self, kbd, time):
        if(supervisor.runtime.serial_connected):
            kbd.updateHIDdevice(usb_hid.devices)
            
            if ble.connected:
                for connection in ble.connections:
                    connection.disconnect()
            ble.stop_advertising()
