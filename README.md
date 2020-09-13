# Circuit Python Keyboard Firmware

## Requirements
* Cortex-M4 board
{ nrf52840 board to use Bluetooth }

## Installation
1. copy this repository to `CIRCUITPY` Drive root.
2. copy files to `lib/`from adafruit library
    * `adafruit_bus_device/i2c_device.mpy`
    * `adafruit_hid/__init__.mpy`
    * `adafruit_hid/keycode.mpy`
    * `adafruit_hid/keyboard.mpy`
    * `adafruit_hid/consumer_control.mpy`
    * `adafruit_hid/consumer_control_code.mpy`
    * `adafruit_ble/*` (if you use Bluetooth)
3. copy/make your keyboard definision script in `lib/keyboard/` (samples is in `lib/keyboard-sample/`)
4. copy/make your keymap on `/keymap.py` (sample is `/keymap-sample.py`)
    * if you using non-bluetooth board, DO NOT use/import Bluetooth feature

## More...
Document is in [yswallow/CPKF-doc](https://github.com/yswallow/CPKF-doc) (not created yet).