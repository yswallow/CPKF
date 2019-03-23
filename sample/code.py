from cpkf.cpkf import CPKFKeyboard
from cpkf.scan.mcp23017 import Scan
import config
import keymap

scan = Scan(config.addresses)
kbd = CPKFKeyboard(keymap=keymap.keymap, scan_method=scan.scan)

kbd.start()

