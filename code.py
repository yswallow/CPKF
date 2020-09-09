import sys

try:
    from cpkf.cpkf import CPKFKeyboard
    import keyboard
    import keymap

    kbd = CPKFKeyboard(keymap=keyboard.layouts(keymap.keymap), scan_method=keyboard.Scan.scan)

    kbd.start()

except Exception as err:
    sys.print_exception(err)
    
    try:
        with open("/log/error.txt", "w") as fp:
            sys.print_exception(err, fp)
    except OSError as err2:
        print("Can't write file.")
        sys.print_exception(err2)
    else:
        raise