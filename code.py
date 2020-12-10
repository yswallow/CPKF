import sys
import board
import supervisor
import os

try:
    supervisor.set_rgb_status_brightness(8)
    from cpkf.cpkf import CPKFKeyboard
    import keyboard
    if "keymap.py" in os.listdir():
        import keymap
        kbd = CPKFKeyboard(keymap=keyboard.layouts(keymap.keymap), scan_method=keyboard.Scan.scan)
    else:
        import keyboard.default_keymap
        kbd = CPKFKeyboard(keymap=keyboard.layouts(keyboard.default_keymap.keymap), scan_method=keyboard.Scan.scan)

    kbd.start()

except Exception as err:
    try:
        kbd.release_all();
    except NameError as err2:
        print("Keyboard not Running.")
    else:
        pass
    
    try:
        with open("/log/error.txt", "w") as fp:
            sys.print_exception(err, fp)
    except OSError as err2:
        print("Can't write file.")
    else:
        raise

    raise(err)
